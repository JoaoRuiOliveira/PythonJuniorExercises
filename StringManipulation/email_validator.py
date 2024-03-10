import re

def validate_email(email):
    standardemail = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    
    if standardemail.match(email): return True
    else: return False
    
  #Test cases
print(validate_email('joao.oliveira2@exampl@e.pt'))
print(validate_email('@fakemail.com'))
print(validate_email('joao.oliveira2example.pt'))
print(validate_email('joao.oliveira2@examplept'))