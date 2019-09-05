class Person:
 def __init__(self,name,age):
    self.name=name;
    self.age=age;

p1=Person("Jeff Bezos",54)
p2=Person("Erlich Backhman",42)

print("\n Name of person #1 is",p1.name)
print("\n Age of person #1 is",p1.age)

print("\n Name of person #2 is",p2.name)
print("\n Age of person #1 is",p2.age)

p2.age=60
print("\n Age of person #1 is",p2.age)