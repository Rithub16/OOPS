# Parent Class
class Payment:
    def pay(self):
        print("Processing general payment...")

# Child Class 1
class GooglePay(Payment):
    def pay(self):
        print("Payment done using Google Pay")

# Child Class 2
class PhonePe(Payment):
    def pay(self):
        print("Payment done using PhonePe")

# Child Class 3
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")


# Creating Objects
p1 = Payment()
g1 = GooglePay()
ph1 = PhonePe()
c1 = CreditCard()

# Calling pay() method
p1.pay()
g1.pay()
ph1.pay()
c1.pay()
