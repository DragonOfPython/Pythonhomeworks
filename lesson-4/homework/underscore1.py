def underscore(stringi):
    len1 = len(stringi)
    vowels = "ieoua"
    newstring = ''
    underscore = []
    for i in range(len1):
        underscore.append(stringi[i])

        if (i+1) % 3 == 0 and i != len1 - 1:
            if stringi[i] not in vowels:
                underscore.append("_")
            elif i < len1 - 1 and stringi[i] not in vowels:
                    underscore.append("_")
            elif stringi[:i+1] == stringi[:i]:
                underscore.append("_")

    result = newstring.join(underscore)

    return result

string1 = 'hello'
string_underscore = underscore(string1)
print(string_underscore)

string2 = 'assalom'
string_underscore = underscore(string2)
print(string_underscore)

string3 = 'abcabcdabcdeabcdefabcdefg'
string_underscore = underscore(string3)
print(string_underscore)

string4 = "salomssshishakhinaaamocceeeanmhcdop"
string_underscore = underscore(string4)
print(string_underscore)

