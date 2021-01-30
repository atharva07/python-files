# function to return all uncommon words
def UncommonWords(A,B):

    # count will contain all word counts
    count = {}

    # insert word of string A into hash
    for word in A.split():
        count[word] = count.get(word, 0) + 1

    # insert word of string B into hash
    for word in B.split():
        count[word] = count.get(word, 0) + 1

    return[word for word in count if count[word] == 1]

A = "Geeks for Geeks"
B = "Geeks for Geeks is awesome"

print(UncommonWords(A,B))