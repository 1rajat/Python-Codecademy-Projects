"""Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren’t charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00

Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00

Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.
""""


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
