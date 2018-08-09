import nltk

f_misspell = open("data/wiki_misspell.txt", "r")
f_correct = open("data/wiki_correct.txt", "r")
f_dictionary = open('data/dict.txt', 'r')

f_predict = open('data/predict_ngram.txt', 'w')

m_list = f_misspell.readlines()
c_list = f_correct.readlines()
d_list = f_dictionary.readlines()

accuracy = 0.0
precision = 0.0
recall = 0.0

correct = 0

predicted_count = 0

for i in range(0, int(len(m_list) / 800)):
    m_word = m_list[i]
    min_distance = 99999
    matched = ""

    m_word = m_word.strip()
    m_word = m_word.replace(m_word, "#" + m_word + "#")
    m_substrings = list(nltk.bigrams(m_word))
    m_len = len(m_substrings)

    for d_word in d_list:
        d_word = d_word.strip()
        d_word = d_word.replace(d_word, "#" + d_word + "#")
        d_substrings = list(nltk.bigrams(d_word))
        d_len = len(d_substrings)

        identical_substrings = [fragment for fragment in m_substrings if fragment in d_substrings]

        distance = m_len + d_len - 2 * len(identical_substrings)
        # if dist <= min_dist:
        #     min_dist = dist
        #     matched = d_word

    min_distance =

    matched = matched[1:len(matched) - 1]
    # f_predict.write(matched)
    # f_predict.write("\n")

    # TODO record the total count of predictions

    if matched == c_list[i].strip():
        correct += 1
accuracy = correct / len(m_list)
precision = correct /
print("Accuracy\t" + str(accuracy))
print("Precision\t" + str(accuracy / len(c_list)))
print("Recall\t" + str(accuracy / len(c_list)))

f_misspell.close()
f_correct.close()
f_dictionary.close()
f_predict.close()
