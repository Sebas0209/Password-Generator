import random

letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

user_create = int(input("Introduce la longitud de tu contraseña: \n"))
user_password = ""

for i in range(user_create):
    user_password += random.choice(letters)

print("Tú nueva contraseña generada es: ", user_password)
