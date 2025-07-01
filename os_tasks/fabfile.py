# Python Fabric Commands

# fab -l -> to list all the available functions
# fab <function_name>:<arguments separated by comma> -> to execute the function

from fabric.api import *

def greetings(msg):
    print("Good {}".format(msg))

def system_info():
    print("Disk Space.")
    local("df -h")

    print("Memory Info.")
    local("free -m")

    print("System Uptime")
    local("uptime")