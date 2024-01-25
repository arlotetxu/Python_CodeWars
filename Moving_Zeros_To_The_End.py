'''
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
'''
def move_zeros(lst):
	i = 0
	count = 0
	while i < len(lst):
		if lst[i] == 0:
			lst.pop(i)
			count += 1
			i = -1
		i += 1
	j = 0
	while j < count:
		lst.append(0)
		j += 1
	print(lst)
	return lst

move_zeros([0, 0, 0, 0, 0, 0, 0, 0, 0, 4])