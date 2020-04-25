import re

corpus = []
with open('2try.csv', encoding='utf-8') as file:
    file = file.readlines()
    for line in file:
        rus = re.findall('^.*;', line)
        fin = re.findall(';.*$', line)
        context = []
        context.append(rus)
        context.append(fin)
        corpus.append(context)

    request = input('введите слово: ')
    request = re.sub('(.*)', r' \1', request)
    for context in corpus:
        for sentence in context:
            for word in sentence:
                if request in word:
                    print(request, context)
