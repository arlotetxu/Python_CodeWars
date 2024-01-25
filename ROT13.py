def rot13(str):
	ret = []

	for i in str:
		if (ord(i) >= 65 and ord(i) <= 77) or (ord(i) >= 97 and ord(i) <= 109):
			ret.append(chr(ord(i) + 13))
		elif (ord(i) >= 78 and ord(i) <= 90) or (ord(i) >= 110 and ord(i) <=
												 122):
			ret.append(chr(ord(i) - 13))
		else:
			ret.append(chr(ord(i)))
	return "".join(ret)

test = rot13("Z")
print(test)