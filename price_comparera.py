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
 else:
  break



#user in put for the pirce checker.
while True:
  all_prices = [ ]
  item1 = input("what is the first item and price you want to compare? ")
  item1 = list(map(int, input().split()))

  all_prices.sort()
   
  item2 = input("what is the second item and price you want to compare? ")
  item2 = list(map(int, input().split()))

  all_prices.sort() 
    
  item3 = input("what is the third item and price you want to compare? ")
  item3 = list(map(int, input().split()))

  all_prices.sort()
   
  item4 = input("what is the forth item and price you want to compare? ") 
  item4 = list(map(int, input().split()))

  all_prices.sort()
    
  item5 = input("what it the fifth item and price you want to compare? ")    
  item5 = list(map(int, input().split()))

  all_prices.sort()
   
  item6 = input("what it the sixth item and price you want to compare? ")
  item6 = list(map(int, input().split()))

  all_prices.sort()
    
  break
# this code checks for the chepiest price.


print(all_prices)

print("this is the cheapest one")





