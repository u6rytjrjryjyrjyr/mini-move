# """Price calculator of calculating price and weight."""
# Coder: Max Allison.
# V 03.5.

# Starting text for the programe.
print("Wecome to the Price Comparison Tool "
      "what do you want to compare.")

# The instructions of the uses of the code.
while True:
 instructions = input("Do you want the instructions? yes or no ").lower()
 if instructions == "yes":
    print("In this programme for it to work "
          "you will have to put in all of the things "
          "you want to compare can not all be put in"
          " at once they have to be spaced out "
          "other wise it will not work properly basically")
    break
 elif instructions == "no":
   break

 else:
   print("please use yes or no please. ")
      
# User input for how many items the user want to compare.

number = int(input("how many number of items"
                   " do you what to compare: "))
# Lists for information and input to be stored.
price_item_weight = []
all_items = []
all_prices = []
all_things = []
all_weight = []
smallest_number = []
weight_price = []
# For in loop for looping the code in side.
# And the code put all of the user inputs in to the arrays.
for i in range(number):
    item1 = input("what is the name of the {} item you"
                  " want to compare? ".format(i))
    price1 = float(input("what is the price of the {} item you"
                         " what to compare? ".format(i)))
    weight = float(input("what is the weight of the {} item "
                         "you what to compare? ".format(i)))
    all_prices.append(price1)
    all_items.append(item1)
    all_weight.append(weight)
    price_item_weight.append(all_prices)
    price_item_weight.append(all_items)
    price_item_weight.append(all_weight)

# Calaulates price / weight
price_per_weight = [price / weight for price, weight
                    in zip(all_prices, all_weight)]
# Lists for storing list that store user inputs
price_item_weight.append([])
price_item_weight.append(all_prices)
price_item_weight.append(all_items)
price_item_weight.append(all_weight)
# gets the smallest item group into the cheapest_things list

cheapest_things = price_per_weight.index(min(price_per_weight))

# This code tells the cheapest price.
# And it also has items and weight and price per weight.
print(f"Item: {all_items[cheapest_things]}")
print(f"Price: {all_prices[cheapest_things]}")
print(f"Weight: {all_weight[cheapest_things]}")
print(f"Price per weight: {price_per_weight[cheapest_things]:.2f}")
