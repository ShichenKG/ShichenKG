import time
a=("1")
b=("1")
c=0
x= str(111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111)
while a!=1:
    while a!=("1111111111111"):
        while b!=x:
            b= b+a
            time.sleep(0.01)
            print (b)
    #        print ("")
            x=int(x)
            b=int(b)
            if x<b:
                break
            x=str(x)
            b=str(b)
        x=str(x)
        b=str(b)
        while b!=(""):
            b=b[:c-1:]
            time.sleep(0.01)
            print (b)
    #        print ("")
        b=str(1)
        c=c-1
        a=a+("1")
#    print (c)
    d=-1
#    print (d)
#    time.sleep(1000)
    while a!=("11"):
        while b!=x:
            b=b+a[:-2:]
            time.sleep(0.01)
            print (b)
            x=int(x)
            b=int(b)
            if x<b:
                break
            x=str(x)
            b=str(b)
        x=str(x)
        b=str(b)
        
        while b!=(""):
            b=b[:c+1:]
            time.sleep(0.01)
            print (b)
    #        print ("")
        b=str(1)
        c=c+1
        a=a[:-1:]
