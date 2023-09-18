from abc import ABC, abstractmethod

# Define the PaymentProcessor abstract base class (target interface)
class PaymentProcessor(ABC):
    @abstractmethod
    def authorize_payment(self):
        pass

    @abstractmethod
    def capture_payment(self):
        pass

# Define the PaypalAdapter class
class PaypalAdapter(PaymentProcessor):
    def __init__(self, paypal_processor):
        self.paypal_processor = paypal_processor

    def authorize_payment(self):
        self.paypal_processor.authorize()

    def capture_payment(self):
        self.paypal_processor.capture()

# Define the StripeAdapter class
class StripeAdapter(PaymentProcessor):
    def __init__(self, stripe_processor):
        self.stripe_processor = stripe_processor

    def authorize_payment(self):
        self.stripe_processor.authorize()

    def capture_payment(self):
        self.stripe_processor.capture()

# Define the PaypalProcessor class
class PaypalProcessor:
    def authorize(self):
        print("Authorizing payment with Paypal")

    def capture(self):
        print("Capturing payment with Paypal")

# Define the StripeProcessor class
class StripeProcessor:
    def authorize(self):
        print("Authorizing payment with Stripe")

    def capture(self):
        print("Capturing payment with Stripe")

# Client code
if __name__ == '__main__':
    type_of_payment = 'paypal'  # Set the payment gateway type based on your requirements

    if type_of_payment == 'paypal':
        paypal_processor = PaypalProcessor()
        payment_processor = PaypalAdapter(paypal_processor)
    elif type_of_payment == 'stripe':
        stripe_processor = StripeProcessor()
        payment_processor = StripeAdapter(stripe_processor)
    
    # Use the payment processor
    payment_processor.authorize_payment()
    payment_processor.capture_payment()
