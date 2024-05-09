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
    all_prices.insert(1, price1)
    all_items.append(item1)
    break


    
# this code checks for the chepiest price.

all_prices = []

print (min(all_prices))


print(all_prices)



print("this is the cheapest one")





