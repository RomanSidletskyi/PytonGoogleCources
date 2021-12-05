#We're using the same syslog, and we want to display the date, time, and process id that's inside the square brackets. 
#We can read each line of the syslog and pass the contents to the show_time_of_pid function. 
#Fill in the gaps to extract the date, time, and process id from the passed line, and return this format: Jul 6 14:01:23 pid:29440.
      
import re
def show_time_of_pid(line):
  pattern = r'^(\w+ [0-9] [0-9]+:[0-9]+:[0-9]+) [\w\.]+ [\w=]+\[([0-9]+)\]'
  result = re.search(pattern, line)
  return '{} pid:{}'.format(result[1],result[2])

print(show_time_of_pid("Jul 6 14:01:23 computer.name CRON[29440]: USER (good_user)")) # Jul 6 14:01:23 pid:29440

print(show_time_of_pid("Jul 6 14:02:08 computer.name jam_tag=psim[29187]: (UUID:006)")) # Jul 6 14:02:08 pid:29187

print(show_time_of_pid("Jul 6 14:02:09 computer.name jam_tag=psim[29187]: (UUID:007)")) # Jul 6 14:02:09 pid:29187

print(show_time_of_pid("Jul 6 14:03:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:03:01 pid:29440

print(show_time_of_pid("Jul 6 14:03:40 computer.name cacheclient[29807]: start syncing from \"0xDEADBEEF\"")) # Jul 6 14:03:40 pid:29807

print(show_time_of_pid("Jul 6 14:04:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:04:01 pid:29440

print(show_time_of_pid("Jul 6 14:05:01 computer.name CRON[29440]: USER (naughty_user)")) # Jul 6 14:05:01 pid:29440


/*
chmod 600 ~/Downloads/qwikLABS-XXXXX.pem
ssh -i ~/Downloads/qwikLABS-XXXXX.pem username@External Ip Address

What you'll do
Write a script to search the log file using regex to find for the exact error.
Report the error into a separate file so you know what's wrong for further analysis
*/
#!/usr/bin/env python3
import sys
import os
import re
def error_search(log_file):
  error = input("What is the error? ")
  returned_errors = []
  with open(log_file, mode='r',encoding='UTF-8') as file:
    for log in  file.readlines():
      error_patterns = ["error"]
      for i in range(len(error.split(' '))):
        error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
      if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
        returned_errors.append(log)
    file.close()
  return returned_errors
  
def file_output(returned_errors):
  with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    for error in returned_errors:
      file.write(error)
    file.close()
if __name__ == "__main__":
  log_file = sys.argv[1]
  returned_errors = error_search(log_file)
  file_output(returned_errors)
  sys.exit(0)
  
  
  #Save the file by clicking Ctrl-o, followed by the Enter key and Ctrl-x.
  chmod 600 ~/Documents/downloads/qwiklabs-L6884454.pem
  ssh -i ~/Documents/downloads/qwiklabs-L6884454.pem student-01-6bba6a24b212@34.70.54.205

#Make the file executable before running it.

``sudo chmod +x find_error.py``
#Now, run the file by passing the path to fishy.log as a parameter to the script.

``./find_error.py ~/data/fishy.log``
#This script will now prompt for the type of error to be searched. Continue by entering the following type of error:

#CRON ERROR Failed to start
