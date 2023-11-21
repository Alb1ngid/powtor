# 1 модули 3 вида
# встроенные модули
# собвственные модули
# внешние модули
# venv виртуальная среда

# множественное наследование
# mro - порядок выполнения методов

class A:
    def a(self):
        print('это метод класса А')

class B:
    def a(self):
        print('это метод класса В')

class C(A):
    def a(self):
        print('это метод С')


class D(A,B,C):
    ...

c=D
c.a(self=1)
#1 murat,erbol
print(D.mro())

# def a()
# a()
# a()
# lambda
