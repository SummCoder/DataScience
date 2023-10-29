import nltk
import synonyms


def inputEDA(date):
    Date1 = date
    Keywords = synonyms.keywords(date, topK=1000)
    Nearby = []
    for i in range(len(Keywords)):
        synlst = synonyms.nearby(Keywords[i])
        if len(synlst[0]) != 0 and len(synlst[0]) != 1:
            Nearby.append(synlst[0][1])
        else:
            Nearby.append(Keywords[i])

    for i in range(len(Keywords)):
        if Keywords[i] in date:
            date = date.replace(Keywords[i], Nearby[i])
    BleuScore = nltk.translate.bleu_score.sentence_bleu([Date1], date)
    return date, BleuScore
