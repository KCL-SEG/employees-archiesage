"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary = 0, hours = 0, 
    hourlyWage = 0, contracts = 0, contractCommision = 0, bonusCommision = 0):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.hourlyWage = hourlyWage
        self.contracts = contracts
        self.contractCommision = contractCommision
        self.bonusCommision = bonusCommision
    
    def get_pay(self):

        return self.salary + (self.hours * self.hourlyWage) + (self.contracts * self.contractCommision) + self.bonusCommision

    def __str__(self):

        if (self.salary != 0):

            if (self.bonusCommision != 0):
                return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.bonusCommision}. Their total pay is {self.get_pay()}."

            if (self.contractCommision != 0):
                return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.contractCommision}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

        else:
            
            if (self.bonusCommision != 0):
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.bonusCommision}. Their total pay is {self.get_pay()}."


            if (self.contractCommision != 0):
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour and receives a commission for {self.contracts} contract(s) at {self.contractCommision}/contract. Their total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.hourlyWage}/hour. Their total pay is {self.get_pay()}."

        return self.name

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary = 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hours=100, hourlyWage=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, contracts=4, contractCommision=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hours=150, hourlyWage=25, contracts=3, contractCommision=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, bonusCommision=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hours=120, hourlyWage=30, bonusCommision=600)
