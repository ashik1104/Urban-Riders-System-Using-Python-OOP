import hashlib

email = 'ashik@gmil.com'
password = 'chaironthetable'
pass_hashed = hashlib.md5(password.encode()).hexdigest()
print(pass_hashed)
