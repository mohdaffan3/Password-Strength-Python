# Returns True only if any String have atleast one special Character
def havespecialChar(user_password):
    special_char = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    for c in user_password:
        if c in special_char:
            return True
    return False

# Returns True only if any String have atleast one Upper and one Lower character
def haveUpperandLower(user_password):
    if any(char.isupper() for char in user_password) and any(char.islower() for char in user_password):
        return True
    return False

# Returns True only if any String have atleast one Number
def haveDigit(user_password):
    if any(char.isdigit() for char in user_password):
        return True
    return False

def passwordStrength(user_password):
    strength = {-1:"Very Weak",0:"Weak",1:"Moderately Weak",2:"Strong",3:"Moderately Strong",4:"Very Strong"}
    score = -1
    pass_length = len(user_password)
    if pass_length>=8:                                 #only password greater than or equal to 8
            score+=1
            if haveUpperandLower(user_password):       #password container both upper and lower case
                score+=1
            if haveDigit(user_password):
                score+=1
            if havespecialChar(user_password):         #password have a special character
                score+=1
            if len(set(user_password)) == pass_length: #all character are unique in password
                score+=1
    return strength[score]

    
    

# User input
user_password = input("Enter your password  : ")
print(passwordStrength(user_password))

