# Problem 1: BankAccount:
class BankAccount:
    def __init__(self, accountnumber, balance):
        self.accountnumber = accountnumber
        self.balance = balance

    # balance is encapsulated here

    # Deopsiting amount and calculating balance
    def Deposit(self, amount):
        self.balance += amount
        print(f"\n Total Balance: Balance amount in account {self.accountnumber} is {self.balance}")

    # Calculating balance once amount is withdrawl
    def Withdrawl(self, withdrawlamount):
        MinimumAmountRequired = 500
        if withdrawlamount < self.balance:
            self.balance -= withdrawlamount
            print(f"\n BalanceAfterWithdrawl: Your remaining balance is {self.balance}")

        elif withdrawlamount >= self.balance:
            print("\n You are making process to take more than the minium amount.")


# Subclass 1:
class SavingsAccount(BankAccount):
    def InterestCalculate(self, time):
        interestrate = 0.05

        # calculating interest
        Interestamount = self.balance * interestrate * time
        self.balance += Interestamount
        print(f"\n Calculated interest: interest amount is {Interestamount} and your current balance is {self.balance}")


# Subclass 2:
class CurrentAccount(BankAccount):
    def MinimumBalance(self, amount):
        AmountRequired = 500
        self.balance += amount

        if self.balance < AmountRequired:
            requiredamount = AmountRequired - self.balance
            print(f"\n Your balance is not meet the minimum balance requirement. Please deposit {requiredamount} more.")

        else:
            print("\n Thank you for your time")


# objects created for each class
TotalBalance = BankAccount(123412341234, 500)
TotalBalance.Deposit(500)
TotalBalance.Withdrawl(700)
Interest = SavingsAccount(123412341234, 1000)
Interest.InterestCalculate(1)
MinBalance = CurrentAccount(123412341234, 200)
MinBalance.MinimumBalance(200)


#-------------------------------------------------------------------------------------------------------------------------


#Problem 2: Employee Management
#Parent Class
class Employee:
    def __init__(self, name, salary, YOE):
        self.name = name
        self.salary = salary
        self.YOE = YOE

    def calculate_salary(self):  # YOE(Years of Experience)
        Incrementpercentage = 0.10
        Incrementpercentage1 = 0.15
        if self.YOE < 5:
            print(f"\n We will offer {self.salary}rs")

        elif self.YOE >= 5 and self.YOE <= 10:  # checking employee experience to decide the percentage
            self.salary += self.salary * Incrementpercentage  # calculating salary and adding to total salary
            print(f"\n {self.name}, Your revised salary is {self.salary}")

        elif self.YOE > 10:
            self.salary += self.salary * Incrementpercentage1
            print(f"\n {self.name}, Your revised salary is {self.salary}")


# Subclass 1: Calculating salary based on the workingdays, and giving 50rs per day as bonus
class RegularEmployee(Employee):
    def __init__(self, name, salary, YOE, Workingdays):
        super().__init__(name, salary, YOE)
        self.Workingdays = Workingdays

    def calculate_salary(self):
        self.salary += self.Workingdays * 50
        print(f"\n {self.name}, Your salary with bonus for the year is {self.salary}")


# Subclass 2: Calculating salary based on the Numberofcourse they completed to meet the goal and based on that percentage will be calculated
class ContractEmployee(Employee):
    def __init__(self, name, salary, YOE, NumberOfCourses):
        super().__init__(name, salary, YOE)
        self.NumberOfCourses = NumberOfCourses

    def calculate_salary(self):
        Increment = 0.10
        if self.NumberOfCourses <= 5:
            print(f"\n {self.name}, Sorry! You are not eligible for the increment")

        elif self.NumberOfCourses > 5:
            self.salary += self.salary * Increment
            print(f"\n {self.name}, Your revised salary is {self.salary}")


# Subclass 3: Calculating salary based on the number of clients he added to the company and based on that percentage will be calculated
class Manager(Employee):
    def __init__(self, name, salary, YOE, NumberofClients):
        super().__init__(name, salary, YOE)
        self.NumberofClients = NumberofClients

    def calculate_salary(self):
        if self.NumberofClients > 20:
            self.salary += self.salary * 0.3
            print(f"\n {self.name}, Congratulation! this is big achievement. Here is your increment {self.salary}")

        else:
            self.salary += self.salary * 0.15
            print(f"\n {self.name}, Please focus on your goal, your increment is {self.salary}")


