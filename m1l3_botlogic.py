import random

def generate_password(length):
    elements = "+-/*!&$#?=@<>123456789"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password
    
