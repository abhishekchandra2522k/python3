# Slicing String
planet = "Closest to Sun"
print(planet)
print(planet[:7])
print(planet[8:10])
print(planet[-3:])

# Slicing a Tuple
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible")

print(devops[0])
print(devops[4])
print(devops[-1])

# increasing the slicing levels
print(devops[2:5])
print(devops[2:5][0])
print(devops[2:5][0][5:11])
print(devops[2:5][0][5:11][-1])

# Slicing a List
devops1 = ["Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python", "Ansible"]

print(devops1[0])
print(devops1[4])
print(devops1[-1])

# increasing the slicing levels
print(devops1[2:5])
print(devops1[2:5][0])
print(devops1[2:5][0][5:11])
print(devops1[2:5][0][5:11][-1])

# Slicing a Dictionary

skills = {"DevOps":("AWS", "Jenkins", "Python", "Ansible"), "Development":["Java", "NodeJS", ".NET"]}
print(skills)
print(skills["DevOps"])
print(skills["DevOps"][1:2])
print(skills["Development"][-1])