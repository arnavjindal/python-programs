"""USE OF SUPER"""


class A:
    classvar1 = "I am a class variable in class A"                                   # <---------------------------------------------------on fourth here
    def __init__(self):
        self.var1 = "I am inside class A's constructor"                              # <---------------------------------------------------on second here #means on parent's instance
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"                                                    # <---------------------------------------------------on third MEANS CLASS VARIABLE

    def __init__(self):                                                             #once constructor is overidden then it never looks back to parent's constructor unless super is used
        self.var1 = "I am inside class B's constructor"                             # <---------------------------------------------------first it looks for opration here """means in its own class's instance"""
        self.classvar1 = "Instance var in class B"
        # super().__init__()                                                        #THING THAT APPEARS AT LAST classvar1 WILL TAKE VALUE FROM THAT
        # print(super().classvar1)


a = A()
b = B()

print(b.special, b.var1, b.classvar1)
