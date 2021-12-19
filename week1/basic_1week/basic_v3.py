stock_dict = {"키움증권": 5000, "카카오": 3000, "네이버": 2000}
stock_num = {"키움증권": 0, "카카오": 0, "네이버": 0}
sum_price = 0
my_wallet = 111000
buy_stop = True
add_stock = True

for key, price in stock_dict.items():
    sum_price = sum_price + price

while buy_stop:
    for key, price in stock_dict.items():
        if my_wallet >= price:
            my_wallet = my_wallet - price
            stock_num.update({key: stock_num.get(key)+1})
        else:
            buy_stop = False
            break

while add_stock:
    stock_dict.update({"키움증권": stock_dict.get("키움증권")+1000})

    if stock_dict.get("키움증권") >= 10000:
        stock_dict.update({"이베스트증권": 5000})
        break

print("총합 : %d" % sum_price)

print(stock_dict)
print(stock_num)
print(my_wallet)