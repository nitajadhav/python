"addition of list"
def addList(list):
 result=0
 for element in list:
	 result=result+element
 return result


list=[1,2,3,4]
result=addList(list)
print("result",result)