import requests
import json


# input_data =  {'body': ["US unveils world's most powerful supercomputer, beats China. ", 
#                "The US has unveiled the world's most powerful supercomputer called 'Summit', " ,
#                "beating the previous record-holder China's Sunway TaihuLight. With a peak performance ",
#                "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, ",
#                "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, ",
#                "which reportedly take up the size of two tennis courts."]
#         }

input_data =  {"body": ["US unveils world's most powerful supercomputer, beats China. ", 
               "The US has unveiled the world's most powerful supercomputer called 'Summit', ", 
               "beating the previous record-holder China's Sunway TaihuLight. With a peak performance ",
               "of 200,000 trillion calculations per second, it is over twice as fast as Sunway TaihuLight, ",
               "which is capable of 93,000 trillion calculations per second. Summit has 4,608 servers, ",
               "which reportedly take up the size of two tennis courts." ,   
            ]
        }

url = ""




r = requests.post(url, json=input_data)
print("result without securely key: ", r.json())















