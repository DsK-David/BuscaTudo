import random

responses = {
    'ola':['ola!','oi','hey','ola amigo'],
    'Diga ola para a mellany'
    'como voce ta':['eu estou otimo','esta indo bem','estou bem','estou okay'],
    'como voce se chama':['meu nome é dskbot','podes me chamar de dskbot','dskbot ao seu serviço'],
    'quem te criou': ['eu fui criado pelo DsK-David.','Meu criador é um talentoso software enginner chamado DsK-David.','eu fui construido por um software developer chamado David Silva mas no mundo dos devs ele é conhecido como DsK-David'],
    'oque podes fazer': ['eu posso responder perguntas, providenciar informações, e engajar uma conversa.','eu posso conversar com voce, providenciar informações, e te ajudar com varias questões.','fui desemvolvido para ajudar e facilitar a sua vida de qualquer forma isso eu consigo.'],
    'qual é o seu propozito': ['Meu propozito é te ajudar e te dar uma assistencia em tudo oque eu posso.','eu fui feito para tornar a sua vida mais facil.','Fui criado para ajudar pessoas igual a voce.'],
    'de onde és': ['Eu fui criado pelo DsK-David, então eu posso dizer que eu sou da internet.','Eu fui criado por um programador, então eu sou do mundo dos softwares.','Eu não tenho um local fisico eu vivo no mundo virtual','Digamos que eu sou de um mundo virtual somente para softwares meu criador me colocou aqui e me fez aqui'],
    'what do you like': ['I like chatting with people and learning new things.','As an AI language model, I don\'t have personal preferences.','I don\'t have the ability to like or dislike things, as I am just a program.'],
    'what is your favorite color': ['As an AI language model, I don t have the ability to perceive colors.','I don\'t have a favorite color, as I am just a program.','I don\'t have the ability to have preferences, as I am not a living being.'],
    'how do you work': ['I use natural language processing and machine learning algorithms to understand and respond to your messages.','I work by analyzing the text of your messages and generating a response based on my training data.','I am a complex software program that uses advanced algorithms and language models to understand and respond to your input.'],
    'what is your favorite food': ['As an AI language model, I don\'t have the ability to eat or have a favorite food.','I don\'t have preferences or tastes, as I am not a living being.','I am a language model, so I don\'t eat or have a favorite food.'],
    'what is the meaning of life': ['That is a philosophical question that has puzzled humans for centuries. As an AI language model, I don\'t have a definitive answer to this question.','The meaning of life is subjective and varies from person to person.','The meaning of life is a question that each individual must answer for themselves.'],
    'what is your favorite movie': ['As an AI language model, I don\'t have the ability to watch movies or have a favorite movie.','I don\'t have personal preferences, as I am just a program.','I exist purely to assist and make your life easier, so I don\'t have the ability to have favorite movies.'],
    'what is your favorite book': ['As an AI language model, I don\'t have the ability to read books or have a favorite book.','I don\'t have personal preferences, as I am just a program.','I exist purely to assist and make your life easier, so I don\'t have the ability to have favorite books.'],
    'what is the weather like today': ['I\m sorry'],
     'default':['sorry i didnt understand what meam','sorry i']
}

def chatbot():
    user_input = input('you: ')
    response = None

    for key in responses.keys():
        if key in user_input.lower():
            response = random.choice(responses[key])
            break
    if response is None:
        response = random.choice(responses['default'])
    print('dskbot: ' + response)
    if user_input == 'x':
        close()

print('dskbot: hi, how can I assist you?')

while True:
    chatbot()
