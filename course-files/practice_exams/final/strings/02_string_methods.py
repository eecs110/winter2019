# write a function called extract_email_address that takes 
# comma-delimited string as a positional argument -- where the email is the
# last item listed -- and returns a string that just contains the email address:
# Below, I show how I would call your function and what it would 
# output to the screen.

def extract_email_address(line):
    return line.split(',')[-1]

print(extract_email_address('John,Doe,Jr.,john_doe@gmail.com'))
print(extract_email_address('Ana,Hernandez,ahernandez@yahoo.com'))
print(extract_email_address('Dr.,Jasmin,Carter,III.,jcarter@northwestern.edu'))
# john_doe@gmail.com
# ahernandez@yahoo.com
# jcarter@northwestern.edu