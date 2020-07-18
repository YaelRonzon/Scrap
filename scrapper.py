import requests
import bs4
from nltk.corpus import stopwords
from time import time
import operator
from functools import wraps



# def speed_test(fn):
#     def wrapper(*args, **kwargs):
#         t1 = time()
#         result = fn(*args, **kwargs)
#         end_time = time()
#         print(f"Times elapsed: {end_time-t1}")
#         return result
#     return wrapper

def scrap():
    response = requests.get("https://en.wikipedia.org/wiki/Mathematics")
    return response.text

# @speed_test
def html_formating(word_c, data):
    html = bs4.BeautifulSoup(data, 'html.parser')
    paragraphs = html.select("p")
    for para in paragraphs:
        count_words(para.text, word_c)

def remove_stopwords(s_text):
    s=set(stopwords.words('english'))
    return list(filter(lambda w: not w in s, s_text))


def count_words(s_text, word_count):
    s_text = remove_stopwords(clean_text(s_text))
    word_count = word_counting(s_text, word_count)
    

def word_counting(s_text, word_count):
    for word in s_text:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count


def clean_text(s_text):
    s_text = s_text.lower()
    s_text = s_text.replace(".", "").replace("," , "").replace("\n", "")
    return s_text.split(" ")


  


if __name__ == "__main__":
    data = scrap()
    word_count = {}
    html_formating(word_count, data)
    


# sorted_x = sorted(word_count.items(), key=operator.itemgetter(1))
# print(sorted_x)

