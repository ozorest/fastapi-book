from os import path
from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, PlainTextResponse, RedirectResponse, FileResponse, Response

app = FastAPI()

@app.get("/html", response_class=HTMLResponse)
async def get_html():
    return """
        <html>
            <head>
                <title>Olá mundo!</title>
            </head>
            <body>
                <h1>Ola mundo!</h1>            
            </body>
        </html>
    """

@app.get("/text", response_class=PlainTextResponse)
async def get_text():
    return "Ola, mundo!"

@app.get("/redirect")
async def redirect():
    return RedirectResponse("/new-url", status_code=status.HTTP_301_MOVED_PERMANENTLY)

@app.get("/cat")
async def get_cat():
    root_directory = path.dirname(path.dirname(__file__))
    picture_path = path.join(root_directory, "assets", "cat.png")
    return FileResponse(picture_path)

@app.get("/xml")
async def get_xml():
    content = """
        <?xml version="1.0" encoding="UTF-8"?>
        <Ola>Mundo</Ola>
    """
    return Response(content=content, media_type="application/xml")
