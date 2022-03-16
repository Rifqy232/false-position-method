#!/usr/bin/python3

def func(x):
    return (9.8 * x / 25 * (1 - pow(2.718281828459045, -(25 / x) * 15))) - 45

def findx():
    i = 0
    xl,xu,fxl,fxu = 0,0,0,0
    while True:
        # print(i)
        if i == 0:
            i += 1
            continue
        
        f = func(i)
        if(f < 0):
            xl = i
            fxl = f
        elif(f > 0):
            xu = i
            fxu = f

        i += 1
        if(fxl * fxu < 0):
            break
    
    # print(xl, xu, fxl, fxu)
    return xl, xu

def false_position(xl, xu, es):
    xr,i = 0.0,0
    xrold = 0.0
    while True:
        print("Iteration - [%d]" % (i+1))
        xrold = xr
        fxl = func(xl)
        fxu = func(xu)
        xr = xu - ( (fxu * (xl - xu)) / (fxl - fxu) )
        fxr = func(xr)

        print("xl: %.3f\tfxl: %.10f\nxu: %.3f\tfxu: %.10f\nxr: %.3f\tfxr: %.10f\txrold: %.3f\nfxl*fxr: %.10f" % (xl,fxl,xu,fxu,xr,fxr,xrold,fxl*fxr))

        if(fxl * fxr < 0):
            xu = xr
        elif(fxl * fxr > 0):
            xl = xr
        elif(fxl * fxr == 0):
            break
            
        ea = (abs(xr - xrold) / xr) * 100
        print("ea = %.10f\n" % ea)
        i += 1
        if (ea < es):
            break
    
    print("The approximate root value is %.5f" % xr)

es = float(input("Input the stopping criterion error: "))
xl,xu = findx()
false_position(xl, xu, es)