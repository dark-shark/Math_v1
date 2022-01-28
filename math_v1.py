import colorama
from colorama import Fore
def pro() :
    print(Fore.RED + "hello welcome to this program")
    print(Fore.GREEN + "--------------------------------------------------")
    print(Fore.BLUE + "    ************* ")
    print(Fore.BLUE + "   *             *")
    print(Fore.BLUE + "  *   ********    *        ")
    print(Fore.BLUE + " *   *  *   *  *    *  ")
    print(Fore.BLUE + "*****   ****    ******      ")
    print(Fore.MAGENTA + "1- Info about the program")
    print(Fore.MAGENTA + "2- Calculator")
    print(Fore.MAGENTA + "3- Area and Perimeter and volume")
    print(Fore.MAGENTA + "4- Unit Convert")
    op = input("please enter your operation (1 to 4) : ")
    if op == "1":
        print(Fore.YELLOW + "Hello to all Users this program its for math works")
        print(Fore.YELLOW + "Its one open source program and its free for all")
        print(Fore.YELLOW + "Work with this program is very easy but if you have any question")
        print(Fore.YELLOW + "you can ask me in the telegram")
        print(Fore.YELLOW + "This program create and design by Alfa Programming Team")
        print(Fore.YELLOW + "Me and my team hope you enjoy this program")
        print(Fore.YELLOW + "* this program is offline and free")
        print(Fore.WHITE + "------------------------------------------------------------------------")
        ch2 = input("do you like try again (y , n) : ")
        if ch2 == "y":
            pro()
        else:
            ex2 = input("please enter one key to exit : ")    
    if op == "2":
        oper = input("please enter your operator (+ , - , * , / , ** , %) : ")
        if oper == "+":
            num1 = int(input("please enter number one : "))   
            num2 = int(input("please enter number two : "))
            num3 = num1 + num2
            print(num3)
        if oper == "-":
            num4 = int(input("please enter number one : "))    
            num5 = int(input("please enter number two : "))
            num6 = num4 - num5
            print(num6)  
        if oper == "*":
            num7 = int(input("please enter number one : "))    
            num8 = int(input("please enter number two : "))
            num9 = num7 * num8
            print(num9)  
        if oper == "/":
            num10 = int(input("please enter number one : "))    
            num11 = int(input("please enter number two : "))
            num12 = num10 / num11
            print(num12)   
        if oper == "**":
            num13 = int(input("please enter number one : "))
            num14 = int(input("please enter number two : ")) 
            num15 = num13 ** num14
            print(num15)
        if oper == "%":
            num16 = int(input("please enter number one : "))  
            num17 = int(input("please enter number two : ")) 
            num18 = num16 % num17
            print(num18)     
        ch = input("do you like try again (y , n) : ")
        if ch == "y":
            pro()
        else:
            ex = input("please enter one key to exit : ") 
    if op == "3":
        print(Fore.WHITE + "1- Square area")
        print(Fore.WHITE + "2- Square perimeter") 
        print(Fore.WHITE + "3- Rectangular area") 
        print(Fore.WHITE + "4- Rectangular perimeter")
        print(Fore.WHITE + "5- Triangle area")
        print(Fore.WHITE + "6- Triangle perimeter")
        print(Fore.WHITE + "7- Trapezoid area")
        print(Fore.WHITE + "8- Trapezoid perimeter")
        print(Fore.WHITE + "9- Lozenge area") 
        print(Fore.WHITE + "10- Lozenge perimeter")
        print(Fore.WHITE + "11- Parallel area")
        print(Fore.WHITE + "12- Parallel perimeter")
        print(Fore.WHITE + "13- Circle area")
        print(Fore.WHITE + "14- Circle perimeter")
        print(Fore.WHITE + "15- Sphere area")    
        print(Fore.WHITE + "16- Sphere volume") 
        print(Fore.WHITE + "17- Rectangular cube volume")
        print(Fore.WHITE + "18- Square cube volume")
        print(Fore.WHITE + "19- Pyramid volume")
        print(Fore.WHITE + "20- Regular pyramid area")
        print(Fore.WHITE + "21- Irregular pyramid area")
        print(Fore.WHITE + "22- Lateral area of ​​the cylinder")
        print(Fore.WHITE + "23- Total surface of the cylinder")
        print(Fore.WHITE + "24- Cone volume")
        print(Fore.WHITE + "25- Lateral area of ​​the cone")
        print(Fore.WHITE + "26- Total area of ​​the cone")
        print(Fore.WHITE + "27- Side area of ​​the charter")
        print(Fore.WHITE + "28- The total area of ​​the charter")
        ope = input("please enter one shape (1 to 28) : ")
        if ope == "1":
            print("Square area = one side * itself")
        if ope == "2":
            print("Square perimeter = one side * 4")  
        if ope == "3":
            print("Rectangular area = length * width") 
        if ope == "4":
            print("Rectangular perimeter = (length + width) * 2")  
        if ope == "5":
            print("Triangle area = (base * height) / 2") 
        if ope == "6":
            print("Triangle perimeter = sum of three sides")  
        if ope == "7":
            print("Trapezoid area = (large base + small base) * height / 2")   
        if ope == "8":
            print("Trapezoidal perimeter = sum of four sides")  
        if ope == "9":
            print("Lozenge area = (large diameter * small diameter) / 2")    
        if ope == "10":
            print("Lozenge perimeter = one side * 4")  
        if ope == "11":
            print("Parallel area = height rule")  
        if ope == "12":
            print("Perpendicular perimeter = sum of two consecutive sides * 2")  
        if ope == "13":
            print("Circle area = P number (3.14) * radius * radius")  
        if ope == "14":
            print("Circle perimeter = P number (3.14) * diameter") 
        if ope == "15":
            print("Sphere area = 4 * 3.14 radius to the power of two")  
        if ope == "16":
            print("Sphere volume = four thirds * 3.14 radius to the power of three")  
        if ope == "17":
            print("Rectangular cube volume = length * width * height")  
        if ope == "18":
            print("Square cube volume = base * height (edge ​​length * area of ​​one face)") 
        if ope == "19":
            print("Pyramid volume = area of ​​the base of the pyramid * height of the pyramid * one third") 
        if ope == "20":
            print("Regular pyramid area = mile length * perimeter * one-half + (base area)")   
        if ope == "21":
            print("Irregular pyramid area = (lateral area) + (base area)")  
        if ope == "22":
            print("Lateral area of ​​the cylinder = circumference of the base * height volume of the cylinder = area of ​​the base * height") 
        if ope == "23":
            print("Total surface of the cylinder = level of two bases + lateral area (total area of ​​two bases + height * around the base)")  
        if ope == "24":
            print("Cone volume = base area * one third * height")  
        if ope == "25":
            print("Lateral area of ​​the cone = P number (3.14) * radius * side length") 
        if ope == "26":
            print("Total area of ​​the cone = (radius + side length) * radius * number (3.14)")  
        if ope == "27":
            print("Side area of ​​the charter = the total area of ​​the side surfaces")   
        if ope == "28":
            print("Total area of ​​the charter = total area of ​​two rules + total area of ​​lateral surfaces")
        ch3 = input("do you like try again (y , n) : ")
        if ch3 == "y":
            pro()
        else:
            ex3 = input("please enter one key to exit : ")
    if op == "4":
        print(Fore.CYAN + "This part coming soon in the version 2")
        ch5 = input("do you like try again (y , n) : ")
        if ch5 == "y":
            pro()
        else:
            ex5 = input("please enter one key to exit : ")    
    else:
        ch4 = input("do you like try again (y , n) : ")
        if ch4 == "y":
            pro()
        else:
            ex4 = input("please enter one key to exit : ")                                                                                  
pro()                          