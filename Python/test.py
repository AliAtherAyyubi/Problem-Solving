class Class1:
    def function_1(self):
         print("a")

    def function_2(self):
         print("b")


class Class2:
    def function_1(self):
         print("c")

    def function_3(self):
         print("d")


class Class3:
    def function_2(self):
         print("e")

    def function_3(self):
         print("f")


class ClassA(Class3, Class1):
    def function_3(self):
         print("h")


class ClassB(Class2):
    def function_2(self):
         print("i")

    def function_3(self):
         print("j")


class ClassC(Class1):
    def function_2(self):
         print("k")

    def function_3(self):
         print("l")
      
      
ClassB().function_3()
ClassA().function_1()
ClassB().function_2()