# 🧠 Semantic Similarity & Word Embeddings (From First Principles)

## Overview

This project explores **how machines understand relationships between words** using **vector embeddings** and **cosine similarity**.

Instead of treating words as symbols or labels, we represent them as **points in a high-dimensional space**, where *meaning emerges from geometry*.

> **LLMs don’t understand language.
> They organize probability in high-dimensional vector space.**

This project removes the “AI is magic” misconception and replaces it with **engineering intuition**.

---

## What This Project Demonstrates

* How words become vectors (embeddings)
* Why similar words live close together in vector space
* How cosine similarity measures semantic closeness
* How semantic similarity works without rules or logic
* The same core idea used inside modern LLMs

No ML libraries.
No abstractions.
Just math, vectors, and probability.

---

## Core Idea (First Principles)

### Fundamental Assumption

> **Words that appear in similar contexts have similar meanings**

The model never learns definitions.
It only learns **patterns of co-occurrence**.

Over time:

```
Context → Optimization → Geometry → Meaning
```

---

## How Meaning Becomes Geometry

### Step 1: Words as Vectors

Each word is represented as a vector:

```
tree → [0.12, -0.83, 0.44, 1.02, ...]
plant → [0.11, -0.85, 0.46, 0.98, ...]
```

The numbers themselves mean nothing individually.

👉 **Meaning comes from relative position and direction.**

---

### Step 2: Context Shapes Vectors

Example contexts:

```
I have a dog
I have a cat
```

Because `dog` and `cat` appear in similar contexts, their vectors are pushed **closer together** during training.

Words like `car` appear in very different contexts, so they drift away.

---

### Step 3: Geometry = Meaning

After millions of updates:

```
dog  ●───●  cat        car ●─────────────
```

Distance in vector space ≈ semantic similarity.

---

## Why Dimensions Don’t Have Names

A common misconception:

❌ “Each dimension represents a specific feature (gender, size, emotion)”

Reality:

* Meaning is **distributed**
* Each dimension contributes partially
* Semantics emerge from **patterns across many dimensions**

Just like a face isn’t one pixel — meaning isn’t one number.

---

## Measuring Similarity: Cosine Similarity

We don’t compare raw values.
We compare **direction**.

Cosine similarity measures the angle between two vectors:

```
cosine ≈ 1.0  → very similar
cosine ≈ 0.0  → unrelated
cosine < 0    → opposite-ish
```

This is why cosine similarity works so well for language.

---

## Implementation Details

### Cosine Similarity

```python
def cosine_similarity(vec_a, vec_b):
    return sum(a * b for a, b in zip(vec_a, vec_b)) / (norm(vec_a) * norm(vec_b))
```

---

### Finding Similar Words

```python
def similar_words(word, top_k=10):
    return sorted(
        word_to_vector.keys(),
        key=lambda x: -cosine_similarity(word_to_vector[x], word_to_vector[word])
    )[:top_k]
```

This is effectively **nearest-neighbor search in embedding space** — the same idea used in:

* Semantic search
* Recommendation systems
* RAG pipelines
* Memory retrieval in LLMs

---

## Example Output

```
['tree', 'wood', 'plant', 'saw', 'farm', 'base', 'star', 'door', 'bird', 'grow']
```

### Why This Makes Sense

* **wood, plant, grow** → biological / natural context
* **saw, door** → material / usage association
* **bird** → narrative co-occurrence
* **farm** → environmental context

This shows something important:

> Embeddings capture **usage proximity**, not dictionary meaning.

---

## Validation via Similarity Checks

```python
plant ↔ grow   → high similarity
plant ↔ tree   → high similarity
plant ↔ minute → low similarity
```

This confirms that vectors encode **semantic relationships**, not spelling or syntax.

---

## How LLMs Use This Internally (High Level)

```
input text
→ tokens
→ embeddings (vectors)
→ attention (relationships)
→ probability over next token
→ response
```

LLMs don’t retrieve facts.
They **navigate meaning-space**.

Your question activates a region.
The response comes from nearby, high-probability regions.

---

## What This Project Taught Me

* Meaning is geometric, not symbolic
* AI doesn’t “understand” emotions
* Similarity ≠ rules, it’s distance
* Embeddings remove the black-box feeling
* Understanding > calling libraries

---

## Why This Matters

This exact idea powers:

* Search engines
* ChatGPT
* Recommendation systems
* Sentiment analysis
* Semantic clustering
* Retrieval-Augmented Generation (RAG)

Scale changes.
Math doesn’t.

---

## Final Takeaway

> **AI is not magic.
> It’s vectors + optimization + probability.**

Building this from scratch replaced misconceptions with clarity — and turned NLP from mystery into engineering.