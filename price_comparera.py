#starting text for the programe.
print ("Wecome to the Price Comparison Tool "
       "what do you want to compare.")


while True:
 instructions = input("Do you want the instructions? ")
 if instructions == "yes":
    print("In this programme for it to work you will have to put in all of the things "
          "you want to compare can not all be put in at once they have to be spaced out "
          "other wise it will not work properly basically and number the inputs them. ")
    break
 elif instructions == "no":
    break

else: 
   print("please use yes or no please. ")


#user in put for the pirce checker.
 
number = int(input("how many number of items do you what to compare: "))
price_item_weight = []
all_items = []
all_prices = []
all_things = []
all_weight = []
smallest_number = []
weight_price = []

for i in range(number): 
    item1 = input("what is the name of the {} item you want to compare? ".format(i))
    price1 = float(input("what is the price of the {} item you what to compare? ".format(i)))
    weight = float(input("what is the weight of the {} item you what to compare? ".format(i)))
    all_prices.append(price1)
    all_items.append(item1)
    all_weight.append(weight)
    price_item_weight.append(all_prices)
    price_item_weight.append(all_items)
    price_item_weight.append(all_weight)
    
    


# calaulates price / weight
price_per_weight = [price / weight for price, weight in zip(all_prices, all_weight)]





price_item_weight.append([])  
price_item_weight.append(all_prices)
price_item_weight.append(all_items)
price_item_weight.append(all_weight)

cheapest_things = price_per_weight.index(min(price_per_weight))










# this code tells the cheapest price 

print(f"Item: {all_items[cheapest_things]}")
print(f"Price: {all_prices[cheapest_things]}")
print(f"Weight: {all_weight[cheapest_things]}")
print(f"Price per weight: {price_per_weight[cheapest_things]:.2f}")



