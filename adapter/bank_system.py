class LegacyBank:
    def make_transfer(self, amount:float):
        print(f"Legacy Bank: Transferring ${amount}")
        
class PaymentProcessor:
    def pay(self, amount:float):
        pass
    
# class BankAdapter(PaymentProcessor):
#     def __init__(self, legacy_bank:LegacyBank):
#         self.legacy_bank = legacy_bank
        
#     def pay(self, amount:float):
#         print("Adapter converting interface....")
#         self.legacy_bank.make_transfer(amount)
        
class BankAdapter(LegacyBank, PaymentProcessor):
    def pay(self, amount:float):
        self.make_transfer(amount)
        
def make_payment(processor:PaymentProcessor):
    processor.pay(100)
    
make_payment(BankAdapter())