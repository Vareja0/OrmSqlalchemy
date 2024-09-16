from pydantic import BaseModel
from datetime import date

class FlorBase(BaseModel):
    tipo: str
    cor: str

class FlorCreate(FlorBase):
    pass

class Flor(FlorBase):
    id: int

    class Config:
        orm_mode = True

class CompraBase(BaseModel):
    quantidade: int
    valor: int | None = None
    id_flor: int
    id_cliente: int

class CompraCreate(CompraBase):
    pass

class Compra(CompraBase):
    id: int
    

    class Config:
        orm_mode = True

class ClienteBase(BaseModel):
    nome: str
    cpf: int

class ClienteCreate(ClienteBase):
    pass

class Cliente(ClienteBase):
    pass

    class Config:
        orm_mode = True 

class FuncionariosBase(BaseModel):
    nome: str
    data_nasc: date
    tipo: str
    cpf: int

class FucnionariosCreate(FuncionariosBase):
    pass

class Funcionario(FuncionariosBase):
    pass

    class Config:
        orm_mode = True