
while True:
    a = input("Введіть сторону а: \n")
    try:
        a = float(a)
        break
    except:
        print("Введіть тільки числа.")
        a = input("Введіть сторону а: \n")

while True:
    b = input("Введіть сторону b: \n")
    try:
        b = float(b)
        break
    except:
        print("Введіть тільки числа.")
        b = input("Введіть сторону b: \n")
S = a * b
print(f"Площа дорівнює {S}.")
