import speech_recognition as sr

repeat_keywords = {'Once':1,'Double':2, 'Triple':3,
					'once':1,'double':2, 'triple':3}

def repeater(s):
    repeats = 0
    s = [ss.strip() for ss in s.split()][::-1]

    for i in range(len(s) - 1):
        if s[i - repeats + 1] in repeat_keywords:
            s[i - repeats] *= repeat_keywords[s[i - repeats + 1]]

            del s[i - repeats + 1]
            repeats += 1

    return ' '.join(s[::-1])

def writtenToSpoken():

    raw_data = input("Enter the raw data:")
    print("Abbreviations spoken :",repeater(str(r.raw_data)))
    abb = repeater(str(raw_data)
    return 

writtenToSpoken()