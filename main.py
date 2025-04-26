from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request
app = FastAPI()
templates = Jinja2Templates(directory=".")

@app.get("/upload/{name} ",response_class=HTMLResponse )
async def reply(request: Request , name = str):
   return templates.TemplateResponse("page.html",{"request":Request, "name": name})
   

