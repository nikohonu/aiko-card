import nltk


def clear_text(text):
    tokens = nltk.word_tokenize(text)
    result = ""
    tags = nltk.pos_tag(tokens)
    for token, tag in tags:
        # print(token, tag)
        without_space = [",", ".", ":"]
        if tag in without_space or (len(token) > 1 and token[-1] == "-"):
            result += token
        else:
            result += " " + token
    return result.strip()
