from starlette.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "<h1 style='color: red;'>Hello World</h1>" in response.text
