from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://obxqzixtdpzvli:ef71255a7f129581653cd314a71f2e0953de62dd060a3fcd06decf521039e922@ec2-174-129-27-3.compute-1.amazonaws.com:5432/d955r77iqaur5c"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()