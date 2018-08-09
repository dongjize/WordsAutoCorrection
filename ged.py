
misspell = open("wiki_misspell.txt", "r")
rectified = open("wiki_misspell.txt", "w")

for word in misspell:

    pass


# def system_GED():
#     # Step 1:
#     pNames = f1.readlines()
#     lNames = f2.readlines()
#
#     # Step 2:
#     for pName in pNames:
#         dis = 1000000
#         matchName = ''
#
#         index = pName.find('\t')
#         pName = pName[0:index]
#         pName = pName.lower()
#         print
#         pName,
#         for lName in lNames:
#             index = lName.find('\n')
#             lName = lName[0:index]
#             disTemp = Levenshtein.distance(lName, pName)
#             if disTemp < dis:
#                 dis = disTemp
#                 matchName = lName
#         print
#         "\t" + matchName
#
#         # Step 3:
#         f4.write(pName + "\t" + matchName + "\n")
#     f4.close()