import os
import sys
print("process started")
os.system('cls')
print("enter the base of the exponent") 
x = int(input(""))
print("enter the power of the exponent")
y = int(input(""))
print("the answer is")
print(x ** y)
print("process ended")
print("restart y/n")
o = input("")
if o == "y":
    os.execl(sys.executable, sys.executable, *sys.argv) 
if o == "n":
    print("process ended")