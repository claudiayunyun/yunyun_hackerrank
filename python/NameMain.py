# What does the if __name__ == “__main__”: do?
# Quote from https://www.geeksforgeeks.org/what-does-the-if-__name__-__main__-do/
# If the python interpreter is running that module (the source file) as the main program, 
# it sets the special __name__ variable to have a value “__main__”. 
# If this file is being imported from another module, 
# __name__ will be set to the module’s name. 
# Module’s name is available as value to __name__ global variable.
# 


# Python program to execute  
# main directly 
print ("Always executed")
  
if __name__ == "__main__": 
    print ("Executed when invoked directly")
else: 
    print ("Executed when imported")