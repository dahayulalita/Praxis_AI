while True: # supaya berulang

    # The app shows welcome display
    print("Selamat Datang di Calculator")
    print(" ")

    # The app asks for user's option
    print("""" Enter your operation
        1. Multiple
        2. Divide
        3. Addition
        4. Subtitusion
        
        """)

    select = input("masukkan operasi pilihanmu ")

    num1 = input("insert the first number: ")
    num2 = input("insert the second number: ")

    #num1 * num2
    if select == "multiple": 
        print(int(num1) * int(num2)) #cara 1
            #multiple num1, num2
        
    elif select == "divide":
        print(int(num1) / int(num2)) 
            #division num1, num2

    elif select == "addition":
        print(int(num1) + int(num2)) 
            #addition num1, num2

    elif select == "subtitusion":
        print(int(num1) - int(num2)) 
            #substraction num1, num2

    else:
        print("incorrect")

# result = int(num1) * int(num2) #cara2
# print(result)