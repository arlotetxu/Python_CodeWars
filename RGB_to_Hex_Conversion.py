'''
The rgb function is incomplete. Complete it so that passing in RGB decimal
values will result in a hexadecimal representation being returned. Valid decimal
values for RGB are 0 - 255. Any values that fall out of that range must be
rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will
not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"

'''
def	to_hexa(dec):
	hexa = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
			'D', 'E', 'F']
	val_hexa = []
	if dec > 255:
		dec = 255
	if dec <= 0:
		return '00'
	while int(dec) > 0:
		#val_hexa.append(hexa[int(dec % 16)])
		val_hexa.append(f"{int(dec % 16):02X}")
		dec /= 16
	val_hexa.reverse()
	ret_hexa = "".join(val_hexa)
	# if len(ret_hexa) < 2:
	# 	ret_hexa = '0' + ret_hexa
	print(val_hexa)
	print(ret_hexa)
	return ret_hexa

def rgb(r, g, b):
	ret_val = []
	ret_val.append(to_hexa(r))
	ret_val.append(to_hexa(g))
	ret_val.append(to_hexa(b))
	ret = "".join(ret_val)
	print(ret)
	return ret


rgb(6, 12, 165)
#060CA5
