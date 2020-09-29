from bert_serving.client import BertClient
print("eee")
bc = BertClient("172.17.0.2")
arrayResults = bc.encode(['Tais toi sale merde', 'Je fais la cuisine'])

from scipy import spatial
print(1-spatial.distance.cosine(arrayResults[0], arrayResults[1]))
