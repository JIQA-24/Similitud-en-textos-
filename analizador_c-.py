import markovify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity 

# Cuerpo de texto original 1
with open("prueba.c-", "r") as f:
    text1 = f.read()

# Cuerpo de texto original 2
with open("prueba2.c-", "r") as f:
    text2 = f.read()

# Generación de programas sintéticos utilizando Markovify
model1 = markovify.Text(text1, state_size=5)
synthetic_program1 = model1.make_sentence(tries=100)

model2 = markovify.Text(text2, state_size=5)
synthetic_program2 = model2.make_sentence(tries=100)

print("Programa sintético 1:\n", synthetic_program1)
print("\nPrograma sintético 2:\n", synthetic_program2)

# Creación de la instancia del vectorizador
vectorizer = TfidfVectorizer()

# Creación de la matriz de características para los cuerpos de texto originales y sintéticos
X_original = vectorizer.fit_transform([text1, text2])
X_synthetic = vectorizer.transform([synthetic_program1, synthetic_program2])

print("Matriz de características para los cuerpos de texto originales:\n", X_original.toarray())
print("\nMatriz de características para los programas sintéticos:\n", X_synthetic.toarray())


# Cálculo de la similitud entre los cuerpos de texto originales y sintéticos
similarity_original_synthetic1 = cosine_similarity(X_original[0], X_synthetic[0])
similarity_original_synthetic2 = cosine_similarity(X_original[1], X_synthetic[1])

print("Similitud entre el cuerpo de texto original 1 y el programa sintético 1:", similarity_original_synthetic1)
print("Similitud entre el cuerpo de texto original 2 y el programa sintético 2:", similarity_original)