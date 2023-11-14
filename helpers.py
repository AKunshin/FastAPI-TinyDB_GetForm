import re


def get_value_type(value):
    test = {
        "date": r"(\d{4})-(\d{1,2})-(\d{1,2})",
        "date2": r"(\d{1,2})-(\d{1,2})-(\d{4})",
        "phone_number": r"^((\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
        "email": r"^\S+@\w+.\w{2,4}$",
    }
    for value_type, r in test.items():
        if re.fullmatch(r, value):
            return value_type

    return "text"