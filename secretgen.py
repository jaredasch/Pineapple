import os
file = open("secret.txt","w")
file.write(str(os.urandom(32)))
