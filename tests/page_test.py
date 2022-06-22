import tests
import pytest
def test_homepage(client):
    response = client.get("/")
    assert response.status_code = 200