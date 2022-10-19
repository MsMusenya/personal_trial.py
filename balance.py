#balance.py
#A program to calculate the value of sum of money in kenyan shillings

def main():
    print("Balance sheet")
    print()
    print("Please enter the count of each note type.")
    brown = int(input("Thousands: "))
    green = int(input("Five hundreds: "))
    blue = int(input("Two hundreds: "))
    purple = int(input("Hundreds: "))
    pink = int(input("Fifty bobs: "))
    total = brown* 1000.0 + green* 500.0 + blue* 200.0 + purple*100.0 + pink*50.0
    print()
    print("The total sum of your money is",total)
    #a continuation trying to get the change after deductions
    print("Please enter your deductions below: ")
    
    shopping = int(input("Shopping:Ksh "))
    rent = int(input("Rent:Ksh "))
    water = int(input("Water:Ksh "))
    electricity = int(input("Electricity:Ksh "))
    utility = int(input("Utility:Ksh "))
    wifi = int(input("Wi-Fi:Ksh "))
    fuel = int(input("Fuel:Ksh "))
    medical = int(input("Medical:Ksh "))

    change = total - shopping - rent - water - electricity - utility - wifi - fuel - medical
    print()
    print("Your change after deductions is: Ksh",change)

main()
  
 



    
    
                      
    
