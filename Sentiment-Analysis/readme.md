# Naive Bayes Sentiment Analysis (From Scratch)

> **"AI is not magic — it’s code + data + probability."**

This project documents my learning journey while building a **Naive Bayes sentiment classifier from scratch** using Python. The goal was not accuracy at scale, but **deep understanding** of how platforms and creators infer audience emotions from comments.

---

## 1. What Problem This Solves

Creators and platforms want to answer questions like:

* Do people like this post?
* Is the audience reacting negatively?
* What is the overall emotional trend?

This project shows how **raw text comments** can be converted into:

```
text → tokens → word frequencies → probabilities → sentiment
```

using **supervised learning**.

---

## 2. Dataset Used (Supervised Learning)

Each comment is manually labeled:

* `pos` → Positive sentiment
* `neg` → Negative sentiment

Example:

```
("I love this post.", "pos")
("This post is horrible.", "neg")
```

This labeled data teaches the model **which words are associated with which emotion**.

---

## 3. Text Preprocessing (Tokenization)

Before learning, text must be cleaned.

Steps:

1. Convert to lowercase
2. Remove punctuation & numbers
3. Replace newlines with spaces
4. Split text into words (tokens)

```python
text.lower()
.translate(str.maketrans("", "", punctuation + "1234567890"))
.replace("\n", " ")
.split()
```

This ensures:

* "Love" and "love" are treated the same
* Noise like punctuation doesn’t affect learning

---

## 4. Learning Word Frequencies

The classifier builds two vocabularies:

* Words from **positive comments**
* Words from **negative comments**

```python
self.pos_counter = Counter(self.mapping["pos"])
self.neg_counter = Counter(self.mapping["neg"])
```

This creates statistical associations like:

| Word | Positive Count | Negative Count |
| ---- | -------------- | -------------- |
| love | high           | low            |
| hate | low            | high           |

---

## 5. Core Idea of Naive Bayes

Naive Bayes assumes:

> Each word contributes **independently** to sentiment

Mathematically:

```
P(sentence | positive)
= P(word1 | positive) × P(word2 | positive) × ...
```

The class (pos / neg) with the **higher probability** wins.

---

## 6. Laplace Smoothing (Why It’s Needed)

Problem:

* If a word never appeared in training → probability = 0
* One unseen word can break prediction

Solution:

```python
(word_count + 1) / (total_words + vocabulary_size)
```

This ensures:

* No zero probabilities
* Better generalization

---

## 7. Log Probabilities (Numerical Stability)

Multiplying many small probabilities causes underflow.

Solution:

```
log(a × b × c) = log(a) + log(b) + log(c)
```

So we **sum log probabilities** instead of multiplying raw values.

---

## 8. Classification Logic (Simplified)

```python
pos_score += log(P(word | positive))
neg_score += log(P(word | negative))
```

Final decision:

* `pos_score > neg_score` → Positive
* `neg_score > pos_score` → Negative
* Else → Neutral

---

## 9. What This Model Teaches

This project helped me understand:

* How sentiment analysis actually works
* How platforms infer audience emotions
* Why probability > rules
* Why Naive Bayes is still relevant

Even though modern systems use transformers, **this logic is the foundation**.

---

## 10. Limitations (Known & Accepted)

* Small dataset
* No sarcasm handling
* No negation logic ("not good")
* No emojis or slang

These are intentionally left out to focus on fundamentals.

---

## 11. Key Takeaway

> AI doesn’t understand emotions.
> It estimates them using **data, frequency, and probability**.

Building this from scratch removed the "black box" feeling and replaced it with clarity.

---


📌 **Learning-first project. Accuracy-second. Understanding-always.**
