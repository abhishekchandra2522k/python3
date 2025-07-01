### Adding a user in CentOS (RPM Based) and giving it sudoers privilege to execute commands without asking password.

useradd devops
passwd devops
<set password>

add in sudoers file - $ visudo
Line 100 -
devops ALL=(ALL) NOPASSWD: ALL

vim /etc/ssh/sshd_config

remove the # from PasswordAuthentication Yes

- restart ssh service
  systemctl restart sshd

### To connect one VM to the other

Check the IP address of the provisioned VMs

- cat /vargant/Vagrantfile

add in local hosts file
vim /etc/hosts

<ip-address of web01> web01
<ip-address of web02> web02

To generate a SSH key

ssh-keygen

To attach the public key to the VM
ssh-copy-id devops@web01

> enter the password

### To run the fab python file functions in another VM (host)

-- Fabric will use the private key to login in the host VM with <username>, where public key was stored.

$ fab -H <hostname> -u <username> <function_name>

-- We can get the <function_name> from fab -l

$ fab -H web01 -u devops remote_exec

### PYTHON FABRIC DEMO PROGRAM

- Install httpd web package & dependencies
- Start and Enable web service
- Download website artifact from tooplate.com
- Extract the artifact (zip file) content into /var/www/html
- Restart the service
- We can access the website VM's IP or EC2 Instance's IP address

$ fab -H web01 -u devops web_setup:https://www.tooplate.com/zip-templates/2136_kool_form_pack.zip,2136_kool_form_pack
