hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price = 0
total_price = [price for price in prices]
print(total_price)
Sum = sum(total_price)
average_price = Sum/len(total_price)
print("Average Haircut Price: "+str(average_price))

new_prices = [price-5 for price in prices]
print(new_prices)
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i]* last_week[i]
print(total_revenue)
average_daily_revenue = total_revenue/7
print(average_daily_revenue)

cuts_under_30 = [i for i in range(len(new_prices)-1) if new_prices[i]<30]
print(cuts_under_30)
