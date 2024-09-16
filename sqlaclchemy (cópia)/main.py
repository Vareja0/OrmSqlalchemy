from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/flores/", response_model=list[schemas.Flor])
def get_flor(db: Session = Depends(get_db)):
    flores = crud.get_all_flor(db)
    return flores

@app.get("/flores/{id_flor}", response_model=schemas.Flor)
def get_florById(id_flor: int, db: Session = Depends(get_db)):
    flor = crud.get_flor_id(db, id_flor=id_flor)
    if flor is None:
        raise HTTPException(status_code=404, detail="flor nao encontrada")
    return flor

@app.get("/compra/", response_model=list[schemas.Compra])
def get_compra(db: Session = Depends(get_db)):
    compras = crud.get_compra_all(db)
    return compras

@app.get("/compra/{valor}", response_model=schemas.Compra)
def get_compraValor(valor: int, db: Session = Depends(get_db)):
    compra = crud.get_compra_valor(db, valor=valor)
    if compra is None:
        raise HTTPException(status_code=404, detail="compra nao achada")
    return compra

@app.get("/func/", response_model=list[schemas.Funcionario])
def getFunc(db: Session = Depends(get_db)):
    funcs = crud.get_funcionarios(db)
    return funcs

@app.get("/func/{nome}", response_model=schemas.Funcionario)
def getFuncById(nome: str, db: Session = Depends(get_db)):
    func = crud.get_funcionarios_by_nome(db, nome=nome)
    if func is None:
        raise HTTPException(status_code=404, detail="funcionario nao encontrado")
    return func

@app.get("/clientes/", response_model=list[schemas.Cliente])
def getClient(db: Session = Depends(get_db)):
    client = crud.get_clients(db)
    return client

@app.post("/flores/", response_model=schemas.Flor)
def create_Flor(flor: schemas.FlorCreate, db: Session = Depends(get_db)):
    return crud.create_flor(db=db, flor=flor)

@app.post("/compra/", response_model=schemas.Compra)
def create_Compra(compra: schemas.CompraCreate, db: Session = Depends(get_db)):
    return crud.create_compra(db=db, compra=compra)

@app.post("/clientes/", response_model=schemas.ClienteCreate)
def createClient(client: schemas.ClienteCreate, db: Session = Depends(get_db)):
    return crud.create_client(db=db, client=client)

@app.post("/func/", response_model=schemas.FucnionariosCreate)
def createFunc(funcionario: schemas.FucnionariosCreate, db: Session = Depends(get_db)):
    return crud.create_funcionario(db=db, funcionario=funcionario)

@app.delete("/flores/{id_flor}", response_model=schemas.Flor)
def get_florById(id_flor: int, db: Session = Depends(get_db)):
    flor = crud.get_flor_id(db, id_flor=id_flor)
    if flor is None:
        raise HTTPException(status_code=404, detail="flor nao encontrada")
    return crud.delete_flor(flor, db=db)

@app.delete("/func/{nome}", response_model=schemas.Flor)
def getFuncByName(nome: str, db: Session = Depends(get_db)):
    func = crud.get_funcionarios(db, nome=nome)
    if func is None:
        raise HTTPException(status_code=404, detail="flor nao encontrada")
    return crud.delete_func(func, db=db)