## Log Analysis Using Regular Expressions
### Introduction
Imagine your company uses a server that runs a service called ticky, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.
The service's developers need your help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, for this lab, you'll write some automation scripts that will process the system log and generate reports based on the information extracted from the log files.

##What you'll do
- Use regex to parse a log file
- Append and modify values in a dictionary
- Write to a file in CSV format
- Move files to the appropriate directory for use with the CSV->HTML converter

``chmod 600 ~/Documents/downloads/qwikLABS-XXXXX.pem``
``ssh -i ~/Documents/downloads/qwikLABS-XXXXX.pem username@External Ip Address``

1. We'll be working with a log file named syslog.log, which contains logs related to ticky.
 The log lines follow a pattern similar to the ones we've seen before. Something like this:

  ``May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)``
  ``Jun 1 11:06:48 ubuntu.local ticky: ERROR: Connection to DB failed (username)``
  
In this section, we'll search and view different types of error messages. The error messages for ticky details the problems with the file with a timestamp for when each problem occurred.

These are a few kinds of listed error:

Timeout while retrieving information
The ticket was modified while updating
Connection to DB failed
Tried to add information to a closed ticket
Permission denied while closing ticket
Ticket doesn't exist
To grep all the logs from ticky, use the following command:
``grep ticky syslog.log``
``grep "ERROR" syslog.log``

import re
line = "May 27 11:45:40 ubuntu.local ticky: ERROR: Error creating ticket [#1234] (username)"
re.search(r"ticky: ERROR: ([\w ]*) ", line)

2. Sort
  fruit = {"oranges": 3, "apples": 5, "bananas": 7, "pears": 2}
  sorted(fruit.items()) // sorted function to sort the items in the dictionary.
We'll now sort the dictionary using the item's key. For this use the operator module.

Pass the function itemgetter() as an argument to the sorted() function. 
Since the second element of tuple needs to be sorted, pass the argument 0 to the itemgetter function of the operator module.  

import operator
sorted(fruit.items(), key=operator.itemgetter(0)) // sort by key
sorted(fruit.items(), key=operator.itemgetter(1)) // sort by values
sorted(fruit.items(), key = operator.itemgetter(1), reverse=True and reverse

#!/usr/bin/env python3
import re
import csv
import operator
import sys

per_user = {}
errors = {}

logfile = 'syslog.log'
f = open(logfile, 'r')

errorfile = 'error_message.csv'
userfile = 'user_statistics.csv'

for log in f:
        result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
        if result.group(2) not in errors.keys():
                errors[result.group(2)] = 0
        errors[result.group(2)] += 1
        if result.group(3) not in per_user.keys():
                per_user[result.group(3)] = {}
                per_user[result.group(3)]["INFO"] = 0
                per_user[result.group(3)]["ERROR"] = 0

        if result.group(1) == "INFO":
                per_user[result.group(3)]["INFO"] += 1
        elif result.group(1) == "ERROR":
                per_user[result.group(3)]["ERROR"] += 1

errors = sorted(errors.items(), key = operator.itemgetter(1), reverse = True)
per_user = sorted(per_user.items())

f.close()
errors.insert(0, ('Error', 'Count'))

f = open(errorfile, 'w')
for error in errors:
        a,b = error
        f.write(str(a)+','+str(b)+'\n')
f.close()

f = open(userfile, 'w')
f.write("Username,INFO,ERROR\n")
for stats in per_user:
        a, b = stats
        f.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')

  
  
