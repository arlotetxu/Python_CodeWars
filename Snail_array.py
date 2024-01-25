'''
Given an n x n array, return the array elements arranged from outermost
elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array
consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]
This image will illustrate things more clearly:


NOTE: The idea is not sort the elements from the lowest value to the highest;
the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array
[[]].
'''

'''
def get_up(arr, ret):
	i = 0
	while i < len(arr[0]):
		ret.append(arr[0][i])
		i += 1
	del arr[0]
	return ret

def get_right(arr, ret):
	len_x = len(arr[0])
	len_y = len(arr)
	i = 0
	while i < len_y:
		ret.append(arr[i][len_x-1])
		del arr[i][len_x-1]
		i += 1
	return ret

def get_bottom(arr, ret):
	len_x = len(arr[0])
	len_y = len(arr)
	while (len_x - 1) >= 0:
		ret.append(arr[len_y - 1][len_x - 1])
		len_x -= 1
	del arr[len_y - 1]
	return ret

def get_left(arr, ret):
	len_y = len(arr) - 1
	while (len_y) >= 0:
		ret.append(arr[len_y][0])
		del arr[len_y][0]
		len_y -= 1
	return ret


def snail_arr(snail):
	ret = []
	while snail:
		if snail:
			get_up(snail, ret)
		if snail:
			get_right(snail, ret)
		if snail:
			get_bottom(snail, ret)
		if snail:
		 get_left(snail, ret)
	return ret
'''
def snail(array):
    out = []
    while len(array):
        out += array.pop(0)
        array = list(zip(*array))[::-1] # Rotate
    return out

snail_arr = [[1, 2, 3, 4, 5, 6],
		 [7, 8, 9, 10, 11, 12],
		 [13, 14, 15, 16, 17, 18],
		 [19, 20, 21, 22, 23, 24],
		 [25, 26, 27, 28, 29, 30],
		 [31, 32, 33, 34, 35, 36]
		 ]
final = snail(snail_arr)
print(final)
print(f"len: {len(final)}")