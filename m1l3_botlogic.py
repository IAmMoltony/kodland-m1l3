import random

def generate_password(length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(length):
        password += random.choice(elements)
    return password
    
