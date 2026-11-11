from product import Product

class Cart:
    def __init__(self):
        self.items = []
        
    def add(self, product, qty):
        if product.is_sold_out():
            print("품절된 상품입니다.")
            return 
    
    
    def remove
    
    
    def is_empty


    def subtotal


    def shipping

    def total

    def show 

    def checkout