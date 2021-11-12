This script begins with a line containing the #! character combination, which is commonly called hash bang or shebang and continues with the path to the interpreter.

``#!/usr/bin/env`` python3 uses the operating system env command, which locates and executes Python by searching the PATH environment variable. Unlike Windows, the Python interpreter is usually already in the $PATH variable on linux, so you don't have to add it.
#### Fix permission denied error. ``sudo chmod +x health_checks.py``
This is because the above command tries to run your script directly as a program. The program is parsed by the interpreter specified in the first line of the script, i.e. shebang. If the kernel finds that the first two bytes are #! it uses the rest of the line as an interpreter and passes the file as an argument. So, to do this, the file needs to have execute permission

- **access to VM** ``ssh -i ~/Downloads/qwiklabs-L5997008.pem student-01-6bba6a24b212 35.239.139.229``
- **execute** : ``./health_checks.py``
- **nano editor to open the file : ** ``./health_checks.py``
- **import module :** ``sudo apt install python3-requests``
- **Import the request module into the file using the import statements. :** ``import requests``
- **import network module (python file created ) : ** ``from network import *``
