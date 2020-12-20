#STRING DECLARATION
success= "Sayan is going to start a job as a coding instructor in SKILLSANTA"
print(success)

#ORDINARY SLICING
print(success[0:5])

#ADVANCED SLICING
print(success[::])          #[::]=first is by default 0;
                            #second is by default the whole length of the string;
                            #third one is by default 1. basically it is used to skip characters

#a greater way to REVERSE A STRING
print(success[::-1])                            


#some functions in string

print(success.isalpha())                       #shows the string is alpha or not
print(success.isalnum())                       #shows the string is alpha numeric or not
print(success.endswith('SKILLSANTA'))          #checks the endpoint
print(success.find('o'))                       #checks where is the character
print(success.count('o'))                      #counts the mentioned character
print(success.capitalize())                    #capitalize the first character
print(success.upper())                         #converts the whole string in to uppercase characters
print(success.replace('Sayan','kalbhairab'))   #replace

