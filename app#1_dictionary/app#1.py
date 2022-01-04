import json
from difflib import get_close_matches

data = json.load(open('data.json'))

while True:

    def translator(w):
        if w in data:
            return data[w]
        elif w.title() in data:
            return data[w.title()]
        elif w.upper() in data:
            return data[w.upper()]
        elif len(get_close_matches(w, data.keys())) > 0:
            misfit = input(f'Probably you meant {get_close_matches(w, data.keys())[0]}?'
                           f' Press Y if yes or N if no. Thanks ')
            while True:
                if misfit == 'y':
                    return data[get_close_matches(w, data.keys())[0]]
                elif misfit == 'n':
                    return "Please double check the word"
                else:
                    return "You haven't chosen an option given"
        else:
            return "The word doesn't exist"

    word = input("Please enter your word: ")

    output = translator(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)