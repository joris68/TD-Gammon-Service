from fastapi import FastAPI, status, Response
from src.BackgammonManager import BackgammonManager
from src.BackgammonState import BackgammonState
from src.utils import json_to_backgammonobject, backgammonstate_to_json
from pydantic import BaseModel, model_serializer
from typing import Any
import logging
import numpy as np
import uuid

logger = logging.getLogger(__name__)

manager = BackgammonManager()

app = FastAPI()

class BackgammonStateJson(BaseModel):
     board : list[int]
     whiteCaught : int
     blackCaught : int
     blackBearing: int
     whiteBearing: int
     blackOutside: int
     whiteOutside : int
     ended : bool
     """
     @model_serializer
     def ser_model(self) -> dict[str, Any]:
        return {"board": self.board,
                "whiteCaught" : self.whiteCaught,
                 "blackCaught": self.blackCaught,
                   "blackBearing": self.blackBearing,
                   "whiteBearing": self.whiteBearing,
                   "blackOutside": self.blackOutside,
                   "whiteOutside": self.whiteOutside,
                   "ended": self.ended}
     """

class PredictionRequest(BaseModel):
     is_black : bool
     curr : BackgammonStateJson


class PredictionResponse(BaseModel):
     prediction_id : str
     curr : BackgammonStateJson | None = None
     next_state : BackgammonStateJson | None = None
     err_msg : str | None = None

def create_prediction_id() -> str:
    random_part = ''.join(map(str, np.random.randint(0, 10, size=6)))
    uuid_part = str(uuid.uuid4())[:8]
    return f"pred-{random_part}-{uuid_part}"


@app.post("/pred", status_code=200)
def make_prediction(request : PredictionRequest, response : Response) -> PredictionResponse:
     prediction_id = create_prediction_id()
     logger.info(f"starting to serve prediction request with ID : {prediction_id}")
     next_state : BackgammonState = manager.get_prediction(is_black=request.is_black , curr_state=json_to_backgammonobject(request.curr))
     if next_state is None:
          res = {
               "prediction_id" : prediction_id,
               "err_msg" : "Could not make prediction due to internal error."
          }
          response.status_code = 500
          return res
     else:
          res = {
               "prediction_id" : prediction_id,
               "curr" : request.curr,
               "next_state" : backgammonstate_to_json(next_state)
          }
          return res

@app.get("/health")
def get_health():
     return {"status": "healthy"}