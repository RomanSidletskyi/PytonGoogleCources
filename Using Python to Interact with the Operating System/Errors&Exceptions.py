/*We'd like to take control of the error messaging here and pre-empt this error. Fill in the blanks below to raise a ValueError in the RemoveValue() function if a value is not in the list. 
You can have the error message say something obvious like "Value must be in the given list".*/
def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

##add an assert type argument that verifies whether the input list is filled with only strings

def OrganizeList(myList):
    for item in myList:
        assert type(item)==str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))


#try/except

try:
  f=open(filename)
except OSError:
  return None

#

# Revised Guess() function
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    try:
        if my_participant_dict['Larry'] == 9:
            return True
        else:
            return False
    except KeyError:
        return None
    
participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))
