import math

#https://pl.python.org/docs/lib/module-math.html

option = int(input("1. x+y\r\n2. x-y\r\n3. x*y\r\n4. x/y\r\n5. acos(x)\r\n6. asin(x)\r\n"+
"7. atan(x)\r\n8. atan2(y,x)\r\n9. ceil(x)\r\n10. cos(x)\r\n11. cosh(x)\r\n12. degrees(x)"+
"\r\n13. exp(x)\r\n14. fabs(x)\r\n15. floor(x)\r\n16. fmod(x,y)\r\n17. frexp(x)\r\n"+
"18. hypot(x,y)\r\n19. ldexp(x,y)\r\n20. log(x,y)\r\n21. log10(x)\r\n22. modf(x)\r\n"+
"23. pow(x,y)\r\n24. radians(x)\r\n25. sin(x)\r\n26. sinh(x)\r\n27. sqrt(x)\r\n"+
"28. tan(x)\r\n29. tanh(x)\r\n30. pi\r\n31. e\r\nEnter the number: "))
if option>0 and option<30:
    a=float(input("Enter a: "))
    if not(option>=5 and option<=7) and option!=16 and not(option>=18 and option<=20) and option!=23:
        b=float(input("Enter b: "))

    if option == 1:
        print(str(a)+'+'+str(b)+'='+str(a+b))
    elif option == 2:
        print(str(a)+'-'+str(b)+'='+str(a-b))
    elif option == 3:
        print(str(a)+'*'+str(b)+'='+str(a*b))
    elif option == 4:
        if b!=0:
            print(str(a)+'/'+str(b)+'='+str(a/b))
        elif b==0:
            print('Do not divide by zero!')
    elif option == 5:
        print("acos("+str(a)+")="+str(math.acos(a)))
    elif option == 6:
        print("asin("+str(a)+")="+str(math.asin(a)))
    elif option == 7:
        print("atan("+str(a)+")="+str(math.atan(a)))
    elif option == 8:
        print("atan2("+str(b)+"/"+str(a)+")="+str(math.atan2(b,a)))
    elif option == 9:
        print("ceil("+str(a)+")="+str(math.atan(a)))
    elif option == 10:
        print("cos("+str(a)+")="+str(math.cos(a)))
    elif option == 11:
        print("cosh("+str(a)+")="+str(math.cosh(a)))
    elif option == 12:
        print("degrees("+str(a)+")="+str(math.degrees(a)))
    elif option == 13:
        print("exp("+str(a)+")="+str(math.exp(a)))
    elif option == 14:
        print("fabs("+str(a)+")="+str(math.fabs(a)))
    elif option == 15:
        print("floor("+str(a)+")="+str(math.floor(a)))
    elif option == 16:
        print("fmod("+str(a)+","+str(b)+")="+str(math.fmod(a,b)))
    elif option == 17:
        print("frexp("+str(a)+")="+str(math.frexp(a)))
    elif option == 18:
        print("hypot("+str(a)+")="+str(math.hypot(a)))
    elif option == 19:
        print("ldexp("+str(a)+","+str(b)+")="+str(math.ldexp(a,b)))
    elif option == 20:
        print("log("+str(a)+","+str(b)+")="+str(math.log(a,b)))
    elif option == 21:
        print("log10("+str(a)+")="+str(math.log10(a)))
    elif option == 22:
        print("modf("+str(a)+")="+str(math.modf(a)))
    elif option == 23:
        print("pow("+str(a)+","+str(b)+")="+str(pow(a,b)))
    elif option == 24:
        print("radians("+str(a)+")="+str(math.radians(a)))
    elif option == 25:
        print("sin("+str(a)+")="+str(math.sin(a)))
    elif option == 26:
        print("sinh("+str(a)+")="+str(math.sinh(a)))
    elif option == 27:
        print("sqrt("+str(a)+")="+str(math.sqrt(a)))
    elif option == 28:
        print("tan("+str(a)+")="+str(math.tan(a)))
    elif option == 29:
        print("tanh("+str(a)+")="+str(math.tanh(a)))
elif option == 30:
    print("pi="+str(math.pi))
elif option == 31:
    print("e="+str(math.e))
else:
    print('Bad option')