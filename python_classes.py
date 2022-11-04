class Employee:
    details = {
        "experience" : 25,
        "department" : "software",
        "profession" : "engineer"
        }
    languages = ['java', 'python', 'javascript']

person_1 = Employee()
print(person_1.details['department'])
print(person_1.languages[2])
