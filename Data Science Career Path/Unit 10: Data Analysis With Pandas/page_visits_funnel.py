import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head(3))
print(cart.head(3))
print(checkout.head(3))
print(purchase.head(3))

visits_cart = pd.merge(visits, cart, how='left')

print(len(visits_cart))

print(len(visits_cart[visits_cart.cart_time.isnull()]))

print(len(visits_cart[visits_cart.cart_time.isnull()]) / float(len(visits_cart)))

cart_checkout = pd.merge(cart, checkout, how='left')

print(len(cart_checkout[cart_checkout.checkout_time.isnull()]) /
float(len(cart_checkout)))

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head(5))

num_checkedout = len(all_data[all_data.checkout_time.notnull()])
num_purchased = len(all_data[all_data.purchase_time.notnull()])

print((num_checkedout - num_purchased) / float(num_checkedout))

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

#print(all_data.time_to_purchase)

#print(all_data.time_to_purchase.mean())