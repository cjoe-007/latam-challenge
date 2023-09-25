from pydantic import BaseModel

class FlightPredictionInput(BaseModel):
    Fecha_I: str
    Vlo_I: int
    Ori_I: str
    Des_I: str
    Emp_I: str
