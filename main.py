from fastapi import FastAPI
from models import Product
from config import SessionLocal, engine
import uvicorn
import schema


app =FastAPI()

# Create the database tables
schema.Base.metadata.create_all(bind=engine)


@app.get("/")
def greet():
    return "Hello, FastAPI!"


products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]



def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = SessionLocal()

    count = db.query(schema.Product).count()
    if count == 0:
    
        for product in products:
            db.add(schema.Product(**product.model_dump()))  ## unpacking the pydantic model to match sqlalchemy model 
        db.commit() ## commit the changes to the database


init_db()




@app.get("/products")
def get_products():
    return products


@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return product


@app.put("/product/{product_id}")
def update_product(product_id: int, product: Product):
    for index, existing_product in enumerate(products):
        if existing_product.id == product_id:
            products[index] = product
            return product
    return {"error": "Product not found"}


if __name__ == "__main__":
    
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
