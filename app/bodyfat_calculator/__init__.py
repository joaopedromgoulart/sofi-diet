from enum import Enum
from pydantic import BaseModel
from app.bodyfat_calculator.calculators import BodyFat
from app.bodyfat_calculator.calculators.petroski import BodyFatFromPetrosky


def calculator_factory(strategy: str) -> BodyFat:
    if strategy == 'PETROSKI':
        return BodyFatFromPetrosky
    raise NotImplementedError()


def calculate(strategy: str, payload: BaseModel):
    calculator_class = calculator_factory(strategy=strategy)
    body_fat_calculator: BodyFat = calculator_class(payload)
    return body_fat_calculator.calculate()


if __name__ == '__main__':
    t_result = calculate(
        strategy='PETROSKI',
        payload={
            'gender': 'H',
            'age': 50,
            'dobras': {
                'sobrescapular': 0.1,
                'triceps': 0.1,
                'suprailiaca': 0.1,
                'panturrilha_medial': 0.1
            }
        }
    )
    print(t_result)
