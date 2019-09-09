from sqlalchemy import Column, String, Integer, Numeric
from sqlalchemy.schema import Sequence
from .database import Base

class GPS (Base):

    __tablename__ = "gps"

    id = Column(Integer, Sequence('gps_id_seq'), primary_key=True)
    pincode = Column(String)
    address = Column(String)
    city = Column(String)
    lat = Column(Numeric(6,4))
    lng = Column(Numeric(6,4))