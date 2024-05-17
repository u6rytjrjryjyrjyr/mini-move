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
   print("please ")


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
    item1 = input("what is the name of the {} item you want to compare? ".format(number))
    price1 = float(input("what is the price of the {} item you what to compare? ".format(number)))
    weight = float(input("what is the weight of the {} item you what to compare? ".format(number)))
    all_prices.append(price1)
    all_items.append(item1)
    all_weight.append(weight)
    price_item_weight.append(all_prices)
    price_item_weight.append(all_items)
    price_item_weight.append(all_weight)
    key = input(number)
    









price_item_weight.append([])  
price_item_weight.append(all_prices)
price_item_weight.append(all_items)
price_item_weight.append(all_weight)








# this code checks for the chepiest price.


price_number = min(smallest_number)

def small_number(smallest_number):
    price_number = smallest_number[0]
    for item in smallest_number:
      if price_number > item:
        price_number = item
      return price_number


print(price_item_weight)


print()



print("this is the cheapest one")





