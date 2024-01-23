fh=open("output 5.txt",'w')
a=int(input("enter the year:"))
if(a%4==0):
    fh.write("it is a leap year "+str(a))
else:
    fh.write("it is not a leap year"+str(a))
fh.close
