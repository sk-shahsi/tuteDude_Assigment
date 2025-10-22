"""
Amount = P(1+R/100) ** 100
P = Principal amount
R = rate of interest
T = time of interest

"""
principle = float(input("Enter principle Amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time duration: "))
#amount = principle *(1 + rate/100)**time
amount=principle*pow((1+rate/100),time)
print("Amount is : ",round(amount))
ci=amount-principle
print("Compound Interest is : ",round(ci))