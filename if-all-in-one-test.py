'''
vscode: 1.99.0
os: windows 11  v10.0.26100 Build 26100

extensions:
    pylance
        Identifier ms-python.vscode-pylance
        Version 2025.4.1
        Last Updated 2025-04-05, 07:36:25
    
    python
        Identifier ms-python.python
        Version 2025.4.0
        Last Updated 2025-04-05, 07:36:25
    
    python debugger
        Identifier ms-python.debugpy
        Version 2025.6.0
        Last Updated 2025-04-05, 07:36:25
'''

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
Accessing CHILD class methods.
'''
child = Child()
child.getChildWorld()
child.getIndex()


a = 1
b = 2
c = None


'''
The intellisense fails when line# 74-75 is uncommented which is the 235th
'if statement'.

When the line are uncommented, the intellisense fails to provide
the auto complete feature for the CHILD object.

For example, when typing 'child.', nothing shows up.

SUMMARY:
When line# 74-75 is uncommented:
    vscode's intellisense fails when these line# are uncommented.
'''
# if (a == 1 and b == 2):
#     c = 3


'''
Try 'child.' here or anywhere in the code.
With the line# 74-75 uncommented, the intellisense fails
'''
child.getChildWorld()


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

