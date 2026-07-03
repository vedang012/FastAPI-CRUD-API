from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from models import Product
from database import session, engine
import database_models
from sqlalchemy.orm import Session
from sqlalchemy import select


app = FastAPI()

database_models.Base.metadata.create_all(bind = engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return "namaste unc!"


@app.get("/products")
def get_products(db : Session = Depends(get_db)):
    db_products = db.execute(select(database_models.Product)).scalars().all()
    return db_products

@app.get("/product/{id}")
def get_product_by_id(id:int, db : Session = Depends(get_db)):
    db_product = db.get(database_models.Product, id)

    if db_product is None:
        raise HTTPException(
            status_code = 404,
            detail = "product not found"
        )
    return db_product


@app.post("/product")
def add_prod(product: Product, db : Session = Depends(get_db)):

    db_product = database_models.Product(
        name = product.name,
        price = product.price,
        id = product.id
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.put("/product/{id}")
def update_prod(id: int, product : Product, db: Session = Depends(get_db)):

    db_product = db.get(database_models.Product, id)

    if db_product is None: 
        raise HTTPException(
            status_code = 404,
            detail = "product not found"
        )
    
    db_product.name = product.name
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)
    
    return db_product

@app.delete("/product/{id}")
def delete_prod(id: int, db : Session = Depends(get_db)):

    db_product = db.get(database_models.Product, id)

    if db_product is None:
        raise HTTPException(
            status_code = 404,
            detail = "product not found"
        )
    
    db.delete(db_product)
    db.commit()
    return {"message": "Product deleted successfully"}    