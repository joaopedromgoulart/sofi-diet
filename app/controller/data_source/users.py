from pydantic import BaseModel
from datetime import date
from abc import ABC, abstractmethod
from typing import List, Union


class Paciente(BaseModel):
    cpf: str
    nome: str
    data_nascimento: date
    id_plano: int
    id_nutri: int


class Nutricionista(BaseModel):
    cpf: str
    nome: str
    id_plano: str


class UsersService(ABC):
    @abstractmethod
    def list_pacientes(self, nutri_id: str) -> List[Paciente]:
        'Retornar todos os pacientes atendidos por determinado nutricionista'

    @abstractmethod
    def get_paciente(self, cpf: str) -> Paciente:
        'Retorna um paciente, buscando pelo cpf'

    @abstractmethod
    def get_nutricionista(self, cpf: str) -> Union[Nutricionista, None]:
        'Retorna o nutricionista buscando pelo CPF'
