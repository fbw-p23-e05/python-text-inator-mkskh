# I'm not sure that it is the most easier way to solve this task, but only this way I can solve it. Please write what do you think about my solving this task. Is it a lot of code or that's okay?

#At the start I tried to write just only with if else where I just compare last letter with list_con. But this way is not working. Or maybe it require some specific syntax ?


list_con = [ 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' ]
list_vow = ['a', 'e', 'i', 'o', 'u']

text = str(input('Enter the word: '))
last_letter = text[-1]


for letter in list_con:
    if last_letter != letter:
        pass
    elif last_letter == letter:
        print(text + 'inator', str(len(text)) + '000')

for letter in list_vow:
    if last_letter != letter:
        pass
    elif last_letter == letter:
        print(text + '-inator', str(len(text)) + '000')







