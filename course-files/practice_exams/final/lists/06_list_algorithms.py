
def get_list_of_words_by_sentence(para):
    para = para.replace('\n', ' ')
    list_of_lists = []
    sentences = para.split('.')
    for sentence in sentences[:-1]:
        list_of_lists.append(sentence.strip().split(' '))
    return list_of_lists

paragraph = 'I love my dog. He is my friend. Today I will walk him.'

results = get_list_of_words_by_sentence(paragraph)
print(results)