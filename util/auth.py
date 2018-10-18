USER = "KateLin"
PASS = "verysecurepassword123!"

#CHECK INTO DATABASE TABLE
def checkInfo(user,pswd):
    if(user == USER and pswd == PASS):
        return "Login Successful"
    elif(user != USER):
        return "ERROR: Invalid Username"
    else:
        return "ERROR: Invalid Password"
