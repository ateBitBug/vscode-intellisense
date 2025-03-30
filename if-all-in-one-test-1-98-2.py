class Parent:
    def __init__(self):
        print('class Parent: __init__')

        self.parent1 = 1
        self.parent2 = 2

    def getParentWorld(self):
        print('Parent: Earth')



class Child(Parent):
    def __init__(self):
        super().__init__()
        print('__init__: Child')

        self.child1 = 1
        self.child2 = 2

    def getChildWorld(self):
        print('Child: Ocean')

    def getIndex(self):
        return [0,1,2]

'''
Accessing CHILD classes methods.
'''
child = Child()
child.getChildWorld()
child.getIndex()


a = 1
b = 2
c = None


'''
The intellisense fails when line# 55-56 is uncommented which is the 235th
'if statement'.

When the line are uncommented, the intellisense fails to provide
the auto complete feature for the CHILD object.

For example, when typing 'child.', nothing shows up.

SUMMARY:
When line# 55-56 is uncommented:
    vscode version 1.84.2 intellisense works without any issues.
    vscode version 1.98.2 intellisense fails when line# are uncommented.
        - in fact, the intellisense has been failing since Nov2023 1.85.0.
'''
# if (a == 1 and b == 2):
#     c = 3

'''
Try 'child.' here or anywhere in the code.
With the line# 55-56 uncommented, the intellisense fails.
'''


'''
The intellisese works on 234 of 'if statements'
'''
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3
if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

if (a == 1 and b == 2):
    c = 3

