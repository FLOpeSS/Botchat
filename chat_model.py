from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer


class Model:
    def __init__(self):
        self.chatbot = ChatBot(
            "Ron obvious",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                'chatterbot.logic.BestMatch'
            ],
            database_url='sqlite:///database.sqlite3'
            )

        self.trainer = ChatterBotCorpusTrainer(self.chatbot)
        self.trained = ListTrainer(self.chatbot)

    # A method to train using your own words, by using train("Your words")
    def trained(self):
        self.trained


    def trainer_english(self):
        self.trainer.train(
            "chatterbot.corpus.english",
            "chatterbot.copurt.english.conversations",
            "chatterbot.copurt.english.greetings",            
            )


