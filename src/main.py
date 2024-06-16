import os
import pathlib
from dotenv import load_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse
from starlette.requests import Request
from pydantic import BaseModel

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from supabase import create_client, Client
import pandas as pd

app = FastAPI()
load_dotenv()

supabase_url = os.environ.get('SUPABASE_URL')
supabase_key = os.environ.get('SUPABASE_KEY')
supabase: Client = create_client(supabase_url, supabase_key)

BASE_DIR = pathlib.Path(__file__).parent


app = FastAPI()
app.mount("/frontend/static", StaticFiles(directory= BASE_DIR/"frontend/static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR/"frontend/template"))

save_count = 0


@app.post("/update")
async def update_data(id: int = Form(...), english: str = Form(...), ibibio: str = Form(...), index: int = Form(...)):
    global save_count
    supabase.table('iko').update({"ENGLISH": english, "IBIBIO": ibibio}).eq("ID", id).execute()
    save_count += 1
    return RedirectResponse(url=f"/?index={index}", status_code=303)



@app.get("/")
async def read_data(request: Request, index: int = 0):
    response = supabase.table('iko').select('ID', 'ENGLISH', 'IBIBIO').range(index, index + 1).execute()
    data = response.data

    total_rows_response = supabase.table('iko').select('ID').execute()
    #total_rows = len(total_rows_response.data)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "data": data[0] if data else None,
        "index": index,
        "save_count": save_count,
    })

@app.get("/speak")
async def read_root(request: Request):
    return templates.TemplateResponse("speech.html", {"request": request})

@app.get("/edit")
async def read_root(request: Request):
    return templates.TemplateResponse("dictionary.html", {"request": request})

@app.get("/about")
async def read_root(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})




# @app.get("/dict")
# async def dict(request: Request):
#     return templates.TemplateResponse("dict.html", {"request": request,})

# @app.get("/supa")
# async def read_data(request: Request, index: int = 0):
#     response = supabase.table('iko').select('ID', 'ENGLISH', 'IBIBIO').range(index, index + 1).execute()
#     data = response.data

#     return templates.TemplateResponse("let.html", {"request": request, "data": data[0] if data else None, "index": index})



# @app.post("/update")
# async def update_data(id: int = Form(...), english: str = Form(...), ibibio: str = Form(...), index: int = Form(...)):
#    supabase.table('iko').update({"ENGLISH": english, "IBIBIO": ibibio}).eq("ID", id).execute()
#   return RedirectResponse(url=f"/?index={index}", status_code=303)

#-------------------------------------------------------------------------------------------------------#
# @app.get("/")
# async def read_data(request: Request, index: int = 0):
#     response = supabase.table('iko').select('ID', 'ENGLISH', 'IBIBIO').range(index, index + 1).execute()
#     data = response.data

#     return templates.TemplateResponse("index.html", {"request": request, "data": data[0] if data else None, "index": index})



# @app.get("/okon")
# async def read_data(request: Request, index: int = 0):
#     response = supabase.table('iko').select('ID', 'ENGLISH', 'IBIBIO').range(index, index + 1).execute()
#     data = response.data

#     return templates.TemplateResponse("supa.html", {"request": request, "data": data[0] if data else None, "index": index})


