# write a function called extract_email_address that takes 
# comma-delimited string as an argument -- where the email is the
# last item listed -- and returns a string of just the email address:

def extract_email_address(line):
    return line.split(',')[-1]

print(extract_email_address('John,Doe,Jr.,john_doe@gmail.com'))
print(extract_email_address('Ana,Hernandez,ahernandez@yahoo.com'))
print(extract_email_address('Dr.,Jasmin,Carter,III.,jcarter@northwestern.edu'))
