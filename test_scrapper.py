import pytest
import scrapper as sc

def test_word_counting_empty_dict_success():
    test_word_count = {}
    test_s_text = ["hello", "how", "are", "you", "hello"]
    expected = {"hello": 2, "how" : 1, "are":1, "you": 1}
    result = sc.word_counting(test_s_text, test_word_count)
    assert expected == result

def test_word_counting_not_empty_dict_success():
    test_word_count = {"hello": 2, "how" : 1, "are":1, "you": 1}
    test_s_text = ["hello", "you", "hello", "new"]
    expected = {"hello": 4, "how" : 1, "are": 1, "you": 2, "new": 1}
    result = sc.word_counting(test_s_text, test_word_count)
    assert expected == result

def test_remove_stopwords_sucess():
    test_s_text = ["of", "that", "math", "something"]
    expected = ["math", "something"]
    result = sc.remove_stopwords(test_s_text)
    assert expected == result

def test_clean_text_sucess():
    test_s_test = "dog. cat, bird\n"
    expected = ["dog", "cat", "bird"]
    result = sc.clean_text(test_s_test)
    assert expected == result


# def clean_text(s_text):
#     s_text = s_text.lower()
#     s_text = s_text.replace(".", "").replace("," , "").replace("\n", "")
#     return s_text.split(" ")

# def remove_stopwords(s_text):
#     s=set(stopwords.words('english'))
#     return filter(lambda w: not w in s, s_text)

    
