"CRUD on list"
list=["nita",100,"Pune","capgemini"]

#Read
print(list)

#create
list.append("Java")
print("after appending",list)

#insert
list.insert(1,"smita")
print("after inserting smita at first index:",list)


#update
list[4]="python";
print("after updation:",list)

#update -by remove


#delete
list.pop(3)
print("after popping:",list)


#delete by remove
list.remove('smita')
print("after removing 2nd element:",list)


#Delete by del
del list[2]
print("after deleting first element", list)



