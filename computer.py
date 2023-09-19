class Computer:

    # What attributes will it need?
    # This is the basic information of the computer, containing multiple attributes to the class.
    description: str = ""
    processor_type: str = ""
    hard_drive_capacity: int = 0
    memory: int = 0
    operating_system: str = ""
    year_made: int = 0
    price: int = 0

    # How will you set up your constructor?
    # Remember: in python, all constructors have the same name (__init__)
    def __init__(self, 
                 description: str, 
                 processor_type: str, 
                 hard_drive_capacity: int,
                 memory: int,
                 operating_system: str,
                 year_made: int,
                 price: float):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
    # What methods will you need?
     
    #print the features of computer
    def printComputer(self):
        print(self.description, self.processor_type, self.hard_drive_capacity, self.memory, self.operating_system, self.year_made, self.price)

    #check if the code can run  
def main(): 
    my_comp = Computer("Mac Pro (Late 2013)","3.5 GHc 6-Core Intel Xeon E5",1024, 64,"macOS Big Sur", 2013, 1500)
    print(my_comp.printComputer())

        
main()