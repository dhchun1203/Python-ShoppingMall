class Product:
    next_id = 1
    def __init__(self, name, price, stock):
        self.id = Product.next_id
        Product.next_id += 1
        self.name = name
        self.price = price
        self.stock = stock
        
    def is_sold_out(self):
        return self.stock == 0
    
    def __str__(self):
        stock_text = "품절" if self.is_sold_out() else f"재고 {self.stock}"
        return f"{self.id}: {self.name} {self.price:,} {self.stock}({stock_text})"