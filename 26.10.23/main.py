from turtle import Turtle

a = Turtle()
a.color('red')
a.width(5)
a.speed(1)

print("Що бажаєте намалювати?")
print("1-квадратик")
print("2-трикутничок")
print("3-багатокутничок")

choice = input("? \n")

if choice == "1":
    side = int(input("Введіть сторону квадрата: \n"))
# int, а не float, бо ціле число для пікселів

    def square(side1): #за межами функція може бути іншою, тому передаємо
    # замість
    # a.speed(1)
    # a.forward(200)
    # a.left(90)
    # a.forward(200)
    # a.left(90)
    # a.forward(200)
    # a.left(90)
    # a.forward(200)
    # a.left(90)
        print(side1)
        for i in range(4):
            a.forward(side1)
            a.left(90)

    square(side)
    a.screen.mainloop()

elif choice == "2":
    side = int(input("Введіть сторону трикутника: \n"))
    def triangle(side1): 

        print(side1)
        for i in range(3):
            a.forward(side1)
            a.left(120)

    triangle(side)
    a.screen.mainloop()

else:
    side = int(input("Введіть сторону багатокутника: \n"))
    def triangle(side1): 

        print(side1)
        for i in range(8):
            a.forward(side1)
            a.left(45)

    triangle(side)
    a.screen.mainloop()