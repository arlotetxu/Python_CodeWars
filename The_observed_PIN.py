'''
DESCRIPTION:
Alright, detective, one of our colleagues successfully observed our target
person, Robby the robber. We followed him to a secret warehouse, where we
assume to find all the stolen stuff. The door to this warehouse is secured
by an electronic combination lock. Unfortunately our spy isn't sure about
the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits
he saw could actually be another adjacent digit (horizontally or vertically,
but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited
amount of wrong PINs, they never finally lock the system or sound the alarm.
That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering
the adjacent digits

Can you help us to find all those variations? It would be nice to have a function,
that returns an array (or a list in Java/Kotlin and C#) of all variations for an
observed PIN with a length of 1 to 8 digits. We could name the function getPINs
(get_pins in python, GetPINs in C#). But please note that all PINs, the observed
one and also the results, must be strings, because of potentially leading '0's.
We already prepared some test cases for you.
Detective, we are counting on you!
'''

def get_pins(observed):

    if observed == '':
        return []

    digit_map = {
      '1' : ['2', '4'],
      '2' : ['1', '3', '5'],
      '3' : ['2', '6'],
      '4' : ['1', '5', '7'],
      '5' : ['2', '4', '6', '8'],
      '6' : ['3', '5', '9'],
      '7' : ['4', '8'],
      '8' : ['5', '7', '9', '0'],
      '9' : ['6', '8'],
      '0' : ['8']
    }

    Q = [observed[0]]
    print(f"Q_start: {Q}")
    Q.extend(digit_map[observed[0]])
    print(f"Q_finish: {Q}")

    res = []


    while len(Q) != 0:

        cur = Q.pop()
        if len(cur) < len(observed):
            Q.append(cur + observed[len(cur)])
            for char in digit_map[observed[len(cur)]]:
                Q.extend([cur + char])
            #Q.extend([cur + char for char in digit_map[observed[len(cur)]]])
        else:
            res.append(cur)

    return res

res = get_pins('123')
print(res)
'''
PIN: 11: ['11', '11', '12', '14', '21', '41'] 
should equal ['11', '12', '14', '21', '22', '24', '41', '42', '44']
PIN: 369: ['269', '339', '359', '366', '368', '369', '369', '369', '399', '669'] 
should equal ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296',
'298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396',
'398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696',
'698', '699']
'''