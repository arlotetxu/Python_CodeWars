'''
In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:

"one" => 1
"twenty" => 20
"two hundred forty-six" => 246
"seven hundred eighty-three thousand nine hundred and nineteen" => 783919
Additional Notes:

The minimum number is "zero" (inclusively)
The maximum number, which must be supported is 1 million (inclusively)
The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
All tested numbers are valid, you don't need to validate them
'''

from icecream import ic
def parse_int(string: str):
	string_1 = string.replace('-', ' ')
	string_2 = string_1.replace(' and ', ' ')
	simple = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
	          'eight', 'nine','ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
	          'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	complex = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy',
	           'eighty', 'ninety']

	numb = []
	for char in string_2.split(' '):
		if char in simple:
			numb.append(simple.index(char))
		elif char in complex:
			numb.append((complex.index(char) + 2) * 10)
		elif char == 'hundred':
			numb[-1] *= 100
		elif char == 'thousand':
			numb[-1] *= 1000
		elif char == 'million':
			numb[-1] *= 1000000
	return sum(numb)

ic(parse_int('five million one hundred thousand three-hundred and twenty-one'))
ic(parse_int('two hundred forty-six'))
ic(parse_int("twenty"))