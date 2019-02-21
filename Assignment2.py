def palidrome():
    original_word = input("Please enter a word ")
    original_word_no_special = special_characters_to_remove(original_word)
    reversed_word = "" 
    for x in range(len(original_word)-1, -1, -1):
        reversed_word += original_word[x]      

    reversed_word_no_special = special_characters_to_remove(reversed_word)

    if original_word_no_special == reversed_word_no_special:
        print(f"{original_word} is a palidrome")
    else:
        print(f"{original_word} is not a palidrome. The reversed word is {reversed_word}")


def special_characters_to_remove(word):
    special_characters = [" ", ".", "!", "?", ",","@","/","#", "-", "&"]
    new_word = word
    for x in special_characters:
        new_word = new_word.replace(x,"")
    return new_word.lower()


palidrome()
