# Leap years

# normal year has 365 days
# but leap years have a extra day in February

# on every year that is evenly divisible by 4
# except every year that is envely divisible by 100
# unless the year is also evenly divisible by 400

# todos os anos múltiplos de 4 que também não são múltiplos de 100, 
# com exceção dos múltiplos de 400, deverão ser anos bissextos.

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")
