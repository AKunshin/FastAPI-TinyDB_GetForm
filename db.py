from tinydb import TinyDB, Query

from helpers import get_value_type

db = TinyDB("templates.json")

Template = Query()


db.insert(
    {
        "name": "OrderForm",
        "client_name": "text",
        "client_email": "email",
        "client_phone": "phone",
        "order_date": "date",
    }
)
db.insert(
    {
        "name": "RegistrationForm",
        "user_name": "text",
        "user_email": "email",
        "user_password": "text",
        "registration_date": "date",
    }
)
db.insert(
    {
        "name": "CommentForm",
        "author_name": "text",
        "author_phone": "phone",
        "text_comment": "text",
    }
)


def search_template(request_params):
    request_with_types = {k: get_value_type(v) for k, v in request_params.items()}
    template = db.search(Query().fragment(request_with_types))
    if template:
        return template[0]["name"]
    return request_with_types
