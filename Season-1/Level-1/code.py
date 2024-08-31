'''
Welcome to Secure Code Game Season-1/Level-1!

Follow the instructions below to get started:

1. tests.py is passing but code.py is vulnerable
2. Review the code. Can you spot the bug?
3. Fix the code but ensure that tests.py passes
4. Run hack.py and if passing then CONGRATS!
5. If stuck then read the hint
6. Compare your solution with solution.py
'''

from collections import namedtuple
import decimal

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

def validorder(order: Order):
    net = 0.0
    price = 0.0
    paid = 0.0

    for item in order.items:
        print(item)
        if item.type == 'payment':            
            paid += item.amount * item.quantity         
        elif item.type == 'product':
            if item.quantity > 1:
              return 'Total amount payable for an order exceeded'
            price += item.amount * item.quantity
        else:
            return "Invalid item type: %s" % item.type
 
    paid = float("{:.2f}".format(paid))
    price = float("{:.2f}".format(price))
    if paid == 0.0:
        return "Order ID: %s - Payment imbalance: $-%0.2f" % (order.id, price)
    
    net = paid - price
    print(price)
    print(paid)
    if net != 0:
        return "Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net)

    return "Order ID: %s - Full payment received!" % order.id