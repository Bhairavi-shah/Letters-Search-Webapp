def search4letters(phrase, letters):
    results = ""
    for letter in letters.lower():
        if letter in phrase.lower() and letter not in results:
            results += letter
    return(results)
