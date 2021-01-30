# making a list of dictionary having a specific ranks
# dictionary of fortune 500 companies

dictFortune500 = {
    "wallmart": 1,
    "Exxon Mobil": 2,
    "Berkshire Hathway": 3,
    "Apple": 4,
    "AT&T": 5,
    "Amazon": 5,
    "Microsoft": 6,
    "Gerneral Motors": 7
}

def searchKeyByVal(dict,byVal):
    keysList = []
    itemsList = dict.items()
    for item in itemsList:
        if item[1] == byVal:
            keysList.append(item[0])
    return keysList

def add_key_if_does_not_exist(dict_obj,key,value):
    if key not in dict_obj:
        dictFortune500.update({key:value})
        print('company added')
        print(dictFortune500)
    else:
        print('Company already present')
        print(dictFortune500)
# get the list of companies having ranking 5
keysList = searchKeyByVal(dictFortune500,5)
add_key_if_does_not_exist(dictFortune500, 'Amazon',5)

print("fortune 500 companies are:", end="\n\n")
print(keysList)

for 
