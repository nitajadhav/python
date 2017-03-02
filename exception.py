"try-catch-finaly"
try:
	file=open("newFile.txt","w");
	raise Exception("exception occured")
except IOError:
	print("file do not exist")
except Exception as error:
	print(error)
else:
	print("inside else")
finally:
	print("inside finally")
