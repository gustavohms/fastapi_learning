import json
from pydantic import BaseModel

from product import Product


class JsonDB(BaseModel):
    path: str

    def read(self):
        with open(self.path, 'r') as f:
            data = json.loads(f.read())
        return data
    
    def write(self, data):
        with open(self.path, 'w') as f:
            f.write(json.dumps(data, indent=4))
    
    def insert(self, product: Product):
        data = self.read()
        data['products'].append(product.dict())
        self.write(data)
    
    def update(self, id: int, new_product: Product):
        data = self.read()
        for i, product in enumerate(data['products']):
            if product['id'] == id:
                data['products'][i] = new_product.dict()
                self.write(data)
                return True
        return False
    
    def delete(self, id: int):
        data = self.read()
        for i, product in enumerate(data['products']):
            if product['id'] == id:
                del data['products'][i]
                self.write(data)
                return True
        return False