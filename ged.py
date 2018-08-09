import Levenshtein

f_misspell = open("data/wiki_misspell.txt", "r")
f_correct = open("data/wiki_correct.txt", "r")
f_dictionary = open('data/dict.txt', 'r')

f_predict = open('data/predict_ged.txt', 'w')

m_list = f_misspell.readlines()
c_list = f_correct.readlines()
d_list = f_dictionary.readlines()

accuracy = 0.0
precision = 0.0
recall = 0.0

correct = 0

predicted_count = 0

for i in range(0, int(len(m_list) / 20)):
    m_word = m_list[i]
    min_distance = 99999
    matched = ""

    m_word = m_word.strip()
    m_word = m_word.replace(m_word, "#" + m_word + "#")

    for d_word in d_list:
        d_word = d_word.strip()
        d_word = d_word.replace(d_word, "#" + d_word + "#")

        distance = Levenshtein.distance(m_word, d_word)
        if distance < min_distance:
            min_distance = distance
            matched = d_word

    matched = matched[1:len(matched) - 1]
    # print(matched)
    f_predict.write(matched)
    f_predict.write("\n")

    if matched == c_list[i].strip():
        correct += 1
accuracy = correct / int(len(m_list) / 20)
precision = correct / int(len(m_list) / 20)
recall = correct / int(len(c_list) / 20)

print("\n====== Result ======")
print("Accuracy\t" + str(accuracy))
print("Precision\t" + str(precision))
print("Recall\t" + str(recall))

f_misspell.close()
f_correct.close()
f_dictionary.close()
f_predict.close()
