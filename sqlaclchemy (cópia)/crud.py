from typing import Optional
from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import delete

def get_all_flor(db: Session):
    return db.query(models.Flor).all()

def get_flor_id(db: Session, id_flor: int):
    return db.query(models.Flor).filter(models.Flor.id == id_flor).first()

def get_compra_all(db: Session):
    return db.query(models.Compra).all()

def get_compra_valor(db: Session, valor: int):
    return db.query(models.Compra).filter(models.Compra.valor == valor).first()

def get_funcionarios(db: Session):
    return db.query(models.Funcionarios).all()

def get_funcionarios_by_nome(db: Session, nome: str):
    return db.query(models.Funcionarios).filter(models.Funcionarios.nome == nome).first()

def get_clients(db: Session):
    return db.query(models.Cliente).all()

def create_flor(db: Session, flor: schemas.FlorCreate):
    db_flor = models.Flor(tipo = flor.tipo, cor = flor.cor)
    db.add(db_flor)
    db.commit()
    db.refresh(db_flor)
    return db_flor

def create_compra(db: Session, compra: schemas.CompraCreate):
    db_compra = models.Compra(quantidade = compra.quantidade, id_flor = compra.id_flor, valor = compra.valor)
    db.add(db_compra)
    db.commit()
    db.refresh(db_compra)
    return db_compra

def create_client(db: Session, client: schemas.ClienteCreate):
    db_client = models.Cliente(cpf = client.cpf, nome = client.nome)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def create_funcionario(db: Session, funcionario: schemas.FucnionariosCreate):
    db_func = models.Funcionarios(cpf = funcionario.cpf, nome = funcionario.nome, data_nasc = funcionario.data_nasc, tipo = funcionario.tipo)
    db.add(db_func)
    db.commit()
    db.refresh(db_func)
    return db_func

def delete_flor(flor: models.Flor, db: Session):
    db.delete(flor)
    db.commit()
    return flor

def delete_func(client: models.Cliente, db: Session):
    db.delete(client)
    db.commit()
    return client
