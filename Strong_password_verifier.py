import re

def password_verifier ():
    correct_pass = re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$")
    true_false = re.findall(correct_pass,password)
    if  true_false:
        print('Woah! its stronger than me')
    else:
        print('Its such a weakling')
while 1:
    password = input('Password : ')
    password_verifier()
