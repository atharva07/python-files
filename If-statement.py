is_male = True

if is_male:
    print("You are awesome")
else:
    print("You are beautiful")

# making it little complex
is_captain = True
is_worthy = False

if is_captain or is_worthy: # OR condition is applied 
    print("You are captain america")
else:
    print("you are just an ordinary man")
 
if is_captain and is_worthy: # AND condition is applied
    print("You are captain america")
elif is_captain and not(is_worthy): # not function negates the parameter
    print("You are half captain")    
else:
    print("You are just an ordinary man")