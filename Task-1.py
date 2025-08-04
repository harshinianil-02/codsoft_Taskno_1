try:
    num_1=int(input("Enter the first Number:"))
    num_2=int(input("Enter the second Number: "))
    print("1.Addition\n2.Substraction\n3.Multiplication\n4.Division")
    choice=int(input("Enter your choice of operation as 1,2,3,4:"))
    if(choice==1):
        print("Your Choice is Addition")
        result=num_1+num_2
        print(f"The Result is {result}")
    elif(choice==2):
        print("Your Choice is Substraction")
        if(num_1>num_2):
            result=num_1-num_2
            print(f"The Result is {result}")
        else:
            print("The result may be negative")
            result=num_1-num_2
            print(f"The Result is {result}")
    elif(choice==3):
        print("Your Choice is Multiplication ")
        result=num_1*num_2
        print(f"The Result is {result}")
    elif(choice==4):
        print("Your Choice is Division")
        if(num_2==0):
            print("Please enter the value greater than Zero")
        else:
            result=num_1/num_2
            print(f"The Result is {result}")
    else:
        print("Invalid Choice. Please Try Again!")
except ValueError:
    print("Invalid Input Please enter Valid number")



