class Payment:
    def __init__(self, method_name, amount):
        self.method_name = method_name
        self.amount = amount

class CreditCardPayment(Payment):
    pass

class PayPalPayment(Payment):
    pass

        
