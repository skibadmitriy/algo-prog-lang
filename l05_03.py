from fuzzywuzzy import fuzz

list = [ "я люблю спать", "Я люблю cпать!", "я люблю есть", "я не люлю есть" ]

for a in list:
    print("\"{}\" и \"{}\" похожи на {}".format(list[0], a, fuzz.ratio(list[0], a)))

'''
"я люблю спать" и "я люблю спать" похожи на 100
"я люблю спать" и "Я люблю cпать!" похожи на 81
"я люблю спать" и "я люблю есть" похожи на 88
"я люблю спать" и "я не люлю есть" похожи на 74
'''
