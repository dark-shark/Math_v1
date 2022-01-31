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
    print(Fore.MAGENTA + "4- Unit Convert (internet services)")
    op = input("please enter your operation (1 to 4) : ")
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
            n1 = int(input("please enter one side : "))
            n2 = int(input("please enter itself : "))
            n3 = n1 * n2
            print(n3)
        if ope == "2":
            print("Square perimeter = one side * 4")
            n4 = int(input("please enter one side : "))
            n5 = n4 * 4
            print(n5)  
        if ope == "3":
            print("Rectangular area = length * width") 
            n6 = int(input("please enter lengh : "))
            n7 = int(input("please enter width : "))
            n8 = n6 * n7
            print(n8)
        if ope == "4":
            print("Rectangular perimeter = (length + width) * 2")
            n9 = int(input("please enter length : "))  
            n10 = int(input("please enter width : ")) 
            n11 = (n9 + n10) * 2
            print(n11)
        if ope == "5":
            print("Triangle area = (base * height) / 2")
            n12 = int(input("please enter base : "))  
            n13 = int(input("please enter height : ")) 
            n14 = (n12 * n13) / 2
            print(n14)
        if ope == "6":
            print("Triangle perimeter = sum of three sides") 
            n15 = int(input("please enter side one : ")) 
            n16 = int(input("please enter side two : ")) 
            n17 = int(input("please enter side three : ")) 
            n18 = n15 + n16 + n17 
            print(n18)
        if ope == "7":
            print("Trapezoid area = (large base + small base) * height / 2")
            n19 = int(input("please enter large base : "))
            n20 = int(input("please enter small base : ")) 
            n21 = int(input("please enter height : ")) 
            n22 = (n19 + n20) * n21 / 2
            print(n22)    
        if ope == "8":
            print("Trapezoidal perimeter = sum of four sides")
            n23 = int(input("please enter side one : ")) 
            n24 = int(input("please enter side two : ")) 
            n25 = int(input("please enter side three : ")) 
            n26 = int(input("please enter side four : ")) 
            n27 = n23 + n24 + n25 + n26 
            print(n27) 
        if ope == "9":
            print("Lozenge area = (large diameter * small diameter) / 2")
            n28 = int(input("please enter large diameter : "))
            n29 = int(input("please enter small diameter : "))
            n30 = (n28 * n29) / 2
            print(n30)    
        if ope == "10":
            print("Lozenge perimeter = one side * 4")
            n31 = int(input("please enter one side : ")) 
            n32 = n31 * 4
            print(n32) 
        if ope == "11":
            print("Parallel area = height rule")
            n33 = int(input("please enter height rule : "))
            print(n33)  
        if ope == "12":
            print("Perpendicular perimeter = sum of two consecutive sides * 2")
            n34 = int(input("please enter consecutive side one : ")) 
            n35 = int(input("please enter consecutive side two : ")) 
            n36 = n34 + n35 * 2
            print(n36)
        if ope == "13":
            print("Circle area = P number (3.14) * radius * radius")
            n37 = int(input("please enter radius : ")) 
            n38 = 3.14 * n37 * n37 
            print(n38) 
        if ope == "14":
            print("Circle perimeter = P number (3.14) * diameter")
            n39 = int(input("please enter diameter : ")) 
            n40 = 3.14 * n39
            print(n40)
        if ope == "15":
            print("Sphere area = 4 * 3.14 radius to the power of two") 
            n41 = int(input("please enter radius : ")) 
            n42 = 4 * 3.14 * n41 ** 2
            print(n42)
        if ope == "16":
            print("Sphere volume = four thirds * 3.14 radius to the power of three") 
            n43 = int(input("please enter four thirds : "))
            n44 = int(input("please enter radius : ")) 
            n45 = n43 * 3.14 * n44 ** 2
            print(n45)
        if ope == "17":
            print("Rectangular cube volume = length * width * height") 
            n46 = int(input("please enter length : ")) 
            n47 = int(input("please enter width : "))
            n48 = int(input("please enter height : "))
            n49 = n46 * n47 * n48 
            print(n49)
        if ope == "18":
            print("Square cube volume = base * height (edge ​​length * area of ​​one face)")
            n50 = int(input("please enter base : ")) 
            n51 = int(input("please enter height : "))
            n52 = int(input("please enter edge length : "))
            n53 = int(input("please enter area of one face : "))
            n54 = n50 * n51 (n52 * n53)
            print(n54)
        if ope == "19":
            print("Pyramid volume = area of ​​the base of the pyramid * height of the pyramid * one third")
            n55 = int(input("please enter area of ​​the base of the pyramid : "))
            n56 = int(input("please enter height of the pyramid : ")) 
            n57 = int(input("please enter one third : "))
            n58 = n55 * n56 * n57
            print(n58)
        if ope == "20":
            print("Regular pyramid area = mile length * perimeter * one-half + (base area)")
            n59 = int(input("please enter mile lenght : "))
            n60 = int(input("please enter perimeter : "))
            n61 = int(input("please enter one-half : ")) 
            n62 = int(input("please enter base area : ")) 
            n63 = n59 * n60 * n61 + (n62)
            print(n63) 
        if ope == "21":
            print("Irregular pyramid area = (lateral area) + (base area)")
            n64 = int(input("please enter lateral area : "))
            n65 = int(input("please enter base area : ")) 
            n66 = (n64) + (n65)
            print(n66) 
        if ope == "22":
            print("Lateral area of ​​the cylinder = circumference of the base * height volume of the cylinder = area of ​​the base * height")
            n67 = int(input("please enter circumference of the base : ")) 
            n68 = int(input("please enter area of the base : ")) 
            n69 = int(input("please enter height : ")) 
            n70 = n68 * n69
            n71 = n70 * n67
            print(n71)
        if ope == "23":
            print("Total surface of the cylinder = level of two bases + lateral area (total area of ​​two bases + height * around the base)")
            n72 = int(input("please enter level of two bases : ")) 
            n73 = int(input("please enter total area of two base : ")) 
            n74 = int(input("please enter height : "))
            n75 = int(input("please enter around the base : "))
            n76 = n73 + n74 * n75
            n77 = n76 + n72
            print(n77)    
        if ope == "24":
            print("Cone volume = base area * one third * height")
            n78 = int(input("please enter base area: "))  
            n79 = int(input("please enter one third : "))
            n80 = int(input("please enter height : ")) 
            n81 = n78 * n79 * n80
            print(n81)  
        if ope == "25":
            print("Lateral area of ​​the cone = P number (3.14) * radius * side length")
            n82 = int(input("please enter radius : ")) 
            n83 = int(input("please enter side length : "))
            n84 = 3.14 * n82 * n83
            print(n84)  
        if ope == "26":
            print("Total area of ​​the cone = (radius + side length) * radius * number (3.14)") 
            n85 = int(input("please enter radius : ")) 
            n86 = int(input("please enter side length : ")) 
            n87 = (n85 + n86) * n85 * 3.14
            print(n87) 
        if ope == "27":
            print("Side area of ​​the charter = the total area of ​​the side surfaces")
            n88 = int(input("please enter the total area of ​​the side surfaces : ")) 
            print(n88)   
        if ope == "28":
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
    if op == "4":
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
    else:
        ch4 = input("do you like try again (y , n) : ")
        if ch4 == "y":
            pro()
        else:
            ex4 = input("please enter one key to exit : ")                                                                                  
pro()                          