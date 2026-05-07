# 🔍 Information Retrieval System using Python

A simple **Information Retrieval (IR) System** developed using **Python** that demonstrates core IR concepts such as:

- Inverted File Indexing
- TF (Term Frequency)
- DF (Document Frequency)
- Term Position Indexing
- TF-IDF Weighting
- Vector Space Model (VSM)
- Cosine Similarity
- Ranked Document Retrieval

---

# 📌 Project Objective

The objective of this project is to build a basic Information Retrieval system that can:

- Process text documents
- Generate index terms
- Construct an inverted index
- Calculate TF and DF values
- Store term positions
- Accept user queries
- Retrieve and rank relevant documents using cosine similarity

---

# 🛠️ Technologies Used

- Python 3
- Visual Studio Code (VS Code)
- Git & GitHub

---

# 📂 Project Structure

```text
IR_Project
│
├── documents
│   ├── doc1.txt
│   ├── doc2.txt
│   └── doc3.txt
│
└── ir_system.py
```

---

# 📄 Document Collection

## doc1.txt

```text
Artificial intelligence improves modern technology and search systems.
```

## doc2.txt

```text
Machine learning and artificial intelligence are important in data science.
```

## doc3.txt

```text
Search engines use indexing and retrieval techniques for information retrieval.
```

---

# ⚙️ Features

✅ Inverted File Indexing  
✅ TF Calculation  
✅ DF Calculation  
✅ Term Position Storage  
✅ TF-IDF Weighting  
✅ Vector Space Retrieval Model  
✅ Cosine Similarity Ranking  
✅ Ranked Retrieval Results  

---

# 🧠 Information Retrieval Concepts Used

## 1. Inverted Index

An inverted index stores terms and the documents where they appear.

Example:

| Term | Documents |
|---|---|
| artificial | doc1, doc2 |
| retrieval | doc3 |

---

## 2. TF (Term Frequency)

Measures how many times a term appears in a document.

Example:

```text
TF(retrieval, doc3) = 2
```

---

## 3. DF (Document Frequency)

Measures the number of documents containing a term.

Example:

```text
DF(artificial) = 2
```

---

## 4. TF-IDF

TF-IDF measures the importance of a term in a document collection.

Formula:

```text
TF-IDF = TF × IDF
```

---

## 5. Vector Space Model (VSM)

Documents and queries are represented as vectors. Similarity is calculated using cosine similarity.

---

# 🚀 How to Run the Project

## Step 1 — Clone Repository

```bash
git clone https://github.com/YourUsername/IR-Project.git
```

---

## Step 2 — Open Project Folder

```bash
cd IR-Project
```

---

## Step 3 — Run Python Program

```bash
python ir_system.py
```

If it does not work:

```bash
python3 ir_system.py
```

---

# 🔎 Sample Queries

```text
artificial intelligence
information retrieval
```

---

# 📊 Sample Ranked Output

```text
QUERY: artificial intelligence

RANKED DOCUMENTS:

doc2.txt => 0.4082
doc1.txt => 0.3535
doc3.txt => 0.0000
```

---

# 📈 Project Output

The system successfully:

- Generates inverted indexes
- Calculates TF and DF values
- Stores term positions
- Computes TF-IDF weights
- Uses cosine similarity
- Retrieves relevant documents
- Ranks documents according to similarity score

---

# 🎯 Learning Outcomes

Through this project, the following concepts were understood practically:

- Information Retrieval fundamentals
- Text preprocessing
- Index construction
- Ranking algorithms
- Vector Space Retrieval
- Cosine Similarity
- Search engine basics

---

# 📚 Future Improvements

Possible future improvements include:

- Stop-word removal
- Stemming
- GUI interface
- Larger document collections
- Web-based search engine
- Query expansion


---

# 📜 License

This project is developed for educational purposes.
