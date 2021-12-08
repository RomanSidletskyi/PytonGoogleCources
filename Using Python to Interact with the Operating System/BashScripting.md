## Bash Scripting Resources
Check out the following links for more information:

https://ryanstutorials.net/bash-scripting-tutorial/

https://linuxconfig.org/bash-scripting-tutorial-for-beginners

https://www.shellscript.sh

1. ``echo *`` output a list of all files in the current directory
2. Which module can you load in a Python script to take advantage of star [*] like in BASH : ``Glob``
3. Conditional execution is based on the ``exit status`` of commands.
4. ``test`` command evaluates the conditions received on exit to verify that there is an exit status of 0 when the conditions are true, and 1 when they are false?
5. The opening square bracket ([), when combined with the closing square bracket (]), is an alias for which command? : ``test``

## Qwiklabs Assessment: Editing Files Using Substrings

Introduction
In this lab, you'll change the username of your coworker Jane Doe from "jane" to "jdoe" in compliance with company's naming policy. The username change has already been done. However, some files that were named with Jane's previous username "jane" haven't been updated yet. To help with this, you'll write a bash script and a Python script that will take care of the necessary rename operations.

#### What you'll do
- Practice using the cat, grep, and cut commands for file operations
- Use > and >> commands to redirect I/O stream
- Replace a substring using Python
- Run bash commands in Python
chmod 600 ~/Documents/downloads/qwiklabs-L6933910.pem
ssh -i ~/Documents/downloads/qwiklabs-L6933910.pem student-01-3b2f35b83401@34.68.220.226
