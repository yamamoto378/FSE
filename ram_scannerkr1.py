import requests

url = "https://catalog.onliner.by/sdapi/catalog.api/search/dram?group=0&group_limit=0&limit=30&shops%5B0%5D=6498&shops%5Boperation%5D=union"

amounts = []

for page_index in range(1, 40):
 new_url = f"{url}&page={page_index}"
 response = requests.get(new_url)
 products = response.json()["products"]
 for product in products:
  print(product["prices"]["price_min"]["amount"])
  amounts.append(float(product["prices"]["price_min"]["amount"]))
 print("---------------------------------------")

amounts.sort()

print(amounts[0])
