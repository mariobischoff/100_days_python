height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride")
    age = int(input("Whats is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif  age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    want_photos = input("Do you want a photo taken? Y or N. ")
    if want_photos == 'Y':
        #Add $3 to their bill
        bill += 3
    
    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller..")
