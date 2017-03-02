"CRUD on dictionary"

#Create
dict={'name':'Nita', 'id':123,'city':'Pune',"number":9689947370}

#inserting with existing keys. how it will work
#$dict={'city':'Mumbai'}
#print("after inserting new city:",dict)

#update
dict['id']=456;
print("After updating id: ",dict)

#Delete
del dict['number']
print("after deleting number:", dict)

#clear
dict.clear();
print("after clearing: ",dict)