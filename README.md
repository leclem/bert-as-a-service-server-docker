# bert-as-a-service-server-docker
Simple server of Bert-As-A-Service with a multilingual BERT model allowing to transform non-fixed size sentences in fixed-size vectors

I will make run a simple docker image of the server of Bert as a service on a cpu : https://github.com/hanxiao/bert-as-service

Usage : 
Download the BERT-Base, Multilingual Cased model supporting 104 languages, 12-layer, 768-hidden, 12-heads, 110M parameters and unzip it in the "model" folder  https://storage.googleapis.com/bert_models/2018_11_23/multi_cased_L-12_H-768_A-12.zip
Run `docker build -t bert-server -f ./DOCKERFILE .`
Run the docker anywhere :)

For local testing : 
⋅⋅⋅ `docker run -dit -p 5555:5555 -p 5556:5556 bert-server` #Runs the server container
⋅⋅⋅ `pip3 install -U bert-serving-client scikit` #Install libraries
⋅⋅⋅ `python3 test.py`#Run the client side and compare two strings that you can modify in the script

or 

⋅⋅⋅ `docker run -dit -p 8125:8125 bert-server` #Runs the server container
⋅⋅⋅ `curl -X POST http://localhost:8125/encode \
  -H 'content-type: application/json' \
  -d '{"id": 123,"texts": ["hello world"], "is_tokenized": false}'`

You can also download another model from https://github.com/google-research/bert
