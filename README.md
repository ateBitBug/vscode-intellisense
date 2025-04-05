# vscode-intellisense

I'm using the latest version of VSCode and my extensions are:

vscode: 1.98.2
os: windows 11

extensions:

    pylance Version 2025.4.1
        Identifier ms-python.vscode-pylance
        Version 2025.4.1
        Last Updated
        2025-04-04, 05:21:39
    
    python Version 2025.2.0
        Identifier ms-python.python
        Version 2025.2.0
        Last Updated
        2025-03-30, 07:59:26
    
    python debugger
        Identifier ms-python.debugpy
        Version 2025.4.1
        Last Updated
        2025-03-30, 07:59:26

THE BUG

I created an example Python code which replicates the bug.  Please try the program 'if-all-in-one-test-1-98-2.py.

When the line #77-78 are uncommented (which is the 235th 'if-statement'), the Python Intellisense doesn't auto display the available methods/properties.

