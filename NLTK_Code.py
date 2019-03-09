import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
nltk.download('punkt') #Опционально
nltk.download('stopwords')

text = '''
Равным образом, убежденность некоторых оппонентов однозначно фиксирует необходимость новых предложений.
Кстати,  многие известные личности призывают нас к новым свершениям, которые, в свою очередь, должны быть превращены в посмешище, хотя само их существование приносит несомненную пользу обществу.
Каждый из нас понимает очевидную вещь: убежденность некоторых оппонентов позволяет выполнить важные задания по разработке поэтапного и последовательного развития общества.
Внезапно, сделанные на базе интернет-аналитики выводы, превозмогая сложившуюся непростую экономическую ситуацию, ассоциативно распределены по отраслям.
Следует отметить, что внедрение современных методик говорит о возможностях модели развития. В целом, конечно, граница обучения кадров требует от нас анализа укрепления моральных ценностей.
'''

download_stopwords = stopwords.words('russian')
stop_text = []
tokens = word_tokenize(text)
words_amount = []
for i in tokens:
    if i not in download_stopwords and i != "," and i != "." and i != ":":
        stop_text.append(i)
for k in tokens:
    if k != "," and k != "." and k != ":":
        words_amount.append(k)
print(text)
print("Количество слов: ", len(words_amount))
print("Количество стоп-слов: ", len(words_amount) - len(stop_text), "\nИх процент в тексте: ", (len(words_amount) - len(stop_text)) / len(words_amount) * 100)
stemmer = SnowballStemmer("russian")
for token in stop_text:
    stems = stemmer.stem(token)
    if token != "":
        print(token, " : ", stems)
