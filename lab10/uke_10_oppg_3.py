# def filter_words(words,must_include, must_exclude):
#     new_words = word_includes_all(words, must_include)
#     return (word_excludes_all(new_words, must_exclude))

# def word_includes_all(words_list, must_include):
#     included_words = []
#     for word in words_list:
#         word_set = set(word)
#         if must_include.issubset(word):
#             included_words.append(word)
#     return included_words

# def word_excludes_all(words_list, must_exclude):
#     allowed_words = []
#     for word in words_list:
#         word_set = set(word)
#         if must_exclude.issubset(word_set):
#             continue
#         else:
#             if word not in allowed_words:
#                 allowed_words.append(word)
#     return allowed_words

# forsøk 2
# hjelpefunksjon som sjekker et enkelt ord mot det som faktisk må være i det
def word_includes_all(single_word, must_include):
    # gjør om ordet til et set
    single_word = set(single_word)
    # sjekker om must_include er et subset i ordet
    if must_include.issubset(single_word):
        return True
    else:
        return False

# hjelpefunkssjon som sjekker om et ord ikke inneholder must_exclude
def word_excludes_all(single_word, must_exclude):
    # gjør ordet til et set
    single_word = set(single_word)
    # en tom liste som tar inn om must_exclude er i ordet
    value_word = []
    for x in must_exclude:
        # sjekker om exclude er i ordet
        if x in single_word:
            value_word.append(False)
        else:
            value_word.append(True)
    # sjekker om det er False i listen
    if False in value_word:
        return True
    else:
        return False

# hjelpefunksjon som legger til tillatte ord 
def words_includes_all(words, must_include):
    # tom liste som skal ta inn tillatte ord
    included_words = []
    # løper gjennom ord for ord
    for word in words:
        # kaller på den første hjelpefunksjonen 
        if word_includes_all(word, must_include):
            included_words.append(word)
    return included_words

# hjelpefunksjon som legger til ord som ikke inneholder must exclude
def words_excluded_all(words, must_exclude):
    # tom liste 
    allowed_words = []
    # sjekker ord for ord
    for word in words:
        # kaller på hjelpefunksjon 2 for å sjekke ord
        if word_excludes_all(word,must_exclude) == False:
            allowed_words.append(word)
    return allowed_words

# hovedfunksjon som filtrerer ord
def filter_words(words, must_include, must_exclude):
    # kaller på de to siste hjelpefunksjonene
    list_of_words = words_includes_all(words, must_include)
    answer = words_excluded_all(list_of_words, must_exclude)
    return answer
