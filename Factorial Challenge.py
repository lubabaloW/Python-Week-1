class Person:
    def _init_(self, speak, age):
        self.speak = speak
        self.age = age

p1 = Person("English", 30)   

print(p1.speak) 
print(p1.age)