from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL

db_url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="",
    host="localhost",
    port=5432,
    database="fastapitest",
)

engine = create_engine(db_url)

session = sessionmaker(
    autoflush = False, 
    autocommit = False, 
    bind=engine
)