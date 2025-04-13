from fastapi.testclient import TestClient
from .main import app
import json

client = TestClient(app)

def test_health():
     res = client.get("/health")
     assert res.status_code == 200
     assert res.json() == {"status": "healthy"}


def test_make_prediction_that_should_work():
     res = client.post("/pred", content= json.dumps({"is_black" : True, "curr" : {'board': [2, 0, 0, 0, 0, -5, 0, -3, 0, 0, 0, 5, -5, 0, 0, 0, 3, 0, 5, 0, 0, 0, 0, -2], 'whiteCaught': 0, 'blackCaught': 0, 'blackBearing': False, 'whiteBearing': False, 'blackOutside': 0, 'whiteOutside': 0, 'ended': False} }) )
     json_res =  res.json()
     required_keys = ["prediction_id", "curr", "next_state", "err_msg"]
     #assert all(key in json_res for key in required_keys)