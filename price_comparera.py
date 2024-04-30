#starting text for the programe.
print ("Wecome to the Price Comparison Tool "
       "what do you want to compare.")


while True:
 instructions = input("Do you want the instructions? ")
 
 if instructions == "yes":
    print("In this programme for it to work you will have to put in all of the things "
          "you want to compare can not all be put in at once they have to be spaced out "
          "other wise it will not work properly basically. ")
    
 else:
  break



#user in put for the pirce checker.
while True:

    item1 = input("what is the first item you want to compare? ")
    price1 = int(input("what is the price: "))
    
    item2 = input("what is the second item you want to compare? ")
    price2 = int(input("what is the price: "))
    
    item3 = input("what is the third item you want to compare? ")
    price3 = int(input("what is the price: ")) 
   
    item4 = input("what is the forth item you want to compare? ") 
    price4 = int(input("what is the price: "))
    
    item5 = input("what it the fifth item you want to compare? ")    
    price5 = int(input("what is the price: "))
   
    item6 = input("what it the sixth item you want to compare? ")
    price6 = int(input("what is the price: "))
    
    break
# this code checks for the chepiest price.
all_prices = [ ]

all_items = [ ]

all_prices.append(price1,price2,price3,price4,price5,price6)

all_items.append(item1,item2,item3,item4,item5,item6)

def price(e):
  return e['lowest price']

all_prices = [ ]

all_prices.sort( reverse=True ,Key=price)

print(all_prices)

def price(e):
  return e['lowest price']

all_item = [ ]

all_item.sort( reverse=True ,Key=price)

print(all_prices)

print("this is the cheapest one")





