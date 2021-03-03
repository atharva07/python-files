import json

people_string = '''
{
    "people": [
        {
            "name": "Atharva Hiwase",
            "phone": "8408902778",
            "emails": ["atharva.hiwase07@gmail.com", "atharvahiwase@gmail.com"],
            "has_license":  false
        },
        {
            "name": "Rahul Sharma",
            "phone": "8983022267",
            "emails": null,
            "has_license":  true
        }
    ]
}
'''

data = json.loads(people_string)
print(type(data))

# to print data in loop
for person in data['people']:
    print(person['name'])

for person in data['people']:
    del person['phone']

new_string = json.dumps(data, sort_keys=True)
print(new_string)

