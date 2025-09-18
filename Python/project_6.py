temp = int(input("What is the temperature?: "))

if temp > 30:
    print("its HOT")
elif temp <= 30 and temp >= 15:
    print("its pleasant")
else:
    print("its COLD")