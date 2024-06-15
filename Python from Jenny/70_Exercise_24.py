# Date: 4th January 2024 Thursday
# Start Time: 11 : 44 PM

# Date: 5th January 2024 Friday
# End Time: 12 : 10 AM          Hn mein Abu nu litrrya

Info =[
    {
        'Name':'Awais',
        'age':22,
        'degree':"B.S"
    },
    {
        'Name':'Mamoon',
        'age':20,
        'degree':"C.S",
        'language':['JS', 'Python']
    }
]

def add_new_person(Name, age, degree, language):
    new_person={
        'Name':Name,
        'age':age,
        'degree':degree,
        'language':language
    }
    # Jenny Solution below
    # new_person={}
    # new_person['Name']=Name
    # new_person['age']=age
    # new_person['degree']=degree
    # new_person['language']=language

    Info.append(new_person)
    
add_new_person("Taimur", 15, 'No', "JS")

print(Info)
print(Info[1]['language'])
