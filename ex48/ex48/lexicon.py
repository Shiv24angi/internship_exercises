# ex48/lexicon.py

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(sentence):
    directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verbs = ['go', 'stop', 'kill', 'eat']
    stops = ['the', 'in', 'of', 'from', 'at', 'it']
    nouns = ['door', 'bear', 'princess', 'cabinet']

    words = sentence.split()
    result = []

    for word in words:
        word_lower = word.lower()

        if word_lower in directions:
            result.append(('direction', word_lower))
        elif word_lower in verbs:
            result.append(('verb', word_lower))
        elif word_lower in stops:
            result.append(('stop', word_lower))
        elif word_lower in nouns:
            result.append(('noun', word_lower))
        else:
            number = convert_number(word_lower)
            if number is not None:
                result.append(('number', number))
            else:
                result.append(('error', word_lower))

    return result
