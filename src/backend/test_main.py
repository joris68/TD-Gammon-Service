


from fastapi.testclient import TestClient
from .main import app
import json

client = TestClient(app)


def test_route():
    res = client.get("/hey")
    assert res.json() == {"hey" : "hello"}
    print("actually tested itS")

