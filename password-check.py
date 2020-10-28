import re
import csv



def check_length():
 input_str = input("Password: ")
    #checking if the length of the password is at least 6 chracters
 if len(input_str) < 6:
  print("your password must be at lesat 6 chracters!")
  check_length()
 elif len(input_str) >= 6:

  if re.match( "^(?=.*[A-Z].*)(?=.*[0-9].*)(?=.*[a-z].*)" , str(input_str) ) == None :
   print("Your password must contain at least one number, one uppercase letter and onw lowercase letter!")
   check_length()
  print("password ok")
  return input_str


check_length()


