from pydantic import BaseModel
from datetime import date
from abc import ABC, abstractmethod
from typing import List, Union


class medidas_gerais(BaseModel):
    cpf: str
    id_cliente: int
    peso: float
    altura: float
    data_medida: date


class dobras(BaseModel):
    id: int
    cpf_cliente: str
    data_medida: date
    dobra_triceps: float
    dobra_subesccapular:float
    dobra_axilar_media: float
    dobra_suprailiaca: float
    dobra_abdomem: float
    dobra_peitoral: float
    dobra_coxa: float
    dobra_biceps: float
    dobra_panturrilha: float

class circunferencias(BaseModel):
    id:int
    cpf_cliente:str
    data_medida: date
    circunf_cintura: float
    circunf_quadril: float 
    circunf_abdomem: float 
    circunf_pescoco: float
    circunf_torax: float
    circunf_coxa_prox: float
    circunf_coxa_meso: float
    circunf_panturillha: float
    circunf_braco: float 
    circunf_braco_contraido: float
    circunf_antebraco: float
    circunf_punho: float

class bioimpedancia(BaseModel):
    id: int
    cpf_cliente:str
    data_medida: date
    pct_gordura: float
    gordura_absoluta: float
    massa_magra: float
    pct_massa_magra: float
    imc: float
    taxa_metabolica_basal:int
    peso_ideal: float
    agua_L: float
    pct_agua: float
    pct_agua_ideal: float



class UserService(ABC):
    @abstractmethod
    def list_bioimpedancia(self, cpf_cliente:str) -> List[bioimpedancia]:
        'Retornar todas as bioimpedancias do paciente'

    @abstractmethod
    def list_circunferencias(self, cpf_cliente:str) -> List[circunferencias]:
        'Retornar todas as medidas de circunferencias do paciente'

    @abstractmethod
    def list_dobras(self, cpf_cliente:str) -> List[dobras]:
        'Retornar todas as medidas de dobras do paciente'

    @abstractmethod
    def list_medidas_gerais(self, cpf_cliente:str) -> List[medidas_gerais]:
        'Retornar todas as medidas de dobras do paciente'

