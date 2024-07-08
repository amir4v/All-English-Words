import nltk
from nltk.corpus import wordnet

# Ensure you have the necessary data
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_synonyms_antonyms(word, n=10):
    definition = None
    synonyms = []
    antonyms = []
    
    for syn in wordnet.synsets(word):
        # Get definition of the word
        if not definition:
            definition = syn.definition()
        
        for lemma in syn.lemmas():
            if lemma.name().lower() != word.lower():
                synonyms.append(lemma.name())
            if lemma.antonyms():
                antonyms.append(lemma.antonyms()[0].name())
        
        # Only need n unique synonyms and antonyms
        if len(synonyms) >= n and len(antonyms) >= n:
            break
    
    # Ensure we only return n unique synonyms and antonyms
    synonyms = list(set(synonyms))[:n]
    antonyms = list(set(antonyms))[:n]
    
    return {
        'word': word,
        'definition': definition,
        'synonyms': synonyms,
        'antonyms': antonyms,
    }
