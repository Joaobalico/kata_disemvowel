# Trolls are attacking your comment section!

# A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

# Your task is to write a function that takes a string and return a new string with all vowels removed.

# For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

# Note: for this kata y isn't considered a vowel.

def disemvowel(string_):
    vowels = [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]
    list_from_str = list(string_)

    for i in list_from_str:
        if ord(i) in vowels:
            list_from_str.remove(i)
            for i in list_from_str:
                if ord(i) in vowels:
                    list_from_str.remove(i)
    str_from_list= ''.join(list_from_str)
    return print(str_from_list)




disemvowel("This websitetU is for losers LOL!") #"Ths wbst s fr lsrs LL!"
disemvowel("Your No offense but, Your writing is among the worst I've ever read") #"Ths wbst s fr lsrs LL!"