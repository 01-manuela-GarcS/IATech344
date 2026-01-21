# scikit-learn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Función de entrenamiento preguntas y respustas
def build_and_train_model(train_pairs): # (dupla) no se puede modificar [este puede cambiar] {diccionario}
    # train_pair lista depares(preguntas, respuestas)
    # Ejemplo [("Hola","!Hola¡"),("adiós","!Hasta luego¡")]
    # separamos las preguntas y respuestas en dos litas
    questions =[q for q, _ in train_pairs]  # lista de preguntas
        # q de questions, a de answers
    answers =[a for _, a in train_pairs] # Lista de respuestas
    # creamos el vectorizado, que traducirá el texto a números
    vectorizer=CountVectorizer()
    # Entrenamiento
    x = vectorizer.fit_transform(questions)
    # obtenemos un lista de respuestas Únicas
    unique_answers = sorted(set(answers)) # sorted nos puede construir una lista de palabras únicas
    # creamos el diccionario con las etiquetas
    answer_to_label={a: i for i, a in enumerate(unique_answers)}
    # creamos una lista
    y=[answer_to_label[a] for a in answers]
    # Modelo clasificación de texto
    model = MultinomialNB()
    # Entrenar el modlo
    model.fit(x,y)
    return model,vectorizer,unique_answers

# Función predict_answer
def predict_answer(model,vectorizer,unique_answers,user_text):
    # convertimos el texto a números
    x = vectorizer.transform([user_text])
    # el modelo predice la etiqueta de la respuesta correcta
    label = model.predict(x)[0]
    return unique_answers[label]

# Programa principal
if __name__== "__main__":
    training_data =[
        #es una dupla, no se modifica
        ("hola", "¡Hola! ¿En qué podemos ayudarte hoy?"),
        ("buenos días", "Buenos días, gracias por contactarnos. ¿Cómo podemos asistirte?"),
        ("buenas tardes", "Buenas tardes, es un gusto atenderte. ¿Qué consulta tienes?"),
        ("buenas noches", "Buenas noches, estamos a tu disposición. ¿En qué podemos ayudarte?"),
        ("información", "Con gusto te brindamos la información que necesitas. ¿Sobre qué tema?"),
        ("soporte", "Nuestro equipo de soporte está listo para ayudarte. Cuéntanos tu inconveniente."),
        ("precio", "Con gusto te compartimos nuestros precios. ¿Qué servicio te interesa?"),
        ("gracias", "Gracias a ti por comunicarte con nosotros. ¡Que tengas un excelente día!")   
    ]
    model,vectorizer,unique_answers=build_and_train_model(training_data)
    # Mostrar un mensaje inicial al usuario
    print("Chatbot supervisado listo, Escribe Salir para terminar.\n")
    while True:
        # Pedimos una frase al usuario
        user =input("Tú: ").strip()
        if user.lower() in {"salir","exit","quit"}:
            print("Bot: !Hasta pronto¡")
            break
        response=predict_answer(model,vectorizer,unique_answers,user)
        print("Bot: ",response)