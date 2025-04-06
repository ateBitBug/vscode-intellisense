# vscode-intellisense
# UPDATE: I tried this with vscode: v1.99.0 and the bug still exists.

I'm using the latest version of VSCode and my extensions are:

vscode: 1.99.0

os: windows 11

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
        
THE BUG

I created an example Python code which replicates the bug.  Please try the program 'if-all-in-one-test.py.

When the line #74-75 are uncommented (which is the 235th 'if-statement'), the Python Intellisense doesn't auto display the available methods/properties.

