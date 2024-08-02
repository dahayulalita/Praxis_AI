while True: # supaya berulang

    # 1. The app shows welcome display
    print("Welcome")
    print(" ")

    # 2. The app asks for user's option
    print("""" Enter your operation
        1. Multiple
        2. Divide
        3. Addition
        4. Subtitusion
        
        """)
    
    # 3. Enter your answer
    select = input("masukkan operasi pilihanmu ")
    if select not in ["multiple", "divide", "addition", "subtitusion"]:
        print("Error")
        continue 

    '''
    pernyataan continue
    kondisi keluar dari loop untuk diuji kembali
    '''

    # 4. The app ask for the numbers
    num1 = (input("insert the first number: "))
    num2 = (input("insert the second number: "))
    
    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        print("Error")
        continue  

    # melakukan operasi yang diminta
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

    # 6. The app will show the result
    
    # 7. The app ask want to exit
    select = input("want to exit?")

    # 8. The app ask for the answer
    if select == "yes":
        print("Bye!!")
        break

    else:
        print("next")