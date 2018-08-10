import fuzzy
import Levenshtein

# f_misspell = open("data/wiki_misspell.txt", "r")
f_misspell = open("data/birkbeck_misspell.txt", "r")
f_correct = open("data/birkbeck_correct.txt", "r")
# f_correct = open("data/wiki_correct.txt", "r")
f_dictionary = open('data/dict.txt', 'r')

f_predict = open('data/predict_soundex.txt', 'w')

m_list = f_misspell.readlines()
c_list = f_correct.readlines()
d_list = f_dictionary.readlines()

precision = 0.0
recall = 0.0

predict_list = []

soundex = fuzzy.Soundex(4)

for m_word in m_list[0: int(len(m_list) / 20)]:
    min_distance = 99999

    candidates = []

    m_word = m_word.strip()
    m_sdx = soundex(m_word)

    temp_list = []

    for d_word in d_list:
        d_word = d_word.strip()

        d_sdx = soundex(d_word)

        if m_sdx == d_sdx:
            temp_list.append(d_word)

    if len(temp_list) == 0:
        for d_word in d_list:
            distance = Levenshtein.distance(m_word, d_word)
            if distance == min_distance:
                candidates.append(d_word)

            elif distance < min_distance:
                min_distance = distance
                candidates.clear()
                candidates.append(d_word)
    else:
        for candidate in temp_list:
            distance = Levenshtein.distance(m_word, candidate)
            if distance > 0:
                if distance == min_distance:
                    candidates.append(candidate)
                elif distance < min_distance:
                    min_distance = distance
                    candidates.clear()
                    candidates.append(candidate)

    f_predict.write(str(candidates))
    f_predict.write("\n")

    predict_list.append(candidates)

predict_count = 0
correct_count = 0

for i in range(0, int(len(c_list) / 20)):
    c_list[i] = c_list[i].strip()
    c_word = c_list[i]

    if c_word in predict_list[i]:
        correct_count += 1

for p in predict_list:
    predict_count += len(p)

precision = round(correct_count / predict_count, 4)
recall = round(correct_count / int(len(c_list) / 20), 4)

print("\n====== Soundex Result ======")
print("Precision\t" + str(precision))
print("Recall\t" + str(recall))

f_misspell.close()
f_correct.close()
f_dictionary.close()
f_predict.close()
