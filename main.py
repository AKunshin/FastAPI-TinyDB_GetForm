from fastapi import FastAPI

from service import search_template

app = FastAPI()


@app.post("/get_form/")
def get_form(data: dict[str, str]):
    return search_template(data)
