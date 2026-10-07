import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = os.environ.get(
    'DATABASE_URL',
    'mysql+mysqlconnector://root:Jcgomezj7699*@localhost:3306/db_crud_fastapi'
)
engine = create_engine(
    DATABASE_URL,
    echo=os.environ.get('DB_ECHO', 'true').lower() == 'true',
    pool_size=20,
    pool_recycle=3600,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()