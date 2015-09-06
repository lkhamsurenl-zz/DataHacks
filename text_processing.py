import os
acc = ""
# read name from argument
for file in os.listdir("/home/Development/dataHacks/data2/"):
	f = open("/home/Development/dataHacks/data2/" + file, 'r')
	text = f.read()
	f.close()
	text = text.replace("\n",'')
	text = text.replace("[",'')
	text = text.replace("]", '')
	acc = acc + text + "\n"
	# For debugging use only
	#print text
# save to this file after removing new lines, and combining them
f = open("/home/Development/dataHacks/" + "merged", 'w')
f.write(acc)
f.close()
