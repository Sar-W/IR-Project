import os
import math
from collections import defaultdict, Counter

# -----------------------------------
# READ DOCUMENTS
# -----------------------------------

folder_path = "documents"

documents = {}

for filename in os.listdir(folder_path):

    if filename.endswith(".txt"):

        with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as file:

            documents[filename] = file.read().lower()

# -----------------------------------
# TOKENIZATION
# -----------------------------------

processed_docs = {}

for doc, text in documents.items():

    processed_docs[doc] = text.split()

# -----------------------------------
# CREATE INVERTED INDEX
# -----------------------------------

inverted_index = defaultdict(dict)
term_positions = defaultdict(dict)

for doc, words in processed_docs.items():

    term_count = Counter(words)

    for position, term in enumerate(words):

        inverted_index[term][doc] = term_count[term]

        if doc not in term_positions[term]:

            term_positions[term][doc] = []

        term_positions[term][doc].append(position)

# -----------------------------------
# DISPLAY INVERTED INDEX
# -----------------------------------

print("\\nINVERTED INDEX\\n")

for term in inverted_index:

    df = len(inverted_index[term])

    print(f"\\nTERM: {term}")
    print(f"DF = {df}")

    for doc in inverted_index[term]:

        tf = inverted_index[term][doc]
        positions = term_positions[term][doc]

        print(f"Document: {doc}")
        print(f"TF: {tf}")
        print(f"Positions: {positions}")

# -----------------------------------
# TF-IDF CALCULATION
# -----------------------------------

N = len(documents)

idf = {}

for term in inverted_index:

    df = len(inverted_index[term])

    idf[term] = math.log10(N / df)

# -----------------------------------
# DOCUMENT VECTORS
# -----------------------------------

doc_vectors = {}

for doc, words in processed_docs.items():

    tf = Counter(words)

    vector = {}

    for term in tf:

        vector[term] = tf[term] * idf[term]

    doc_vectors[doc] = vector

# -----------------------------------
# COSINE SIMILARITY
# -----------------------------------

def cosine_similarity(query_vector, doc_vector):

    dot_product = 0

    for term in query_vector:

        if term in doc_vector:

            dot_product += query_vector[term] * doc_vector[term]

    query_magnitude = math.sqrt(sum(weight ** 2 for weight in query_vector.values()))

    doc_magnitude = math.sqrt(sum(weight ** 2 for weight in doc_vector.values()))

    if query_magnitude == 0 or doc_magnitude == 0:

        return 0

    return dot_product / (query_magnitude * doc_magnitude)

# -----------------------------------
# SEARCH FUNCTION
# -----------------------------------

def search(query):

    query_words = query.lower().split()

    query_tf = Counter(query_words)

    query_vector = {}

    for term in query_tf:

        if term in idf:

            query_vector[term] = query_tf[term] * idf[term]

    scores = {}

    for doc in doc_vectors:

        similarity = cosine_similarity(query_vector, doc_vectors[doc])

        scores[doc] = similarity

    ranked_docs = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print("\\nQUERY:", query)
    print("\\nRANKED DOCUMENTS:\\n")

    for doc, score in ranked_docs:

        print(doc, "=>", round(score, 4))

# -----------------------------------
# TEST QUERIES
# -----------------------------------

search("artificial intelligence")
search("information retrieval")