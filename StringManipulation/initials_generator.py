def generate_initials(name): return ''.join([name[0].upper() for name in name.split()])

print(generate_initials('João Sliveira'))