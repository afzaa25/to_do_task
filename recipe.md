# Check if text includes the string #TODO




## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
# As a user 
# So that I can keep track of my tasks
# I want to check if a text includes the string #TODO.

## 2. Design a Method Signature
_Include the name of the method, its parameters, return value, and side effects_


def to_do(text)
# Parameters:
    # text - a string including #TODO
# Return:
    # It will return the text if #TODO is found
    # Otherwise it will raise an exception




## 3. Create Examples as Tests 
_Make a list of examples of what the method will take and return_

""" 
If string is written without #TODO
It will raise an error
"""
# test_no_to_do("Reminder: You are amazing!")
# => ['This does not have a TODO]

# test_with_to_do("#TODO: To do the laundry!")
#  => ["#TODO: To do the laundry!"]


_Encode each example as a test. You can add to the above list as you go_




## 4. Implement the Behaviour
_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour_



