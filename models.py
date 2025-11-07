from pydantic import BaseModel

class Product(BaseModel):
    id:int
    name:str
    description:str
    price:float
    quantity:int


# class UpdateProduct(BaseModel):
#     name:str | None = None
#     description:str | None = None
#     price:float | None = None
#     quantity:int | None = None

    



    
