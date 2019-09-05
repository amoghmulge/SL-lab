class Person:
	def __init__(self,name,age):
		self.name = name
		self.age = age

p1 = Person("dwarkesh",14)

print("\n Name of person is ",p1.name)
print("\n Age of person is ",p1.age)

#Printing after deleting just theage attribute for p1#
del p1.age
print("\n Name of the person #1 is ",p1.name)

#Printing after deleting p1#
del p1
print("\n Name of the person #1 is ",p1.name)
:this gives and error as p1 is deleted already.