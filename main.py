from fastapi import FastAPI

from db import search_template

app = FastAPI()


@app.post("/get_form/")
def get_form(data: dict[str, str]):
    print(f"{data=}")
    return search_template(data)
