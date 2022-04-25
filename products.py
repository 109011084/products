products = [] #大清單
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    p = [] #小清單
    p = [name, price]
       #p.append(name)
       #p.append(price) 上面那行取代這兩行
    products.append(p)
print(products)