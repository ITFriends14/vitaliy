import turtle
# turtle.color("red")
# for i in range(4):
#     turtle.right(90)
#     turtle.forward(150)

# buba = input('Введите число:')
# bubas = input ('Введите число:')

# if buba != bubas:
#     print(f'{buba} не равно {bubas}')

# else:
#     print(f'{buba} равно {bubas}')

# while True:
#     buba1 = int(input())
#     buba2 = int(input())
#     s = input()
#     if type(buba1) == type(buba2):
#         if type(s) == str:
#             if s == "+":
#                 print(buba1 + buba2)
#             if s == "-":
#                 print(buba1 - buba2)
#             if s == "*":
#                 print(buba1 * buba2)
#             if s == "/":
#                  print(buba1 / buba2)
#             if s == "exit":
#                 break
while True:
    s = input('Введите фигуру: ').split(',')

    if s[0] == "квадрат": 
        for i in range(4):
            if len(s) > 1:
                turtle.right(int(s[1]))
                if len(s) > 2:
                    turtle.forward(int(s[2]))
                else:
                    turtle.right(int(s[1]))
                    turtle.forward(100)
            else:
                turtle.right(90)
                turtle.forward(100)
    elif s[0] == "круг":
        for i in range(25):
            turtle.right(15)
            turtle.forward(10)
    else:
        break