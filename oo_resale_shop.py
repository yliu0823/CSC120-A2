from computer import *
class ResaleShop:
    # What attributes will it need?
    inventory : list
    itemID: int = 0
    price: int = 0
    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self):
        self.inventory = []

    # add computer into inventory
    def buy(self, newComputer:Computer):
        self.inventory.append(newComputer)

    # check if computer is in inventory
    # remove computer from inventory
    def sell(self, oldComputer:Computer):
        if oldComputer in self.inventory:
            self.inventory.remove(oldComputer)
            print(oldComputer, "is sold")
        else:
            print(oldComputer, "is not found")

    # check computer in the inventory
    # update price and os based on year made
    def refurbishing(self, computer:Computer):
        if computer in self.inventory:# locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price= 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000

        else:
            print(computer,"Item not found. Please select another item to refurbish.")

    def update_price(self, computer:Computer, new_price):
        if computer in self.inventory: #check if it is in inventory
            computer.price = new_price  #update old price to new price
        else:
            print("Item", computer, "not found. Cannot update price.")

    def update_os(self, computer:Computer, new_os):
        if computer in self.inventory: #check if it is in inventory
            computer.os = new_os #update old os to new os
        else:
            print("Item", computer, "not found. Cannot update operating system")

    def printInventory(self):
        for computer in self.inventory:
            computer.printComputer() #print computer from Computer class
        
            
def main(): #check if the code can run
    myStore=ResaleShop()
    c1=Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    c2=Computer("Mac (2014)","4.0 GHc Intel Xeon E5", 512, 32, "IOS", 2014, 2000)
    myStore.buy(c1)
    myStore.update_price(c1,2000)
    myStore.buy(c2)

    myStore.sell(c1)  
    myStore.sell(c2)
    myStore.update_os(c1,"android")
    
    print(c1.operating_system)

    myStore.refurbishing(c1)
    print(c1.price)
    myStore.printInventory()

main()
