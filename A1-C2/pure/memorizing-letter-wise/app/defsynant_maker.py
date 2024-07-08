from app.defsynant import get_synonyms_antonyms


def define_A1A2B1():
    words = open('A1toC2_hinted_leveled/2_level/1', 'rt').read().split('\n')
    words.remove('<->')
    words.remove('<->')
    words.remove('')
    
    defined = []
    
    for word in words:
        defined.append(get_synonyms_antonyms(word))
    
    import pickle
    pickle.dump(defined, open('1_A1A2B1_words_defined_as_dict.pickle', 'wb'))


def define_B2C1C2():
    words = open('A1toC2_hinted_leveled/2_level/2', 'rt').read().split('\n')
    words.remove('<->')
    words.remove('<->')
    words.remove('')
    
    defined = []
    
    for word in words:
        defined.append(get_synonyms_antonyms(word))
    
    import pickle
    pickle.dump(defined, open('2_B2C1C2_words_defined_as_dict.pickle', 'wb'))


# define_A1A2B1()
# define_B2C1C2()
