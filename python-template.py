#! /usr/bin/env python3
#SHEBANG
#created by Dinesh_Kumar_Palanivelu
#Save file as <title>.py in your preferred location. Then start typing
try:
       module1 = "argparse"
       #import modules with methods in this space
       import argparse
except:
       #if module not found in local
       print(f"Please run pip install {module1}")
try:
       module2 = "os"
       #import modules with methods in this space
       import os
except:
       #if module not found in local
       print(f"Please run pip install {module2}")
try:
       module3 = "csv"
       #import modules with methods in this space
       import csv
except:
       #if module not found in local
       print(f"Please run pip install {module3}")


#Including breaking sequence
print("Press 'ctrl+c' anytime to exit. Thanks.\n")

#Ignore below argparse function if it is confusing. It is just an example.        
def argparser():
       parser = argparse.ArgumentParser(description="Welcome to my Application"); parser.print_help();
       #argparse with description
       parser.add_argument('arg1', type = int, action = 'store', help='Argument input 1');
       parser.add_argument('arg2', type = int, action = 'store', help='Argument input 2')
       #Adding arguments       
       args = parser.parse_args()
       input3=args.arg1+args.arg2;
       #return output to the function argparser() 
       return f"Output is {input3}";
       
       
#write your main function here. You will call all required functions here.      
def main():
       try:
              #nothing will be printed when you call below function because you just return. try print(argarparser()) to print
              print(argparser());                     
       except KeyboardInterrupt: #ctrl+c sequence is included
              print("Exiting because of program interpreted by user"); print("Thanks for using my application");       
              
if __name__=='__main__':
       main() 
