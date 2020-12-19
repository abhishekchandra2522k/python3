import requests

my_data = {'name' : 'Abhishek', 'email': "ab25chandra@gmail.com"}

r = requests.post('form.html', data=my_data)

f = open("./requests_form.html", "w+")

f.write()