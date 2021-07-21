from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


def relevantAnswerFinderFunc(completeResponseJson, question):
    similarityArr = []

    for val, item in enumerate(completeResponseJson):
        # X = input("Enter first string: ").lower()
        # Y = input("Enter second string: ").lower()
        X = question.replace("?", "")
        Y = item['title']

        # tokenization
        X_list = word_tokenize(X)
        Y_list = word_tokenize(Y)

        # sw contains the list of stopwords
        sw = stopwords.words('english')
        l1 = [];
        l2 = []

        # remove stop words from the string
        X_set = {w for w in X_list if not w in sw}
        Y_set = {w for w in Y_list if not w in sw}

        # form a set containing keywords of both strings
        rvector = X_set.union(Y_set)
        for w in rvector:
            if w in X_set:
                l1.append(1)  # create a vector
            else:
                l1.append(0)
            if w in Y_set:
                l2.append(1)
            else:
                l2.append(0)
        c = 0

        # cosine formula
        for i in range(len(rvector)):
            c += l1[i] * l2[i]
        cosine = c / float((sum(l1) * sum(l2)) ** 0.5)
        if float(cosine) > 0:
            similarityArr.append({"i": val, "cosine": cosine})


    returnArr = []
    if len(similarityArr) == 0:
        returnArr.append({"i": 0, "cosine": 1})
        returnArr.append({"i": 1, "cosine": 0.999})
        return returnArr

    def getCos(simitem):
        return simitem.get('cosine')

    similarityArr.sort(key=getCos, reverse=True)

    if len(similarityArr) > 3:
        returnArr.append(similarityArr[0])
        returnArr.append(similarityArr[1])
        returnArr.append(similarityArr[2])
        return returnArr
    else:
        returnArr = similarityArr
        return returnArr