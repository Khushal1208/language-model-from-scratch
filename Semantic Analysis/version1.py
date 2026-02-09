import os
import pickle
from numpy.linalg import norm

# -------------------------------
# Load word embeddings
# -------------------------------

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
EMBEDDING_PATH = os.path.join(CURRENT_DIR, "word_to_vector_trsf.pkl")

with open(EMBEDDING_PATH, "rb") as f:
    word_to_vector = pickle.load(f)

print(f"Loaded {len(word_to_vector)} word vectors")


# -------------------------------
# Cosine Similarity
# -------------------------------

def cosine_similarity(vec_a, vec_b):
    """
    Measures similarity between two vectors.
    Returns a value between -1 and 1.
    """
    return sum(a * b for a, b in zip(vec_a, vec_b)) / (norm(vec_a) * norm(vec_b))


# -------------------------------
# Find Similar Words
# -------------------------------

def similar_words(word, top_k=10):
    """
    Returns top_k most similar words to the given word
    using cosine similarity.
    """
    if word not in word_to_vector:
        raise ValueError(f"Word '{word}' not found in vocabulary")

    target_vector = word_to_vector[word]

    similarities = []

    for other_word, other_vector in word_to_vector.items():
        sim = cosine_similarity(target_vector, other_vector)
        similarities.append((other_word, sim))

    # Sort by similarity (highest first)
    similarities.sort(key=lambda x: x[1], reverse=True)

    return similarities[:top_k]


# -------------------------------
# Demo / Experiments
# -------------------------------

if __name__ == "__main__":

    # Pairwise similarity checks
    print("\n--- Cosine Similarity Examples ---")
    print("plant ↔ grow   :", cosine_similarity(
        word_to_vector["plant"], word_to_vector["grow"]))
    print("minute ↔ plant :", cosine_similarity(
        word_to_vector["minute"], word_to_vector["plant"]))
    print("plant ↔ tree   :", cosine_similarity(
        word_to_vector["plant"], word_to_vector["tree"]))

    # Nearest neighbors
    print("\n--- Words similar to 'tree' ---")
    for word, score in similar_words("tree", top_k=10):
        print(f"{word:>10} : {score:.4f}")

    print("\n--- Words similar to 'plant' ---")
    for word, score in similar_words("plant", top_k=10):
        print(f"{word:>10} : {score:.4f}")