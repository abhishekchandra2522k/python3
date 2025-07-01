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

def remote_exec():
    run("hostname")
    run("uptime")
    run("df -h")
    run("free -m")

    sudo("yum install unzip zip wget -y")

def web_setup(WEBURL, DIRNAME):
    print("#####################################################")
    print("Installing Dependencies")
    print("#####################################################")
    sudo("yum install httpd wget unzip -y")

    print("#####################################################")
    print("Start & enable service")
    print("#####################################################")
    sudo("systemctl start httpd")
    sudo("systemctl enable httpd")

    print("#####################################################")
    local("apt install zip unzip -y")

    print("#####################################################")
    print("Downloading and pushing website to webservers")
    print("#####################################################")
    local(("wget -O website.zip %s") % WEBURL)
    local(("unzip -o website.zip"))

    print("#####################################################")
    with lcd(DIRNAME): # local cd to DIRNAME
        local("zip -r tooplate.zip * ") # zip everything in that folder to tooplate.zip
        put("tooplate.zip", "/var/www/html/", use_sudo=True)
        
    with cd("/var/www/html/"):
        sudo("unzip -o tooplate.zip")
    
    sudo("systemctl restart httpd")

    print("website setup is done")

    