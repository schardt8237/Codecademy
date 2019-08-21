#Cost of premium shipping
prem_ship_cost = 125.0

#Calculates cost of ground shipping given package weight
def ground_shipping(weight):
  # Base cost of ground shipping
  flat_charge = 20.0
  
  if weight <= 2:
    return weight * 1.5 + flat_charge
  elif weight <= 6:
    return weight * 3.0 + flat_charge
  elif weight <= 10:
    return weight * 4.0 + flat_charge
  else:
    return weight * 4.75 + flat_charge
  
#Calculates cost of drone shipping given package weight
def drone_shipping(weight):
  if weight <= 2:
    return weight * 4.5
  elif weight <= 6:
    return weight * 9.0
  elif weight <= 10:
    return weight * 12.0
  else:
    return weight * 14.25

#Determines the cheapest method of shipping
def cheapest_shipping(weight):
  ground_cost = ground_shipping(weight)
  drone_cost = drone_shipping(weight)
  
  if ground_cost < prem_ship_cost and ground_cost < drone_cost:
    return "You should ship using ground shipping, it will cost $" + str(ground_cost)
  elif drone_cost < prem_ship_cost:
    return "You should ship using drone shipping, it will cost $" + str(drone_cost)
  else:
    return "You should ship using premium shipping, it will cost $" + str(prem_ship_cost)

print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))
print(cheapest_shipping(3))