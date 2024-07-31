num1 = input("insert the first number: ")
num2 = input("insert the second number: ")

select = input("masukkan operasi pilihanmu ")

#num1 * num2
if select == "mul": 
    print(int(num1) * int(num2)) #cara 1
          #multiply num1, num2
    
elif select == "div":
    print(int(num1) / int(num2)) 
          #division num1, num2

elif select == "add":
    print(int(num1) + int(num2)) 
          #addition num1, num2

elif select == "sub":
    print(int(num1) - int(num2)) 
          #substraction num1, num2

else:
    print("tak blok kon")

# result = int(num1) * int(num2) #cara2
# print(result)