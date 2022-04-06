import colorama
from colorama import Fore
import math
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
    print(Fore.MAGENTA + "4- Unit Convert (internet services)")
    print(Fore.MAGENTA + "5- P number")
    print(Fore.MAGENTA + "6- get the Absolute value")
    print(Fore.MAGENTA + "7- get the square root")
    print(Fore.MAGENTA + "8- get the two number power")
    print(Fore.MAGENTA + "9- get the Trigonometry")
    print(Fore.MAGENTA + "10- convert radians to degrees")
    print(Fore.MAGENTA + "11- convert degrees to radians")
    print(Fore.MAGENTA + "12- get the union")
    print(Fore.MAGENTA + "13- get the difference")
    print(Fore.MAGENTA + "14- get the intersection")
    op = input("please enter your operation (1 to 14) : ")
    if op == "1":
        print(Fore.YELLOW + "Hello to all Users this program its for math works")
        print(Fore.YELLOW + "Its one open source program and its free for all")
        print(Fore.YELLOW + "Work with this program is very easy but if you have any question")
        print(Fore.YELLOW + "you can ask me in the telegram")
        print(Fore.YELLOW + "The version 2 coming soon")
        print(Fore.YELLOW + "You can use another math tools")
        print(Fore.YELLOW + "Math tools its like Coordinates , The geometry , ...")
        print(Fore.YELLOW + "All of this tools add in the version 2")
        print(Fore.YELLOW + "The version 2 have very easy installer")
        print(Fore.YELLOW + "The version 2 coming here")
        print(Fore.YELLOW + "This program create and design by Alfa Programming Team")
        print(Fore.YELLOW + "Me and my team hope you enjoy this program")
        print(Fore.YELLOW + "* this program is offline and free")
        print(Fore.WHITE + "------------------------------------------------------------------------")
        ch2 = input("do you like try again (y , n) : ")
        if ch2 == "y":
            pro()
        else:
            ex2 = input("please enter one key to exit : ")    
    elif op == "2":
        oper = input("please enter your operator (+ , - , * , / , ** , %) : ")
        if oper == "+":
            num1 = int(input("please enter number one : "))   
            num2 = int(input("please enter number two : "))
            num3 = num1 + num2
            print(num3)
        elif oper == "-":
            num4 = int(input("please enter number one : "))    
            num5 = int(input("please enter number two : "))
            num6 = num4 - num5
            print(num6)  
        elif oper == "*":
            num7 = int(input("please enter number one : "))    
            num8 = int(input("please enter number two : "))
            num9 = num7 * num8
            print(num9)  
        elif oper == "/":
            num10 = int(input("please enter number one : "))    
            num11 = int(input("please enter number two : "))
            num12 = num10 / num11
            print(num12)   
        elif oper == "**":
            num13 = int(input("please enter number one : "))
            num14 = int(input("please enter number two : ")) 
            num15 = num13 ** num14
            print(num15)
        elif oper == "%":
            num16 = int(input("please enter number one : "))  
            num17 = int(input("please enter number two : ")) 
            num18 = num16 % num17
            print(num18)     
        ch = input("do you like try again (y , n) : ")
        if ch == "y":
            pro()
        else:
            ex = input("please enter one key to exit : ") 
    elif op == "3":
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
            n1 = int(input("please enter one side : "))
            n2 = int(input("please enter itself : "))
            n3 = n1 * n2
            print(n3)
        elif ope == "2":
            print("Square perimeter = one side * 4")
            n4 = int(input("please enter one side : "))
            n5 = n4 * 4
            print(n5)  
        elif ope == "3":
            print("Rectangular area = length * width") 
            n6 = int(input("please enter lengh : "))
            n7 = int(input("please enter width : "))
            n8 = n6 * n7
            print(n8)
        elif ope == "4":
            print("Rectangular perimeter = (length + width) * 2")
            n9 = int(input("please enter length : "))  
            n10 = int(input("please enter width : ")) 
            n11 = (n9 + n10) * 2
            print(n11)
        elif ope == "5":
            print("Triangle area = (base * height) / 2")
            n12 = int(input("please enter base : "))  
            n13 = int(input("please enter height : ")) 
            n14 = (n12 * n13) / 2
            print(n14)
        elif ope == "6":
            print("Triangle perimeter = sum of three sides") 
            n15 = int(input("please enter side one : ")) 
            n16 = int(input("please enter side two : ")) 
            n17 = int(input("please enter side three : ")) 
            n18 = n15 + n16 + n17 
            print(n18)
        elif ope == "7":
            print("Trapezoid area = (large base + small base) * height / 2")
            n19 = int(input("please enter large base : "))
            n20 = int(input("please enter small base : ")) 
            n21 = int(input("please enter height : ")) 
            n22 = (n19 + n20) * n21 / 2
            print(n22)    
        elif ope == "8":
            print("Trapezoidal perimeter = sum of four sides")
            n23 = int(input("please enter side one : ")) 
            n24 = int(input("please enter side two : ")) 
            n25 = int(input("please enter side three : ")) 
            n26 = int(input("please enter side four : ")) 
            n27 = n23 + n24 + n25 + n26 
            print(n27) 
        elif ope == "9":
            print("Lozenge area = (large diameter * small diameter) / 2")
            n28 = int(input("please enter large diameter : "))
            n29 = int(input("please enter small diameter : "))
            n30 = (n28 * n29) / 2
            print(n30)    
        elif ope == "10":
            print("Lozenge perimeter = one side * 4")
            n31 = int(input("please enter one side : ")) 
            n32 = n31 * 4
            print(n32) 
        elif ope == "11":
            print("Parallel area = height rule")
            n33 = int(input("please enter height rule : "))
            print(n33)  
        elif ope == "12":
            print("Perpendicular perimeter = sum of two consecutive sides * 2")
            n34 = int(input("please enter consecutive side one : ")) 
            n35 = int(input("please enter consecutive side two : ")) 
            n36 = n34 + n35 * 2
            print(n36)
        elif ope == "13":
            print("Circle area = P number (3.14) * radius * radius")
            n37 = int(input("please enter radius : ")) 
            n38 = 3.14 * n37 * n37 
            print(n38) 
        elif ope == "14":
            print("Circle perimeter = P number (3.14) * diameter")
            n39 = int(input("please enter diameter : ")) 
            n40 = 3.14 * n39
            print(n40)
        elif ope == "15":
            print("Sphere area = 4 * 3.14 radius to the power of two") 
            n41 = int(input("please enter radius : ")) 
            n42 = 4 * 3.14 * n41 ** 2
            print(n42)
        elif ope == "16":
            print("Sphere volume = four thirds * 3.14 radius to the power of three") 
            n43 = int(input("please enter four thirds : "))
            n44 = int(input("please enter radius : ")) 
            n45 = n43 * 3.14 * n44 ** 2
            print(n45)
        elif ope == "17":
            print("Rectangular cube volume = length * width * height") 
            n46 = int(input("please enter length : ")) 
            n47 = int(input("please enter width : "))
            n48 = int(input("please enter height : "))
            n49 = n46 * n47 * n48 
            print(n49)
        elif ope == "18":
            print("Square cube volume = base * height (edge ​​length * area of ​​one face)")
            n50 = int(input("please enter base : ")) 
            n51 = int(input("please enter height : "))
            n52 = int(input("please enter edge length : "))
            n53 = int(input("please enter area of one face : "))
            n54 = n50 * n51 (n52 * n53)
            print(n54)
        elif ope == "19":
            print("Pyramid volume = area of ​​the base of the pyramid * height of the pyramid * one third")
            n55 = int(input("please enter area of ​​the base of the pyramid : "))
            n56 = int(input("please enter height of the pyramid : ")) 
            n57 = int(input("please enter one third : "))
            n58 = n55 * n56 * n57
            print(n58)
        elif ope == "20":
            print("Regular pyramid area = mile length * perimeter * one-half + (base area)")
            n59 = int(input("please enter mile lenght : "))
            n60 = int(input("please enter perimeter : "))
            n61 = int(input("please enter one-half : ")) 
            n62 = int(input("please enter base area : ")) 
            n63 = n59 * n60 * n61 + (n62)
            print(n63) 
        elif ope == "21":
            print("Irregular pyramid area = (lateral area) + (base area)")
            n64 = int(input("please enter lateral area : "))
            n65 = int(input("please enter base area : ")) 
            n66 = (n64) + (n65)
            print(n66) 
        elif ope == "22":
            print("Lateral area of ​​the cylinder = circumference of the base * height volume of the cylinder = area of ​​the base * height")
            n67 = int(input("please enter circumference of the base : ")) 
            n68 = int(input("please enter area of the base : ")) 
            n69 = int(input("please enter height : ")) 
            n70 = n68 * n69
            n71 = n70 * n67
            print(n71)
        elif ope == "23":
            print("Total surface of the cylinder = level of two bases + lateral area (total area of ​​two bases + height * around the base)")
            n72 = int(input("please enter level of two bases : ")) 
            n73 = int(input("please enter total area of two base : ")) 
            n74 = int(input("please enter height : "))
            n75 = int(input("please enter around the base : "))
            n76 = n73 + n74 * n75
            n77 = n76 + n72
            print(n77)    
        elif ope == "24":
            print("Cone volume = base area * one third * height")
            n78 = int(input("please enter base area: "))  
            n79 = int(input("please enter one third : "))
            n80 = int(input("please enter height : ")) 
            n81 = n78 * n79 * n80
            print(n81)  
        elif ope == "25":
            print("Lateral area of ​​the cone = P number (3.14) * radius * side length")
            n82 = int(input("please enter radius : ")) 
            n83 = int(input("please enter side length : "))
            n84 = 3.14 * n82 * n83
            print(n84)  
        elif ope == "26":
            print("Total area of ​​the cone = (radius + side length) * radius * number (3.14)") 
            n85 = int(input("please enter radius : ")) 
            n86 = int(input("please enter side length : ")) 
            n87 = (n85 + n86) * n85 * 3.14
            print(n87) 
        elif ope == "27":
            print("Side area of ​​the charter = the total area of ​​the side surfaces")
            n88 = int(input("please enter the total area of ​​the side surfaces : ")) 
            print(n88)   
        elif ope == "28":
            print("Total area of ​​the charter = total area of ​​two rules + total area of ​​lateral surfaces")
            n89 = int(input("please enter total area of ​​two rules : "))
            n90 = int(input("please enter total area of ​​lateral surfaces : "))
            n91 = n89 + n90
            print(n91)
        ch3 = input("do you like try again (y , n) : ")
        if ch3 == "y":
            pro()
        else:
            ex3 = input("please enter one key to exit : ")
    elif op == "4":
        print(Fore.CYAN + "Service speed  |  Maximum download in the best conditions")
        print(Fore.CYAN + "1024 (1 Mbps)  |  128 KBps")
        print(Fore.CYAN + "2048 (2 Mbps)  |  256 KBps")
        print(Fore.CYAN + "3017 (3 Mbps)  |  384 KBps")
        print(Fore.CYAN + "4096 (4 Mbps)  |  512 KBps")
        print(Fore.CYAN + "8192 (8 Mbps)  |  1024 KBps")
        print(Fore.CYAN + "16384 (16 Mbps)|  2048 KBps")
        ch5 = input("do you like try again (y , n) : ")
        if ch5 == "y":
            pro()
        else:
            ex5 = input("please enter one key to exit : ") 
    elif op == "5":
        print(math.pi)
        ch6 = input("do you like try again (y , n) : ")
        if ch6 == "y":
            pro()
        else:
            ex6 = input("please enter one key to exit : ") 
    elif op == "6":
        num19 = int(input("please enter one number : "))   
        print(abs(num19)) 
        ch7 = input("do you like try again (y , n) : ")
        if ch7 == "y":
            pro()
        else:
            ex7 = input("please enter one key to exit : ")
    elif op == "7":
        num20 = int(input("please enter one number : "))  
        print(math.sqrt(num20))
        ch8 = input("do you like try again (y , n) : ")
        if ch8 == "y":
            pro()
        else:
            ex8 = input("please enter one key to exit : ") 
    elif op == "8":
        num21 = int(input("please enter your first number : ")) 
        num22 = int(input("please enter your second number : "))
        print(math.pow(num21, num22))
        ch9 = input("do you like try again (y , n) : ")
        if ch9 == "y":
            pro()
        else:
            ex9 = input("please enter one key to exit : ")
    elif op == "9":
        num23 = int(input("please enter your cos : ")) 
        num24 = int(input("please enter your sin : ")) 
        num25 = int(input("please enter your tan : ")) 
        print(math.cos(num23)) 
        print(math.sin(num24))
        print(math.tan(num25))
        ch10 = input("do you like try again (y , n) : ")
        if ch10 == "y":
            pro()
        else:
            ex10 = input("please enter one key to exit : ") 
    elif op == "10":
        num26 = int(input("please enter your number : ")) 
        print(math.degrees(num26))
        ch11 = input("do you like try again (y , n) : ")
        if ch11 == "y":
            pro()
        else:
            ex11 = input("please enter one key to exit : ") 
    elif op == "11":
        num27 = int(input("please enter your number : "))
        print(math.radians(num27))
        ch12 = input("do you like try again (y , n) : ")
        if ch12 == "y":
            pro()
        else:
            ex12 = input("please enter one key to exit : ")
    elif op == "12":
        num28 = set(input("please enter the numbers of one : "))
        num29 = set(input("please enter the numbers of two : "))
        A = num28
        B = num29
        A_union_B = A | B
        B_union_A = B | A
        print(A.union(B))
        print(B.union(A))
        ch13 = input("do you like try again (y , n) : ")
        if ch13 == "y":
            pro()
        else:
            ex13 = input("please enter one key to exit : ")
    elif op == "13":
        num30 = set(input("please enter the numbers of one : "))
        num31 = set(input("please enter the numbers of two : ")) 
        A = num30
        B = num31
        print(A - B)
        print(A.difference(B))
        print(B.difference(A)) 
        ch14 = input("do you like try again (y , n) : ")
        if ch14 == "y":
            pro()
        else:
            ex14 = input("please enter one key to exit : ")
    elif op == "14":
        num32 = set(input("please enter the numbers of one : "))
        num33 = set(input("please enter the numbers of two : "))
        A = num32
        B = num33
        print(A & B)
        print(A.intersection(B))
        print(B.intersection(A))
        ch15 = input("do you like try again (y , n) : ")
        if ch15 == "y":
            pro()
        else:
            ex15 = input("please enter one key to exit : ")                                                                  
    else:
        ch4 = input("do you like try again (y , n) : ")
        if ch4 == "y":
            pro()
        else:
            ex4 = input("please enter one key to exit : ")                                                                                  
pro()                          