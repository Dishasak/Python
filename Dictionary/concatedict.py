dict1 = {0: 'a',1: 'b',2: 'c'}
dict2 = {3: 'd',4: 'e',5: 'f'}
dict3 = {6: 'a',7: 'g'}

concate ={**dict1, **dict2, **dict3}
print(concate)