from sqlalchemy.orm import Session
from . import models
import numpy as np


def get_address_postgres(db: Session, lat: float, lng: float, distance: int):
    db.execute("CREATE EXTENSION IF NOT EXISTS cube")
    db.execute("CREATE EXTENSION IF NOT EXISTS earthdistance")
    if db.query(models.GPS).filter(models.GPS.lat == lat, models.GPS.lng == lng).first():
    	return db.execute("SELECT * FROM gps WHERE earth_box(ll_to_earth({}, {}), {}) @> ll_to_earth(lat, lng)".format(lat, lng, distance*1000)).fetchall()
    else:
    	return False

def get_address_self(db: Session, lat: float, lng: float, distance: int):
	radius=6371
	maxlat=lat+np.rad2deg(distance/radius)
	minlat=lat-np.rad2deg(distance/radius)
	maxlng=lng+np.rad2deg(distance/radius/np.cos(np.deg2rad(lat)))
	minlng=lng-np.rad2deg(distance/radius/np.cos(np.deg2rad(lat)))
	if db.query(models.GPS).filter(models.GPS.lat == lat, models.GPS.lng == lng).first():
		return db.query(models.GPS).filter(models.GPS.lat >= minlat, models.GPS.lng >= minlng, models.GPS.lat <= maxlat, models.GPS.lng <= maxlng).all()
	else:
		return False
