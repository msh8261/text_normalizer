import requests
import json


# input_data =  {'body': ["US unveils world's most powerful supercomputer, beats China. ", 
#                "The US has unveiled the world's most powerful supercomputer called 'Summit', " ,
#                "beating the previous record-holder China's Sunway TaihuLight. With a peak performance ",
#                "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, ",
#                "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, ",
#                "which reportedly take up the size of two tennis courts."]
#         }

input_data =  {"body": ['The sky is blue and beautiful.',
                  'Love this blue and beautiful sky!',
                  'The quick brown fox jumps over the lazy dog.',
                  "A king's breakfast has sausages, ham, bacon, eggs, toast and beans",
                  'I love green eggs, ham, sausages and bacon!',
                  'The brown fox is quick and the blue dog is lazy!',
                  'The sky is very blue and the sky is very beautiful today',
                  'The dog is lazy but the brown fox is quick!'    
            ]
        }


# url = "https://y5umgtbrt0.execute-api.us-east-2.amazonaws.com/dev/normalize"


url = "https://q0cl1wwzb7.execute-api.us-east-2.amazonaws.com/dev/spacy"

# url = "https://y5umgtbrt0.execute-api.us-east-2.amazonaws.com/dev/nltk"

r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())
print("result without securely key: ", r.text)


# key = {'x-api-key': 'tI95Zb3Ikr5l8jK1o3DDN4BOzFDLi13y3GYZ5uDW'}


# r = requests.post(url, json.dumps(input_data), headers=key)
# res = json.loads(r.content)
# print("result with securely key: ", res)













