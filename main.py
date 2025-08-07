import sys
import os

# Add the current directory to Python's path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src import _contactbook
print("Hello user 😊!!!!")
heck = -1
while(heck!=0):
    heck = int(input("To add contact write '1'\nTo view contact write '2'\nTo search contact write '3'\nTo delete contact write '4'\nTo get out write '0'\nYour choice: "))
    if(heck==1):
        _contactbook.Contactbook.add_contact()
    elif(heck==2):
        _contactbook.Contactbook.view_contact()
    elif(heck==3):
        _contactbook.Contactbook.search_contact()
    elif(heck==4):
        _contactbook.Contactbook.delete_contact()
    elif(heck==0):
        print("BYE BYE 😄!!!!")
    else:
        print("invaid input... Please try again 😄...")