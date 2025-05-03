
# In object-oriented programming (OOP), encapsulation is a fundamental concept that describes wrapping variables and methods in one unit.


class UserInfo:
   def __init__(self, username, email_address):
      self.username = username # username field
      self.email_address = email_address # email field

   def check_username(self, username_to_check):
       # if check_username field matches class constructor username field above then return True else return False
       if username_to_check == self.username:
           return True
       else:
           return False
       
   def check_email(self, email_to_check):
       # if check_email field matches class constructor email field above then return True else return False
       if email_to_check == self.email_address:
           return True
       else:
           return False

user = UserInfo('user123', 'abc@edf.ghi') # our instance 
# apply user instance to check_username
print(user.check_username('user123')) # returns True
print(user.check_username('user456')) # returns False
print(user.check_email('bert@gmail.com')) # returns False
print(user.check_email('abc@edf.ghi')) # returns True