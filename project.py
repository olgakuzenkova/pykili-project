import re, collections, sys, random

def corpus_maker():
    corpus = []
    with open('5try.csv', encoding='utf-8') as file:
        file = file.readlines()
        for line in file:
            rus = re.findall('^.*;', line)
            fin = re.findall(';.*$', line)
            context = []
            context.append(rus)
            context.append(fin)
            corpus.append(context)
    return corpus

def requesting():
    request = input('Введите слово: ')
    request = re.sub('(.*)', r' \1', request)
    request = request.lower()
    return request

def contexting(corpus, request):
    context_s = ''
    for context in corpus:
        for sentence in context:
            for word in sentence:
                if request in word:
                    context = str(context)
                    context_s = context_s + context + '\n' + '\n'
    return context_s

def bad(context_s, request):
    badwords = {' и ': ' ja ' ,' я ': ' minä ',' ты ': ' sinä ',' он ': ' hän ',' она ': ' hän ',
                ' мы ': ' me ',' вы ': ' te ',' они ': ' he ',' был ': ' oli ',' была ': ' oli ',
                ' были ': ' olivat ',' его ': ' hänellä ',' её ': ' hänellä ',' Кирила ': ' Kirila ',
                ' Петрович ': ' Petrovitsch ',' Дубровский ': ' Dubrovskij ',' Мария ': ' Maria ',
                ' Владимир ': ' Vladimir ',' но ': ' mutta ',' не ': ' ei ',' есть ': ' on ',
                ' что ': ' että ',' с ': ' kanssa ',' (не) был(а) ': ' ole ',' его ': ' hänen ',' её ': ' hänen '}
    translation = badwords.get(request)
    print('перевод: ', translation, '\n')
    context_s = context_s.split('\n')
    good_context_s = []
    for context in context_s:
        if translation in context:
            good_context_s.append(context)
    return good_context_s
            
def improver(context_s, request):
    badwords = {' и ': ' ja ' ,' я ': ' minä ',' ты ': ' sinä ',' он ': ' hän ',' она ': ' hän ',
                ' мы ': ' me ',' вы ': ' te ',' они ': ' he ',' был ': ' oli ',' была ': ' oli ',
                ' были ': ' olivat ',' его ': ' hänellä ',' её ': ' hänellä ',' Кирила ': ' Kirila ',
                ' Петрович ': ' Petrovitsch ',' Дубровский ': ' Dubrovskij ',' Мария ': ' Maria ',
                ' Владимир ': ' Vladimir ',' но ': ' mutta ',' не ': ' ei ',' есть ': ' on ',
                ' что ': ' että ',' с ': ' kanssa ',' (не) был(а) ': ' ole ',' его ': ' hänen ',' её ': ' hänen '}
    all_fin_words = re.findall('[a-zA-ZäöÄÖ]+', context_s)
    bad_fin_words = badwords.values()
    fin_words = []
    for word in all_fin_words:
        word = word.lower()
        word = re.sub('(.*)', ' \\1', word)
        if not word in bad_fin_words:
            fin_words.append(word)
    topwords = collections.Counter(fin_words)
    top = collections.defaultdict(list)
    for word, freq in topwords.items():
        top[freq].append(word)
    dict(top)
    freq_s = list(top.keys())
    freq_s.sort()
    freq_s.reverse()
    freq_s = freq_s[0:4]
    top5words = []
    for i in freq_s:
        top5words.append(top[i])
        print(i, ':', top[i])
    top5words = str(top5words)
    top5words = re.findall('[\wöäÖÄ]+', top5words)        
    context_s = context_s.split('\n')
    good_context_s = []
    for context in context_s:
        for word in top5words:
            if word in context:
                if not context in good_context_s:
                     good_context_s.append(context)
    
    return good_context_s

def printer(good_context_s):
    if len(good_context_s) > 10:
        context_s_toprint = random.choices(good_context_s, k=10)
    else:
        context_s_toprint = good_context_s
    answer = []
    for one in context_s_toprint:
        one = str(one)
        one = re.sub('\[\[[\'\"](.*)\;[\'\"]\]\, \[[\'\"]\;(.*)[\'\"]\]\]', '\\1 \n \\2\n\n', one)
        answer.append(one)
    return answer

def main():
    corpus = corpus_maker()
    request = requesting()
    context_s = contexting(corpus, request)
    if len(context_s) == 0:
        sys.exit('Результатов не найдено')
    badwords = {' и ': ' ja ' ,' я ': ' minä ',' ты ': ' sinä ',' он ': ' hän ',' она ': ' hän ',
                ' мы ': ' me ',' вы ': ' te ',' они ': ' he ',' был ': ' oli ',' была ': ' oli ',
                ' были ': ' olivat ',' его ': ' hänellä ',' её ': ' hänellä ',' Кирила ': ' Kirila ',
                ' Петрович ': ' Petrovitsch ',' Дубровский ': ' Dubrovskij ',' Мария ': ' Maria ',
                ' Владимир ': ' Vladimir ',' но ': ' mutta ',' не ': ' ei ',' есть ': ' on ',
                ' что ': ' että ',' с ': ' kanssa ',' (не) был(а) ': ' ole ',' его ': ' hänen ',' её ': ' hänen '}
    if request in badwords:
        good_context_s = bad(context_s, request)
    else:
        good_context_s = improver(context_s, request)
    answer = printer(good_context_s)
    print(answer)

if __name__ == '__main__':
    main()

#bot = telebot.Telebot('1027945505:AAFjALqO8Pi8gqaLBBweYuVbCUxCqF4RdRo')

#@bot.message_handler(commands=['start'])
#def start_message(message):
#     bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

#def send_text(request):
    

#bot.polling()




