import Levenshtein

# f_misspell = open("data/wiki_misspell.txt", "r")
f_misspell = open("data/birkbeck_misspell.txt", "r")
# f_correct = open("data/wiki_correct.txt", "r")
f_correct = open("data/birkbeck_correct.txt", "r")

m_list = f_misspell.readlines()
c_list = f_correct.readlines()

operations = []

for i in range(0, len(m_list)):
    m_word = m_list[i]
    m_word = m_word.strip()
    c_word = c_list[i]
    c_word = c_word.strip()
    ops_list = Levenshtein.editops(c_word, m_word)
    ops = [op[0] for op in ops_list]
    if ops == ['replace', 'replace']:
        ops = 'disposition'
    elif len(ops) > 1:
        ops = 'multiple'
    else:
        ops = ops[0]
    operations.append(ops)
print("insert\t" + str(operations.count('insert')) + "\t" + str(round(operations.count('insert') / len(m_list), 4)))
print("delete\t" + str(operations.count('delete')) + "\t" + str(round(operations.count('delete') / len(m_list), 4)))
print("disposition\t" + str(operations.count('disposition')) + "\t" +
      str(round(operations.count('disposition') / len(m_list), 4)))
print("substitution\t" + str(operations.count('replace')) + "\t" +
      str(round(operations.count('replace') / len(m_list), 4)))
print("multiple\t" + str(operations.count('multiple')) + "\t" +
      str(round(operations.count('multiple') / len(m_list), 4)))
