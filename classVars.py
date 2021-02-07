class ClassVar():
    collection = 2
    def __init__(self, var1):
        self.var1 = var1
    def set_vars(self, var2):
        self.collection = var2

object1 = ClassVar(5)
print(object1.var1, object1.collection)
#object1.set_vars(10)
object2 = ClassVar(4)
print(object2.var1, object2.collection)

ClassVar.collection = 10
print(object1.var1, object1.collection)

#object2 = ClassVar(4)
print(object2.var1, object2.collection)