names = ['Ravi','Pankaj','Karan','Ram']
surnames = ['Gill','Chand','Dhillon','Parkash']
mydict = {name:surname for name,surname in zip(names,surnames) if name!='Ram'}
print(mydict['Ravi'])
if mydict['Ravi']=='Gill':
    raise ValueError("Ravi must be Jag")

