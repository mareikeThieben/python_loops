print("Willkommen bei FizzBuzz")

zahl = int(input("Wähle eine Zahl zwischen 1 und 100: "))

for x in range (1, zahl + 1):
    if x % 3 == 0 and x % 5 == 0:
        print ("fizzbuzz")
    elif x % 3 == 0:
        print ("fizz")
    elif x % 5 == 0:
        print ("buzz")
    else:
        print(x)