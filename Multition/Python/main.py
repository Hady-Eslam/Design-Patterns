from Multition import Multition

class_v1_1 = Multition.GetInstance('Class1')
class_v1_2 = Multition.GetInstance('Class1')
print(class_v1_1 is class_v1_2)

class_v2_1 = Multition.GetInstance('Class2')
class_v2_2 = Multition.GetInstance('Class2')
print(class_v2_1 is class_v2_2)

class_v3_1 = Multition.GetInstance('Class3')
class_v3_2 = Multition.GetInstance('Class3')
print(class_v3_1 is class_v3_2)

print(class_v2_1 is class_v3_2)
