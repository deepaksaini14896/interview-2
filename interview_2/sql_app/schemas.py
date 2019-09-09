from typing import List
from pydantic import BaseModel

class UserBase(BaseModel):
	pincode: str


class LatCreate(UserBase):
    lat: float


class LngCreate(LatCreate):
    lng: float


class Distance(LngCreate):
	distance: int

	class Config:
		orm_mode = True