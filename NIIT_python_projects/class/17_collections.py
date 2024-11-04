cart = [
    {'item': 'apple', 'price': 100, 'qty': 7},
    {'item': 'ball', 'price': 800, 'qty': 1},
    {'item': 'cat', 'price': 19100, 'qty': 1}
]
print("Total Orders", len(cart))
total = 0
items = 0
for order in cart:
    p = order['price']
    q = order['qty']
    i = order['item']
    print(i, "is", p*q)
    total += p
    items += q
    vat = 7.5
    x = ((total * vat)/100) + total
    z = ((x * 10)/100)
    z = x-z
    print('Total Price', total)
    print('Total Items', items)
    print('Gross Price', "is", x)
    print('Net Price', "is", z)
