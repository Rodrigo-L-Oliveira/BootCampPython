import random
import wikipedia
import spacy
import joblib
import datetime

# carrega o modelo de processamento de linguagem natural
nlp = spacy.load("en_core_web_sm")

# carrega o modelo de aprendizado de máquina
clf = joblib.load("modelo.pkl")

# função para responder à entrada do usuário
def responder(entrada):
    # processa a entrada do usuário com o modelo NLP
    doc = nlp(entrada)

    # extrai as características da entrada do usuário
    palavras_chave = []
    for token in doc:
        if token.is_stop:
            continue
        if token.pos_ in ["NOUN", "VERB", "ADJ"]:
            palavras_chave.append(token.text)

    # faz uma previsão com o modelo de aprendizado de máquina
    categoria = clf.predict([entrada])[0]

    # gera uma resposta com base na categoria
    if categoria == "cumprimento":
        respostas = ["Oi, tudo bem?", "Olá! Como posso ajudar?", "Olá, o que você precisa?"]
        return random.choice(respostas)
    elif categoria == "hora":
        hora = datetime.datetime.now().strftime("%H:%M:%S")
        return "A hora atual é " + hora
    elif categoria == "pesquisa":
        if palavras_chave:
            pesquisa = " ".join(palavras_chave)
            try:
                resultado = wikipedia.summary(pesquisa, sentences=2)
                return resultado
            except:
                return "Desculpe, não encontrei informações sobre " + pesquisa
        else:
            return "O que você gostaria de pesquisar?"
    else:
        return "Desculpe, não entendi o que você quis dizer. Pode ser mais específico?"

# lista de mensagens do usuário
mensagens = ["Como posso ajudar?", "Qual é a categoria dessa pergunta?"]

# loop principal
for entrada in mensagens:
    # responde à entrada do usuário usando o modelo de aprendizado de máquina
    resposta = responder(entrada)
    print(resposta)

    # atualiza o modelo de aprendizado de máquina com a entrada do usuário
    categoria = input("Qual é a categoria dessa pergunta? ")
    clf.partial_fit([entrada], [categoria])

    # verifica se o usuário quer sair
    if "tchau" in entrada.lower() or "adeus" in entrada.lower():
        break

# salva o modelo de aprendizado de máquina atualizado
joblib.dump(clf, "modelo.pkl")
