import re

# Function to validate email
def validate_email(email):
    # Regular expression to validate a standard email
    standardEmail = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    if standardEmail.match(email): return True
    else: return False
    
#Test cases
print(validate_email('joao.oliveira2@example.pt'))#True
print(validate_email('@fakemail.com'))#False
print(validate_email('joao.oliveira2example.pt'))#False
print(validate_email('joao.oliveira2@examplept'))#False