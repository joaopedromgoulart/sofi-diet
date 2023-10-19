from pydantic import BaseModel
from typing import List
from app.controller.data_source.users import UsersService, Pasciente, Nutricionista


class BasicPacienteInfo:
    cpf: str
    nome: str


class HomeVeiwInfo(BaseModel):
    nutri: str
    pacientes: List[BasicPacienteInfo]


def get_home_data(nutri_id: str) -> HomeVeiwInfo:
    user_svc: UsersService = None # nesse modelo fica simples alterar a forma de acesso ao banco de dados
    nutri = user_svc.get_nutricionista(cpf=nutri_id)
    all_pacientes = user_svc.list_passientes(nutri_id=nutri_id)

    return HomeVeiwInfo(
        nutri=nutri.nome,
        pacientes=[BasicPacienteInfo(**p.dict) for p in all_pacientes]
    )