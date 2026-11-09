packets = input().strip()
if len(packets) < 5:
    print("Ошибка: длина меньше 5")
    exit()
if not all(char in '01' for char in packets):
    print("Неверный ввод. Используйте только символы '0' и '1'!")
    exit()
total = len(packets)
lost = packets.count('0')
max_zeros = 0
current_zeros = 0
for char in packets:
    if char == '0':
        current_zeros += 1
        if current_zeros > max_zeros:
            max_zeros = current_zeros
    else:
        current_zeros = 0
pct = (lost / total) * 100
if 0 <= pct <= 1:
    res = "отличное"
elif 1 < pct <= 5:
    res = "Хорошее качество"
elif 5 < pct <= 10:
    res = "Удовлетворительное качество"
elif 10 < pct <= 20:
    res = "Плохое качество"
else:
    res = "критическое состояние сети"
print("\nВывод:")
print(f"Общее количество пакетов: {total}")
print(f"Количество потерянных пакетов: {lost}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_zeros}")
print(f"Процент потерь: {pct:.1f}%")
print(f"Качество связи: {res}")
