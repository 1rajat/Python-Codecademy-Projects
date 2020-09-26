def ground_shipping(weight):
  if weight<=2:
    price_per_pound = 1.50
  elif weight<=6:
    price_per_pound = 3.00
  elif weight<=10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20+(price_per_pound*weight)

Cost_premium_ground_shipping = 125.00
def drone_shipping(weight):
  if weight<=2:
    price_per_pound = 4.50
  elif weight<=6:
    price_per_pound = 9.00
  elif weight<=10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return price_per_pound*weight
 
ground_shipping = ground_shipping(4.8)
drone_shipping = drone_shipping(4.8)

if ground_shipping < drone_shipping:
  print("ground shipping is cheaper")
else:
  print("drone shipping is cheaper")