import vk_api
import time
import sys
import nltk
from nltk.tokenize import word_tokenize
import pymorphy2
from nltk.corpus import stopwords

nltk.download('stopwords')

session = vk_api.VkApi(token = '00d582e400d582e400d582e4bb00bcb620000d500d582e45c53c88eaaab6f6509e2b1a7')

vk = session.get_api()
offset = 0

posts = ''

c = 0
text_raw = ""
for i in range(0 ,2):

    data = vk.wall.get(domain = 'bugurt_thread' ,count=50, offset=offset)

    offset += 50

    for i in data['items']:

        text_raw += i['text'] + " "

        c += 1

    time.sleep(20)

sw_ru = set(stopwords.words('russian'))
token_text = word_tokenize(text_raw)
morph = pymorphy2.MorphAnalyzer()
res_text = []
for word in token_text:
    if word not in sw_ru:
        res_text.append(word)
count = {}
for word in res_text:
    cur = morph.parse(word)[0]
    result = cur.normalized
    if result[0] not in count:
        count.update({result[0]: 1})
    else:
        count[result[0]] += 1
text2 = open("Бугуртный_частотник.txt", "w", encoding = "utf=8")
for key in sorted(count, key = count.get):
    text2.write(str(key) + " " + str(count[key]) + "\n")
