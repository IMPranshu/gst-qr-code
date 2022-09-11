import json
import qrcode



# Python program to read
# json file


# Opening JSON file
f = open('SampleJson.json')

# returns JSON object as
# a dictionary
data = json.load(f)
# print(data["SignedQRCode"])

# Iterating through the json
# list
for i in data:
	print(i)

# Closing file
f.close()


img=qrcode.make(data["SignedQRCode"])
img.save("qrpic.png")