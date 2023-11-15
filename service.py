import re

from collections import Counter
from tinydb import Query
from fill_db import db


def _get_value_type(value):
    test = {
        "date": "|".join(
            [r"(\d{4})-(\d{1,2})-(\d{1,2})", r"(\d{1,2})\.(\d{1,2})\.(\d{4})"]
        ),
        "phone": r"^(\+7)\s(\d{3})\s(\d{3})\s(\d{2})\s(\d{2})$",
        "email": r"^\S+@\w+.\w{2,4}$",
    }
    for value_type, r in test.items():
        if re.fullmatch(r, value):
            return value_type
    return "text"


def _find_most_common_template(request_with_types: dict[str, str]) -> str:
    find_templates = []
    for field_name, field_type in request_with_types.items():
        template = db.search(Query().fragment({field_name: field_type}))
        if template:
            find_templates.append(template[0]["name"])
    if find_templates:
        most_common_template = Counter(find_templates).most_common(1)[0][0]
        print(f"{most_common_template=}")
        return most_common_template


def search_template(request_params: dict[str, str]) -> str | dict[str, str]:
    request_with_types = {k: _get_value_type(v) for k, v in request_params.items()}
    if most_common_template := _find_most_common_template(request_with_types):
        return most_common_template
    return request_with_types
