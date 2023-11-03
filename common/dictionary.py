data ={
    'name':'ritesh',
    'age':'19',
    'skills':['c','c++','java']
}

print(data['name'])
print(data['age'])
print(data['skills'])
print(data['skills'][-1])


data1= {
    'report': {
        'alex':{
            'maths':[40,50,23],
            'science':[76,34,45]
            },
            'ashish':{
               'maths':[34,67,98,56],
               'science':[45,97,57]
            }
    }
}
print(data1['report']['alex'])
print(data1['report']['ashish'])
print(sum(data1['report']['alex']['maths']))