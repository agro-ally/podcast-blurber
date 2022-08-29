from listennotes import podcast_api
import json

listen_key = ''

client = podcast_api.Client(api_key=listen_key)

response = client.search(q='satanic cult',len_max=2)

j_response = response.json()

for doc in j_response['results']:
  print(doc['title_original'], doc['audio'])