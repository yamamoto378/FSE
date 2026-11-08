prev = int(input())
curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

cost = 21.0
if used > 300:
    tier2 = min(used, 600) - 300
    cost += tier2 * 0.06
if used > 600:
    tier3 = min(used, 800) - 600
    cost += tier3 * 0.04
if used > 800:
    tier4 = used - 800
    cost += tier4 * 0.025

avg_price = cost / used if used > 0 else 0.0

print(f"{'Предыдущее':^14}{'Текущее':^14}{'Использовано':^16}{'К оплате':^14}{'Ср. цена m^3':^16}")
print(f"{prev:^14}{curr:^14}{used:^16}{cost:^14.2f}{avg_price:^16.2f}")

