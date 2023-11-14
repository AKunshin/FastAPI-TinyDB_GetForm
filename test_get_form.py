import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_template():
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
    }

    # data = {
    #     "user_name": "Piter Parker",
    #     "user_email": "spiderman@marvel.com",
    #     "registration_date": "2023-11-14"

    # }
    data = {
        "registration_dat": "14-11-2023"

    }
    response = client.post("/get_form/", data=json.dumps(data), headers=headers)
    print(response.text)
    assert response.status_code == 200
    assert response.text == '"RegistrationForm"'
