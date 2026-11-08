x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

#Определяем цвет первой клетки
if (x1 + y1) % 2 == 0:
    color1 = "White"
else:
    color1 = "Black"

#Определяем цвет второй клетки
if (x2 + y2) % 2 == 0:
    color2 = "White"
else:
    color2 = "Black"

#Проверяем совпадение цветов и выводим результат
if color1 == color2:
    print("YES")
    print(color1)
else:
    print("NO")

