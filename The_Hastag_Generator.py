'''
The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples

" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
'''

def tag_gen(string):
    if string == None:
        return False
    list_words = string.title().split()
    list_words_j = "#" + "".join(list_words)
    if (len(list_words_j) > 140) or (len(list_words_j) == 1):
        return False
    return list_words_j

test = tag_gen("   probando probando       ")
print(test)

