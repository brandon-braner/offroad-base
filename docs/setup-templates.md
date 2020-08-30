# Setup UI Templates

## Jinja 2
```bash
pip install jinja2
pip install aiofiles
```


Add Jinja to main.py 
```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def root():
    return {"message": "Hello World"}
```

Create templates folder
```bash
mkdir tempaltes
```