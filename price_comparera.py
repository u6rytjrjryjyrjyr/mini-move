#starting text for the programe.
print ("Wecome to the Price Comparison Tool "
       "what do you want to compare.")


while True:
 instructions = input("Do you want the instructions? ")
 
 if instructions == "yes":
    print("In this programme for it to work you will have to put in all of the things "
          "you want to compare can not all be put in at once they have to be spaced out "
          "other wise it will not work properly basically. ")
    break
 elif instructions == "no":
    break

else: 
   print()


#user in put for the pirce checker.
 
number = int(input("how many number of items do you what to compare: "))

all_items = []

all_prices = []

for i in range(number):

    
    item1 = input("what is the name of the item you want to compare? ")
    price1 = int(input("what is the price of the item you what to compare? "))
    all_prices.append(price1)
    all_items.append(item1)
    


    
# this code checks for the chepiest price.


smallest_number = min(all_prices)

def smallest_number(all_prices):
    smallest_number = all_prices[0]
    for item in all_prices:
      if smallest_number > item:
        smallest_number = item
      return smallest_number

print(smallest_number)



print("this is the cheapest one")





