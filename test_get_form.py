import json

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_template_only_by_existing_fields():
    params = {
        "client_name": "Tony Stark",
        "client_email": "ironman@marvel.com",
        "client_phone": "+7 999 987 65 65",
        "order_date": "15.11.2023",
    }
    response = client.post("/get_form/", params=params)
    assert response.status_code == 200
    assert response.text == '"OrderForm"'


def test_get_template_with_filds_from_diffrent_templates():
    params = {
        "user_name": "Piter Parker",
        "user_email": "spiderman@marvel.com",
        "user_password": "Secret",
        "registration_date": "2023-11-14",
        "author_phone": "+7 987 125 52 52",
        "text_comment": "Comment user",
        "author_name": "Stive",
    }
    response = client.post("/get_form/", params=params)
    assert response.status_code == 200
    assert response.text == '"RegistrationForm"'


def test_not_found_template():
    params = {
        "user": "Eddie Brock",
        "mail": "venom@marvel.com",
        "pass": "Secret",
        "registr_date": "2023-11-14",
    }
    response = client.post("/get_form/", params=params)
    assert response.status_code == 200
    assert (
        response.text
        == '{"user":"text","mail":"email","pass":"text","registr_date":"date"}'
    )
