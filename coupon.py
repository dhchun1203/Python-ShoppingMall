class Coupon:
    def __init__(self, name):
        self.name = name
        
    # 할인 금액 반환
    def discount_amount(self, total):
        return 0
    
# 10% 할인 쿠폰 
class RateDiscount(Coupon):
    # 할인율과 최대 할인율 적용
    def __init__(self, rate, max_discount):
        super().__init__("10% 할인 쿠폰")
        self.rate = rate
        self.max_discount = max_discount
        
    def discount_amount(self, total):
        pass
        # 상품합계 X 10%, 단 5,000원을 넘지 않는다. 원단위 미만은 버림
        
# 정액 할인 쿠폰
class FixedDiscount(Coupon):
    def __init__(self, amount, min_total):
        super().__init__(f"쿠폰이름- {min_total}만원이상 {amount}원 할인쿠폰 ")
        
    def discount_amount(self, total):
        pass
        # 상품 합계가 20,000원 이상이면 3,000원, 아니면 0원