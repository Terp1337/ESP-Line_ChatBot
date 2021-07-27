import json

#Variablen
filename = 'programming.txt'
jsonfile = 'Liste.json'
name = input("Name : ")
age = input("Alter : ")

#File öffnen
with open(filename, 'a') as file_object:
	file_object.write("\n" + "Name : " + name + " ; ")
	file_object.write("Alter : " + age )
#	file_object.write("line 1 line 2")
	
# öffnet filename
with open(filename) as file_object:
	lines = file_object.readlines()
	
pi_string =''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))

alter_unter = input("Alter bis : ")

with open(jsonfile) as f:
	data = json.load(f)
	
#print(data["Alter"])


for dic in data:
	if dic["Alter"] <= alter_unter : 
	 	json_name = dic['Name']
	 	json_alter = dic['Alter']
	 	json_mail = dic['Mail']
	 	print(json_name + ": " + json_mail + " -- " + json_alter)
