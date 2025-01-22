try:
    num_1 = int(input("Enter First Number: "))
    num_2 = int(input("Enter Second Number: "))

    print("Type the calculation method to perform: \n",
        "1. Add\n",
        "2. Subtract\n",
        "3. Multiply\n",
        "4. Divide\n")
    
    cal = input().strip().lower()

    if cal == "add":
        ans = num_1 + num_2
    elif cal == "subtract":
        ans = num_1 - num_2
    elif cal == "multiply":
        ans = num_1 * num_2
    elif cal == "divide":
        if num_2 == 0:
            print("Error! Can't Divide By Zero.")
            ans = None
        else:
            ans = num_1 / num_2
    else:
        print("Invalid Operation!")
        ans = None
    
    if ans is not None:
        print(f"The Answer is: {ans}")
except ValueError:
    print("Invalid Input! Please Enter Valid Number!")