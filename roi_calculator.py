class roicalculator():

    def __init__(self, monthlyincome=0, monthlyexpenses=0, totalinvestment=0):
        self.monthlyincome = monthlyincome
        self.monthlyexpenses = monthlyexpenses
        self.totalinvestment = totalinvestment
    
    def askMonthlyIncome(self):
        try:
            self.monthlyincome = int(input("How much do you collect for rent monthly"))
            print("You collect:", self.monthlyincome)
        except ValueError:
            print("Please input whole integers only...")  

    def askMonthlyExpenses(self):
        try:
            mortgage = int(input("How much do you pay for mortgage monthly?"))
            print("Your monthly mortage payment is:", mortgage)
        except ValueError:
            print("Please input whole integers only...")  
        else:
            try:
                tax = int(input("How much do you pay for tax monthly?"))
                print("Your monthly tax payment is:", tax)
            except ValueError:
                print("Please input whole integers only...")
            else:
                try:
                    insurance = int(input("How much do you pay for insurance monthly?"))
                    print("Your monthly insurance payment is:", insurance)
                except ValueError:
                    print("Please input whole integers only...")
                else:
                    try:
                        utilities = int(input("How much do you pay for utilities monthly?"))
                        print("Your monthly utility payment is:", utilities)
                    except ValueError:
                        print("Please input whole integers only...")
                    else:
                        try:
                            hoa = int(input("How much do you pay for HOA fees monthly?"))
                            print("Your monthly HOA payment is:", hoa)
                        except ValueError:
                            print("Please input whole integers only...")
                        else:
                            try:
                                propmanager = int(input("How much do you pay for a property manager monthly?"))
                                print("Your monthly property manager cost is:", propmanager)
                            except ValueError:
                                print("Please input whole integers only...")
                            else:
                                try:
                                    repairs = int(input("How much do you set aside for repairs monthly?"))
                                    print("Your monthly allocation for repairs is:", repairs)
                                except ValueError:
                                    print("Please input whole integers only...")
        self.monthlyexpenses = mortgage + tax + insurance + utilities + hoa + propmanager + repairs 

    def askInitialInvestment(self):
        try:
            downpayment = int(input("How much was the down payment after closing costs?"))
            print("Your downpayment cost was:", downpayment)
        except ValueError:
            print("Please input whole integers only...")
        else:
            try:
                rehab = int(input("How much was the rehab cost?"))
                print("Your rehab cost is:", rehab)
            except ValueError:
                print("Please input whole integers only...")
        self.totalinvestment = downpayment + rehab

    def cashOnCashROI(self):
        cashflow = 12 * (self.monthlyincome - self.monthlyexpenses)
        roi = cashflow / self.totalinvestment
        print("Your return on investment is:", roi*100,"%")

rentalProperty = roicalculator()

def run():
    while True:
        response = input("press (1) for income / (2) for expenses / (3) for initial investment / (4) ROI Calculation (5) to quit")
        
        if response == '5':
            print('Goodbye!')
            break 
        elif response == '4':
            if rentalProperty.totalinvestment == 0:
                print("Try again after inputting initial investment")
            elif rentalProperty.monthlyincome <= 0:
                print("Your income is less than or equal to zero, either input values in section 1 or it's a bad investment")
            elif rentalProperty.monthlyexpenses == 0:
                print("Please note that the ROI will be calculated without expenses added")
                rentalProperty.cashOnCashROI()                
            else:
                rentalProperty.cashOnCashROI()
        elif response == '3':
            rentalProperty.askInitialInvestment()
        elif response == '2':
            rentalProperty.askMonthlyExpenses()
        elif response == '1':
            rentalProperty.askMonthlyIncome()
        else:
            print('Try another command')
run()