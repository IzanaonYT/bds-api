from fastapi import FastAPI

# .\run.bat

app = FastAPI()

@app.get("/api/bdfd/funcion/{funcion}/{texo}")
def read_root(funcion: str, texo: str=None):
    if texo is None:
        texo = "Nada proporcionado"
    
    return {"funcion": funcion, "texto": texo}
