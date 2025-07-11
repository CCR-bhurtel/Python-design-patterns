from stripe_example import PaymentProcessor

class OrderService:
    def __init__(self, payment_processor: PaymentProcessor):
        self.payment_processor = payment_processor
        
    def checkout(self, amount:float):
        self.payment_processor.pay(amount)
        
# Now We can inject any type of Processor like Stripe, Paypal etc that implements PaymentProcessor