import tweepy
import time
import random
import localdata

CONSUMER_KEY = localdata.ConsumerKey
CONSUMER_SECRET = localdata.ConsumerSecret
ACCESS_KEY = localdata.AccessKey
ACCESS_SECRET = localdata.AccessSecret

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = "last_seen_id.text"

def retrieve_last_seen_id(file_name):
    f_read = open (file_name, "r")
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id

def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, "w")
    f_write.write(str(last_seen_id))
    f_write.close()
    return

def reply_to_tweets():
    print("Recibiendo pelotudos y educándolos...")
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    listtt = ["Cuando tengas un ratito podés irte a la mierda!! Al carajo ya te fuiste... PELOTUDO!!!",
"Confirmo que sos un forro que repite lo que escriben los trolls.",
"Qué pedazo de imbécil resultaste. Pelotudo.",
"Revisá la historia. Corrés el riesgo de parecer idiota por desinformade.",
"Pelotudo y cagón que no das la cara. Sos un pobre pelotudo. Te quedó claro?",
"Te voy a dedicar el último -andá a la concha de tu madre del año-. Si serás pelotudo!!!",
"Andamos muy bien pedazo de hijo de puta",
"Qué pedazo de pelotudo resultaste. Pasaste de hacerme reír a tener pena por tu imbecilidad. Solo agradece que mi paciencia es infinita. Y rogá que tus imbéciles prepoteadas un día no se crucen con alguien sanguíneo. Seguí tu vida. Pelotudo",
"No me hagas perder el tiempo ya te he dicho que no hablo con pajeros de tu especie",
"Eras un perfecto pelotudo. Mi único error fue prestarte atención. Chau pelotudo.",
"Nada peor que un pelotudo que se cree inteligente!!! Hoy atendí PELOTUDOS XL como vos entre las 17 y 20 hs. Llegaste fuera de horario. Pedí turno para el próximo miércoles.",
"Pelotudo...Nada más penoso que un pelotudo que se cree inteligente",
"Vos sos un hijo de puta mayúsculo que insulta y difama desde el anonimato. Así son ustedes. Mierdas que votan a los verdugos de la gente humilde. No sos nadie. Hijo de puta",
"Lamentablemente no mostrás tu cara de imbécil...",
"Chau imbécil. Atenete a las consecuencias de los difamadores",
"Nada hay más penoso que un idiota que habla sin saber. No te hagas el vivo... de boludo venías bastante bien.",
"Volvé el día que dejes de hablar como un imbécil. es muy fácil denostar aquí. Este es un lugar en el que los idiotas se creen inteligentes. Es tu caso.",
"Ay Dios... qué tarado!!!",
"Pelotudos desinformados que repiten boludeces hay miles. Entre ellos vos",
"No te conozco pero cuando te presentás hablando sos horrible",
"Pajero y pelotudo... lo tuyo no tiene cura. Y no te insulto. te describo",
"Para enojarme hace falta algo más que un tarado que se cree inteligente. Volvé mañana. por hoy no atiendo más pelotudos",
"No hablés al pedo Corrés el riesgo de tener que meterte tus palabras en el culo. Te lo advierto de buen pibe que soy. Entendiste pelotudo?",
"Andamos muy bien, pedazo de hijo de puta",
"Me aburriste. Sos un pobre forro. Chau. Te bloqueo",
"Pajert... Si fuera vos no hablaría... Recordás cuántas boludeces predijiste? Callate Pajert",
"No pensaste en hacerte hervir y tomarte el caldo? Es hora de que pruebes la sopa de boludo!!!",
"Cuando tengas un ratito podés irte a la mierda!!!! Al carajo ya te fuiste... PELOTUDO!!!",
"Confirmo que sos un forro que repite lo que escriben los trolls!",
"Qué pedazo de imbécil resultaste... Pelotudo.",
"Revisá la historia... Corrés el riesgo de parecer idiota por desinformade.",
"Pelotudo y cagón que no das la cara!! Sos un pobre pelotudo. Te quedó claro?",
"Te voy a dedicar el último andá a la concha de tu madre del año. Si serás pelotudo!!!",
"Andamos muy bien pedazo de hijo de puta!",
"Qué pedazo de pelotudo resultaste... Pasaste de hacerme reír a tener pena por tu imbecilidad. Solo agradece que mi paciencia es infinita. Y rogá que tus imbéciles prepoteadas un día no se crucen con alguien sanguíneo. Seguí tu vida. Pelotudo",
"No me hagas perder el tiempo, ya te he dicho que no hablo con pajeros de tu especie",
"Eras un perfecto pelotudo... Mi único error fue prestarte atención. Chau pelotudo.",
"Nada peor que un pelotudo que se cree inteligente! Hoy atendí PELOTUDOS XL como vos entre las 17 y 20 hs. Llegaste fuera de horario. Pedí turno para el próximo miércoles.",
"Pelotudo...Nada más penoso que un pelotudo que se cree inteligente!!!",
"Vos sos un hijo de puta mayúsculo que insulta y difama desde el anonimato. Así son ustedes, mierdas que votan a los verdugos de la gente humilde. No sos nadie. Hijo de puta!!!",
"Lamentablemente no mostrás tu cara de imbécil!!!",
"Chau imbécil, atenete a las consecuencias de los difamadores",
"Nada hay más penoso que un idiota que habla sin saber... No te hagas el vivo... de boludo venías bastante bien.",
"Volvé el día que dejes de hablar como un imbécil... es muy fácil denostar aquí. Este es un lugar en el que los idiotas se creen inteligentes. Es tu caso.",
"Ay Dios... qué tarado!!!!!",
"Pelotudos desinformados que repiten boludeces hay miles, entre ellos vos",
"No te conozco pero cuando te presentás hablando sos horrible!!!",
"Pajero y pelotudo... lo tuyo no tiene cura... y no te insulto, te describo",
"Para enojarme hace falta algo más que un tarado que se cree inteligente, volvé mañana. por hoy no atiendo más pelotudos",
"No hablés al pedo... Corrés el riesgo de tener que meterte tus palabras en el culo. Te lo advierto de buen pibe que soy. Entendiste pelotudo?",
"Andamos muy bien. Pedazo de hijo de puta!!!",
"Me aburriste... sos un pobre forro. Chau; te bloqueo",
"Pajert... Si fuera vos no hablaría, recordás cuántas boludeces predijiste? Callate Pajert",
"No pensaste en hacerte hervir y tomarte el caldo?? Es hora de que pruebes la sopa de boludo",
]
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode="extended")

    for mention in reversed(mentions):
        print(str(mention.id) + " - " + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if  "#albertoputeame" in mention.full_text.lower():

            print("Pelotudo encontrado")
            print("Pelotudo puteado")
            api.update_status("@" + mention.user.screen_name + " " +
                                random.choice(listtt), mention.id)

while True:
    try:
        reply_to_tweets()
        time.sleep(30)
    except tweepy.error.TweepError:
        continue