#Objects created for each class
EmpSal = Employee("Lithu", 1000000, 11)
RegEmpSal = RegularEmployee("Madhu", 1200000, 5, 350)
ContEmpSal = ContractEmployee("Malathi", 1000000, 7, 4)
ManSal = Manager("Aaruth", 2000000, 15, 7)

TotalSal = [EmpSal, RegEmpSal, ContEmpSal, ManSal]
for i in TotalSal:
    i.calculate_salary()


#------------------------------------------------------------------------------------------------------------------------

#Problem 3: Vehicle Rental
#Parent Class
class Vehicle:
    def __init__(self, Name, Model, Rental_Rate, Hours):
        self.Model = Model
        self.Rental_Rate = Rental_Rate
        self.Hours = Hours
        self.Name = Name

    # Calculating Rental rate for vehicle based on Hours used

    def Calculate_Rental(self):
        if self.Hours <= 5:
            rate = self.Hours * 100
            print(f"\n Hi {self.Name},you used our vehicle for {self.Hours} hours and Rent is {rate}")

        if self.Hours > 5:
            rate = self.Hours * 150
            print(f"\n Hi {self.Name},you used our vehicle for {self.Hours} hours and Rent is {rate}")


# Subclass 1: Calculating Rental rate for Car based on KM Reached
class Car(Vehicle):
    def __init__(self, Name, Model, Rental_Rate, Hours, KM):

        # Used already defined variables from parent class
        super().__init__(Name, Model, Rental_Rate, Hours)
        self.KM = KM

        # Calculating rent based on the car type

    def Calculate_Rental(self):
        if self.Model == "Battery":
            self.Rental_Rate = 30
            amount = self.Rental_Rate * self.KM
            print(f"\n Hi {self.Name},you have used our {self.Model} car for {self.KM} KM and rent is {amount}")


        elif self.Model == "Petrol":
            self.Rental_Rate = 60
            amount = self.Rental_Rate * self.KM
            print(f"\n Hi {self.Name},you have used our {self.Model} car for {self.KM} KM and rent is {amount}")


        elif self.Model == "Diesel":
            self.Rental_Rate = 50
            amount = self.Rental_Rate * self.KM
            print(f"\n Hi {self.Name},you have used our {self.Model} car for {self.KM} KM and rent is {amount}")


# Subclass 2: Calculating Rental rate based on how many days bike has been used

class Bike(Vehicle):
    def __init__(self, Name, Model, Rental_Rate, Hours, Days):
        super().__init__(Name, Model, Rental_Rate, Hours)
        self.Days = Days

    def Calculate_Rental(self):

        if self.Model == "Electric":
            RentRate = self.Days * 100
            print(f"\n Hi {self.Name},you have used our {self.Model} Bike for {self.Days} and rent is {RentRate}")

        else:
            RentRate = self.Days * 150
            print(f"\n Hi {self.Name},you have used our {self.Model} Bike for {self.Days} days and rent is {RentRate}")


# Subclass 3: Calculating Rental Rate based on Weight of the load

class Truck(Vehicle):
    def __init__(self, Name, Model, Rental_Rate, Hours, TON):
        super().__init__(Name, Model, Rental_Rate, Hours)
        self.TON = TON

    def Calculate_Rental(self):
        if self.TON < 1.5:
            Truckrate = self.TON * 2000
            print(f"\n Hi {self.Name},Rent for your {self.TON} load is {Truckrate}")

        if self.TON > 1.5:
            Truckrate = self.TON * 4000
            print(f"\n Hi {self.Name},Rent for your {self.TON} load is {Truckrate}")


# Object created for each class

VehiRent = Vehicle("Lithu", 0, 0, 10)
CarRent = Car("Madhu", "Petrol", 0, 0, 10)
BikeRent = Bike("Malathi", "Suzuki", 0, 0, 10)
TruckRent = Truck("Aaruth", "Lorry", 0, 0, 1.6)

TotalSal = [VehiRent, CarRent, BikeRent, TruckRent]
for i in TotalSal:
    i.Calculate_Rental()




























