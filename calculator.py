#commmond line calcultor 

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divisable(a,b):
    if b == 0:
        return"!!error , divisable by 0 "
    return a/b

def main():
    while True:
        print("1. Addition (+): ")
        print("2. Subtraction (-): ")
        print("3.Multiplication (*): ")
        print("4.Divison (/): ")
        print("5. Exit ")

        try:
         choice = int(input("Enter your choice(1-5) : "))
        except:
          print("Invalid choice .. try again : ")
          continue

        if choice not in [1,2,3,4,5]:
         print("choose a valid option ")
         continue
        
        if choice == 5:
         print("Exiting calculator ...... visit us again!!!")
         break

        num1 = float(input("Enter your first number : "))
        num2 = float(input("Enter your secon number : "))
           
        if choice == 1:
           result = add(num1,num2)

        if choice == 2:
           result = sub(num1,num2)
        
        if choice == 3:
           result = multiply(num1,num2)
        
        if choice == 4:
          result = divisable(num1,num2)

        print(f"Result : {result}")
if __name__ == "__main__":
   main()