def draw_rectangle(rows, columns, ch='#'):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print()
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
draw_rectangle(n, m)

