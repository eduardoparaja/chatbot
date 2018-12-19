from chatterbot import ChatBot


chatbot = ChatBot(
        
        "Chatbot",
        trainer ="chatterbot.trainers.ChatterBotCorpusTrainer"
        )

chatbot.train(
        "chatterbot.corpus.english"
        )
        
while True:
    user = input(">>> ")
    response = chatbot.get_response(user)
    print("Chatbot: " + str(response))