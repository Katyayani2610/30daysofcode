# validate input keep asking the user for input until they enter a number  between 1 and 10# validate input
while True:
    number= int(input("enter the valid between 1 and 10"))
    if 1 <= number<= 10:
        print("thanks")
        break
    else :
        print ("invalid input")