def initials(name: str):
    word_list = name.split()
    new_names = []

    for word in word_list:
        if word == word_list[-1]:
            new_names.append(word.title())
        else:
            new_names.append(f"{word[0].upper()}")

    return ' '.join(new_names)
if __name__ == '__main__':
    print(initials('code wars'))