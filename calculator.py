from ast import Break


sum=0
list=0
while(True):
    x= input("enter your items Rs :")
    if(x !="q"):
        sum=sum+int(x)
        list=list+1
        print(f"your total is {sum} and items is {list}")
    else:
        print(f"your total is {sum} and total items are {list} Thanks for shoppe with us {list}")
        Break
