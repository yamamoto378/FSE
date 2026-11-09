def is_valid_number(num):
    return num.isdigit() and len(num) in [13, 15, 16]
def get_check_sum(num):
    total = 0
    reverse_digits = num[::-1]
    for idx, char in enumerate(reverse_digits):
        digit = int(char)
        if idx % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
    return total
def get_card_type(num):
    length = len(num)
    if (length == 13 or length == 16) and num.startswith("4"):
        return "Visa"
    if length == 15 and (num.startswith("34") or num.startswith("37")):
        return "American Express"
    if length == 16 and any(num.startswith(prefix) for prefix in ["51", "52", "53", "54", "55"]):
        return "Master Card"
    return "Invalid"
card = input("Введите номер банковской карты: ").strip()

if is_valid_number(card) and get_check_sum(card) % 10 == 0:
    print(get_card_type(card))
else:
    print("Invalid")

