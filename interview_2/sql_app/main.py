from typing import List

from fastapi import Depends, FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder

from sqlalchemy.orm import Session
from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:  
        request.state.db.close()
    return response


# Dependency
def get_db(request: Request):
    return request.state.db


@app.get("/get_using_postgres/{lat}&{lng}&{distance}", response_model=schemas.Distance)
def read_user(lat: float, lng: float, distance: int, db: Session = Depends(get_db)):
    db_user = crud.get_address_postgres(db, lat=lat, lng=lng, distance=distance)
    if db_user is False:
        raise HTTPException(status_code=404, detail="Latitude and Longitude are not exist.")
    else:
        json_compatible_item_data = jsonable_encoder(db_user)
        db_pincode=[]
        for i in json_compatible_item_data:
            db_pincode.append({"pincode":i['pincode']})
        return JSONResponse(content=db_pincode)


@app.get("/get_using_self/{lat}&{lng}&{distance}", response_model=schemas.Distance)
def read_user(lat: float, lng: float, distance: int, db: Session = Depends(get_db)):
    db_user = crud.get_address_self(db, lat=lat, lng=lng, distance=distance)
    if db_user is False:
        raise HTTPException(status_code=404, detail="Latitude and Longitude are not exist.")
    else:
        json_compatible_item_data = jsonable_encoder(db_user)
        db_pincode=[]
        for i in json_compatible_item_data:
            db_pincode.append({"pincode":i['pincode']})
        return JSONResponse(content=db_pincode)
