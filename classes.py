class Complex: 
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
    
    def method(self):
        print("Something this way comes")

# Basic Class interactions
#
# print(Complex(3.0, -4.5))
# print((Complex(3.0, -4.5)).r)
# print((Complex(3.0, -4.5)).i)

# Referencing a raw class object and using it later
#
# class_obj = Complex(3.0, -4.5)
# method_obj = class_obj.method
# print(method_obj) #raw object
# print(method_obj()) # running the function

# The nature of classes in Python 
#
x = Complex(3.0, -4.5)
# these are the same way of refering to a class method
x.method()
Complex.method(x)