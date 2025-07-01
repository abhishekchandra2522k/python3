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

To attach the key to the VM
ssh-copy-id devops@web01

> enter the password
