inType = str(input("Enter desired output [fahrenheit or celsius]: "))
val = float(input("Enter the value: "))

if (inType == "fahrenheit"):
    out = (val*1.8)+32
    print(f"The Fahrenheit of {val}*C is {out}*F")
elif (inType == "celsius"):
    out = (val-32)/1.8
    print(f"The Celsius of {val}*F is {out}*C")
