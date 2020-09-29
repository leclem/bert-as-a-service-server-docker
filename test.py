from bert_serving.client import BertClient
print("eee")
bc = BertClient("172.17.0.2")
arrayResults = bc.encode(['I am doing something', 'I am not doing it'])

from scipy import spatial
print(1-spatial.distance.cosine(arrayResults[0], arrayResults[1]))
