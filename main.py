from fastapi import FastAPI, Request

from service import search_template

app = FastAPI()


@app.post("/get_form/")
def get_form(request: Request):
    return search_template(dict(request.query_params))
