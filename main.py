from fastapi import FastAPI, HTTPException
from json_db import JsonDB
from product import Product

app = FastAPI()

productDB = JsonDB(path='./data/products.json')

@app.get('/products')
def get_laget_products():
    products = productDB.read()
    return {"products": products}

@app.post('/products')
def create_products(product: Product):
    productDB.insert(product)
    return {"status": "inserted"}

@app.put('/products/{product_id}')
def update_product(product_id: int, product: Product):
    if not productDB.update(product_id, product):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "updated"}

@app.delete('/products/{product_id}')
def delete_product(product_id: int):
    if not productDB.delete(product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"status": "deleted"}