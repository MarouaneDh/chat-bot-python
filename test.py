from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

# Get a response to an input statement
chatbot.get_response("Hello, how are you today?")

# import json
# with open('intents.json', 'r') as json_data:
#     intents = json.load(json_data)
# res=[]
# for intent in intents['intents']:
#     res.append({"tag":intent["intent"],  "patterns":intent["text"]   , "responses":intent["responses"]})
# res_final={"intents":res}
# # to_json= json.dumps(res_final)
# # print(to_json)
#
# with open('data.json', 'w') as outfile:
#     json.dump(res_final, outfile)