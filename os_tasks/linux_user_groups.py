#!/usr/bin/python3

import os

userlist = ["alpha", "beta", "gamma"]

print("Adding users to system")
print("###############################################################")

# loop to add user from userlist
for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("User {} doesnot exists. Adding it". format(user))
        print("#####################################################")
        print()
        os.system("useradd {}".format(user))
    else:
        print("User already exists, skipping it")
        print("#####################################################")
        print()

# condition to check if group exists or not, add if not exists
exitcode = os.system("grep science /etc/group")
if exitcode != 0:
    print("Group science does not exists. Adding it")
    print("#####################################################")
    print()
    os.system("groupadd science")
else:
    print("Group already exists, skipping it.")
    print("#####################################################")
    print()

for user in userlist:
    print("Adding user {} to the science group". format(user))
    print("#####################################################")
    print()

    os.system("usermod -G science {}".format(user))