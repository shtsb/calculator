import math

input1=float(input("please enter first number"))
op=input("please choose operation + - * / ")
input2=float(input("please enter second number"))
if op =="+" : 
    result = input1+input2
elif op == "-" :
    result = input1-input2
elif op == "*" :
    result = input1*input2
elif op == "/" :  
    if input2 == 0 :
        result = "it is impossible"
    else :
        result = input1/input2
else :
    result = "please choose operation that exit in this calculatore like + - * /" 
print (result)       






