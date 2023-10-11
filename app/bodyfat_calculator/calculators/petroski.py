from pydantic import BaseModel
from app.bodyfat_calculator.calculators import BodyFat


class Dobras(BaseModel):
    sobrescapular: float
    triceps: float
    suprailiaca: float
    panturrilha_medial: float


class PetroskyFeatures(BaseModel):
    gender: str
    age: int
    dobras: Dobras



class BodyFatFromPetrosky(BodyFat):
    _dobras_relevantes_homen = ['sobrescapular', 'triceps', 'suprailiaca', 'panturrilha_medial']
    _dobras_relevantes_mulher = []

    def __init__(self, features: dict) -> None:
        self._features = PetroskyFeatures(**features)

    @property
    def dobras_relevantes(self) -> list:
        if self._features.gender == 'H':
            return self._dobras_relevantes_homen
        elif self._features.gender == 'M':
            return self._dobras_relevantes_mulher
        else:
            raise NotImplementedError()

    @property
    def densidade_corporal(self) -> float:
        soma_dobras_relevantes = sum([getattr(self._features.dobras, d) for d in self.dobras_relevantes])
        return (1.10726863 -
                0.00081201*soma_dobras_relevantes +
                0.00000212*soma_dobras_relevantes - 
                0.00041761*self._features.age)

    def calculate(self):
        return ((4.95/self.densidade_corporal) - 4.50) * 100
