import json
import requests


r = requests.get('http://localhost:3000')

data = r.json()
name = json.dumps(data[0]['name'])
color = json.dumps(data[0]['color'])
name1 = json.dumps(data[1]['name'])
color1 = json.dumps(data[1]['color'])
name2 = json.dumps(data[2]['name'])
color2 = json.dumps(data[2]['color'])
name3 = json.dumps(data[3]['name'])
color3 = json.dumps(data[3]['color'])

print("%s is %s" % (name, color))
print("%s is %s" % (name1, color1))
print("%s is %s" % (name2, color2))
print("%s is %s" % (name3, color3))

