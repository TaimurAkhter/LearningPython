# Date: 25th Dec 2023 Monday
# Start Time: 10 : 17 PM

# Date: 4th January 2024 Thursday
# Time: 10 : 28 PM
# Start Time: 10 : 57 PM

Info ={
    'Awais':{'age':22, 'degree':"B.S"},
    'Mamoon':{'age':20, 'degree':"C.S"}
}
print(Info['Awais'])
print(Info['Awais']['degree'])

Info['Mamoon']['language'] = 'Angular'

print(Info['Mamoon'])
del Info['Mamoon']['language']
print(Info['Mamoon'])

# Nesting a dictionary in list
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
print(Info[0]['Name'])
print(Info[1]['language'])


# Nesting a list in dictionary
# phone = {
#     'Awais':[123, 345],
#     'Mamoon':[678, 891]
# }
# print(phone['Awais'])
# print(phone['Mamoon'][0])

# End Time: 11 : 39 PM