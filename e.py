
def yes_no(question):

    while True:
        response = input(question).lower()
    
        if response == "yes" or response == "y":
            return "yes"
        

        elif response == "no" or response == "n":
            return "no"
        
        else:
             print("plesse enter yes or no")
MAX_TICKETS = 3
tickets_sold = 0
while tickets_sold < MAX_TICKETS:
    name = input("please enter your name or 'xxx' to quit: ")

    if name == 'xxx':
        break

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print('Congratulations you have sold all the all the tickets')
else:
    print('you have sold {} ticket/s. There is {} ticket\s '
          'remaining'.format(tickets_sold, MAX_TICKETS - tickets_sold))
    
while True:
    want_instructions = yes_no("Do you want to read the instruction? ")

    if want_instructions == "yes":
        print('instuctions go here') 

            
    print("we are done")
    print()




