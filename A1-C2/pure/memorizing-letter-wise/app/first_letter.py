import string
import random

lower_chars = string.ascii_lowercase

text = f"""
"""


def mini_letterize(word, parts=3):
    if len(word) <= 0:
        return ''
    
    word = word.lower()
    word = word.title()
    
    if parts == 1 or '-' in word:
        # First Letter
        for c in lower_chars:
                word = word.replace(c, '')
    elif parts in [2, 3]:
        # Multipart
        if parts == 2:
            # Two
            word = f'{word[0]}-{word[-1]}'
        elif parts == 3:
            # Three
            mid = len(word) // 2
            word = f'{word[0]}-{word[mid]}-{word[-1]}'
    
    return word.lower()


def _letterize(text):
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.title()
    words = text.split(' ')

    results = []
    for word in words:
        word = word.replace('\n', ' ').strip(' ').strip('\n')
        org_word = word
        for c in lower_chars:
            word = word.replace(c, '')
        word = word.lower().replace('\n', ' ').strip(' ').strip('\n')
        results.append((word, org_word))
    return results


def letterize(text, separator=' ', parts=1, display=False, randomize=False):
    # separator = '\n'
    # separator = ' '
    # Separation part
    if separator == ' ':
        text = text.replace('\n', ' ')
    text = text.lower()
    text = text.title()
    if separator == ' ':
        words = text.split(separator)
    elif separator == '\n':
        words = text.split(separator)
    
    if randomize:
        random.shuffle(words)
    
    results = []
    for word in words:
        word = word.strip('\r \n')
        org_word = word
        
        if len(word) <= 0:
            continue
        
        if parts == 1:
            # First Letter
            for c in lower_chars:
                    word = word.replace(c, '')
        elif parts in [2, 3]:
            # Multipart
            if '-' in word:
                for c in lower_chars:
                    word = word.replace(c, '')
            else:
                if parts == 2:
                    # Two
                    word = f'{word[0]}-{word[-1]}'
                elif parts == 3:
                    # Three
                    mid = len(word) // 2
                    word = f'{word[0]}-{word[mid]}-{word[-1]}'
        
        word = word.lower()
        if display:
            word = f'{word} ({org_word})'
        results.append((word, org_word))
    return results
