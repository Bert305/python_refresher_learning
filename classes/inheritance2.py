



  
#   Inheritance is a feature of object-oriented programming (OOP) that enables the transfer of methods and properties of one class to another.
  
# Inheritance allows for reusability of code as well as extending the capability of new classes.  
  
  
  
  
  
  # parent class
class Person:
    # constructor fields  
  def __init__(self, name, age):
      self.name = name
      self.age = age
  def print_info(self):
      print(self.name)
      print(self.age)

# child class
class Teacher(Person):
   # Teacher class holds the param of the Person class 
  def __init__(self, name, age, subject):
      self.subject = subject # This class inherits the same param fields as the parent class. New subject field is added
    #   self.name = name
    #   self.age = age
    #   self.subject = subject

      Person.__init__(self, name, age) # We can use the person class constructor to have further access.

# now we can execute our myTeacher instance allowing the child class to use fields from the parent class
myTeacher = Teacher("Dr. Hirani", 49, "Computer Science")
myTeacher.print_info()
print(myTeacher.subject) # Computer Science
print(myTeacher.name) # Dr. Hirani
print(myTeacher.age) # 49
print(myTeacher.subject) # Computer Science