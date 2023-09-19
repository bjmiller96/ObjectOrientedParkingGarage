class ParkingGarage():
    """
        Simple parking garage class for taking a ticket, paying for parking, and leaving the garage
    """

    def __init__(self):
        self.tickets = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.parkingSpaces = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.currentTicket = {'paid': False}
        self.hasTicket = False

    def takeTicket(self):
        if self.hasTicket != True:
            if len(self.tickets) > 0 and len(self.parkingSpaces) > 0:
                self.tickets.pop()
                self.parkingSpaces.pop()
                print(f"\nHere is your ticket. Please find any open parking spot from the remaining {len(self.parkingSpaces)} parking spaces.")
                self.hasTicket = True
            else:
                print("\nSorry but there are no more available parking spots!")
        else:
            print("\nSorry you're only allowed to have one parking ticket at a time.")
            
    def payForParking(self):
        if self.hasTicket == True:
            while True:
                pay_ticket = input("\nPlease provide the dollar amount you owe for your ticket. $")
                if pay_ticket != '':
                    self.currentTicket['paid'] = True
                    print("\nYour ticket has been paid. You have 15 minutes to leave.")
                    break
                else:
                    print("\nThe ticket amount cannot be left blank. Please provide the correct amount.")
                    continue
        else:
            print("\nYou don't have a parking ticket to pay for yet.")
    
    def leaveGarage(self):
        if self.hasTicket == True:
            if self.currentTicket['paid'] == True:
                self.tickets.append(1)
                self.parkingSpaces.append(1)
                print("\nThank you. Have a nice day.")
            else:
                print("\nPlease pay for your parking ticket first.")
        else:
            print("\nOkay. Have a great rest of your day. Bye.")
            


parkCar = ParkingGarage()


def parking_car():
    print("Welcome to the Parking Garage!")

    while True:
        print("\nWould you like to take a parking ticket, pay for your parking spot, or leave the garage?")
        user_input = input("Please use one of the following keywords: Ticket, Pay, or Leave? ")

        if user_input.lower() == 'ticket': 
            parkCar.takeTicket()
            
        elif user_input.lower() == 'pay':
            parkCar.payForParking()
            
        elif user_input.lower() == 'leave':
            if parkCar.hasTicket == True:
                if parkCar.currentTicket['paid'] == True:
                    parkCar.leaveGarage()
                    break
                else:
                    parkCar.leaveGarage()
            else:
                parkCar.leaveGarage()
                break
                
        else:
            print("Invalid Input. Please try again.")


parking_car()