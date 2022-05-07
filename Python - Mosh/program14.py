"""
Project : Weight Converter. 
"""
"""
Weight conversion. You can enter the weight as either pounds or kilograms. 
If it is in pounds, it will convert and give your weight in kilograms.
If it is in kilograms, it will convert and give your weight in pounds.
And when giving "l" for pounds or "k" for kilograms, it is not case sensitive. 

Weight = 160
(L)bs or (K)g: l
You are 72.0 kilos.

My answer:

Weight = (input("Weight: "))
l = 0.45*int(Weight)
k = 2.2046*int(Weight)
print(input("(L)bs or (K)g: "))

if input is l:
    msg = f"You are {l} kilos"
    print(msg)
elif input is k:
    lsg = f"You are {k} pounds"
    print(lsg)
else:
    print("Invalid input.")

"""
weight = int(input("Weight: "))
unit = input('(L)bs or (K)kg: ')
if unit.upper() == "L":
    converted = weight*0.45
    print(f'You are {converted} kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} pounds')
