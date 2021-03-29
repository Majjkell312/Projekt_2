import datetime

data = datetime.datetime.now()
hours = data.hour
minutes = data.minute
print (str(hours)+":"+str(minutes))

hours = bin(hours)[2:]
minutes = bin(minutes)[2:]
print (str(hours) + ":" + str(minutes))


