
#Your internal code expects this interface
class PaymentProcessor:
    def pay(self, amount:float, currency:str):
        pass
    
#But Stripe's API looks like
class Stripe:
    def create_charge(self, amount_cents:int, currency:str):
        print(f"Stripe: Charged {amount_cents} cents in {currency}")
        
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe):
        self.stripe = stripe
    
    def pay(self, amount:float, currency:str):
        cents = int(amount * 100)
        self.stripe.create_charge(cents, currency)
        
def create_payment(processor:PaymentProcessor):
    processor.pay(25.0, "USD")
    
create_payment(StripeAdapter(Stripe()))