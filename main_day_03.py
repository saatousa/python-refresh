sales = [
    {"product": "Laptop", "price": 1000},
    {"product": "Phone", "price": 800},
    {"product": "Tablet", "price": 600},
    {"product": "Laptop", "price": 1200}
]

total_sale = 0
for sale in sales:
    # print(sale["product"])
    total_sale += sale["price"]

# print(total_sale)

def highest_sale(sales):
    highest_price = 0
    for sale in sales:
        if sale["price"] > highest_price:
            highest_price = sale["price"]

    print(highest_price)

# highest_sale(sales)

def sold_laptops(sales):
    total_laptop = 0
    for sale in sales:
        if sale["product"] == "Laptop":
            total_laptop += 1

    print(total_laptop)

# sold_laptops(sales)


def average_price(sales):
    total_price = 0
    for sale in sales:
        total_price += sale["price"]

    print(total_price/len(sales))    


# average_price(sales)


text_arr = []
with open("sales.txt", 'r') as file:
    for line in file:
        # print(line.strip())
        result = int(line)
        text_arr.append(result)
  
     
print(text_arr)
total = 0
for number in text_arr:
    total += number
print(total)
print(total/len(text_arr))

