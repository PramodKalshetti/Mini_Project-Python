# importing Random Modules

import random

lower= "abcdefghijklmnopqrstuvwxyz"
upper= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers= "0123456789"
sysmbols= "!@#$%^&*+-/,"

all= lower+upper+numbers+sysmbols
length = 16
password="".join(random.sample(all,length))
print(password)