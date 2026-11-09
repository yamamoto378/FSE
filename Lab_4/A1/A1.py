import random
import time


N = int(input("Введите количество примеров: "))

correct_count = 0  
total_time = 0.0  
for i in range(N):

    a = random.randint(2, 9)
    b = random.randint(2, 9)

    while True:

        start_time = time.time()

        try:

            answer = int(input(f"{a} * {b} = "))


            time_spend = time.time() - start_time
            total_time += time_spend

            break  
        except ValueError:

            print("Пожалуйста, введите целое число")


    if answer == a * b:
        print("Правильно!")
        correct_count += 1
    else:
        print(f"Неправильно. Правильный ответ: {a * b}")
average_time = total_time / N if N > 0 else 0
success_percentage = (correct_count / N) * 100 if N > 0 else 0
print("\n--- Статистика ---")
print(f"Общее время, затраченное на ответы: {total_time:.2f} сек.")
print(f"Среднее время на один пример: {average_time:.2f} сек.")
print(f"Количество правильных ответов: {correct_count}")
print(f"Процент правильных ответов: {success_percentage:.1f}%")
