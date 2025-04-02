from fastapi import FastAPI
import logging

app = FastAPI()

logger = logging.getLogger(__name__)

@app.get("/hey")
def hello():
    logger.info("processing")
    return {"hey" : "hello"}


# make move

#start game

# stop game

