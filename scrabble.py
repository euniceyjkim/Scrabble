from wordscore import score_word

#open sowpods.txt
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    data = [i.lower() for i in data]

#create run_scrabble
def run_scrabble(rack):
    '''Go through each letter in sowpods. If letter also in rack, add a count and remove that letter from the rack.'''
    valid_words = []
    wildcard = rack.count("*") + rack.count("?")

    for i in rack:
        if i in "0123456789":
            return "No #."
        elif i.lower() not in "abcdefghijklmnopqrstuvwxyz?*":
            return "No invalid characters."
    if len(rack) > 7 or len(rack) < 2:
        return "Rack length is btwn 2-7 characters."
    elif len(rack) == 0:
        return "Empty rack."
    elif wildcard > 2:
        return "No more than 2 wildcards."

    else:
        for word in data:
            listrack = list(rack.lower())
            count = 0
            for char in word:
                if char in listrack:
                    count += 1
                    listrack.remove(char)
                elif "*" in listrack:
                    count += 1
                    listrack.remove("*")
                elif "?" in listrack:
                    count += 1
                    listrack.remove("?")
                else:
                    break
                if len(word) == count:
                    valid_words.append(word.lower())

        scores = []
        from operator import itemgetter
        for word in valid_words:
            scores.append([score_word(word, rack), word.upper()])
        scores = sorted(scores, key = itemgetter(0), reverse = True)
        tuples = [tuple(x) for x in scores]

        return tuples, len(valid_words)