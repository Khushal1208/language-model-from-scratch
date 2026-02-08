from string import punctuation
from collections import Counter
import math

# Training data
post_comments_with_labels = [
    ("I love this post.", "pos"),
    ("This post is your best work.", "pos"),
    ("I really liked this post.", "pos"),
    ("I agree 100 percent. This is true", "pos"),
    ("This post is spot on!", "pos"),
    ("So smart!", "pos"),
    ("What a good point!", "pos"),
    ("Bad stuff.", "neg"),
    ("I hate this.", "neg"),
    ("This post is horrible.", "neg"),
    ("I really disliked this post.", "neg"),
    ("What a waste of time.", "neg"),
    ("I do not agree with this post.", "neg"),
    ("I can't believe you would post this.", "neg"),
]


class NaiveBayesClassifier:
    def __init__(self, samples):
        self.vocab = set()
        self.class_word_counts = {"pos": Counter(), "neg": Counter()}
        self.class_counts = Counter()
        self.total_words = {"pos": 0, "neg": 0}

        for text, label in samples:
            tokens = self.tokenize(text)
            self.class_word_counts[label].update(tokens)
            self.class_counts[label] += 1
            self.total_words[label] += len(tokens)
            self.vocab.update(tokens)

        self.vocab_size = len(self.vocab)
        self.total_samples = len(samples)

    @staticmethod
    def tokenize(text):
        text = text.lower().replace("'", "")
        return (
            text.translate(str.maketrans("", "", punctuation + "1234567890"))
            .split()
        )

    def log_probability(self, tokens, label):
        # log P(label)
        log_prob = math.log(self.class_counts[label] / self.total_samples)

        # log P(words | label)
        for token in tokens:
            word_count = self.class_word_counts[label][token] + 1  # Laplace smoothing
            total = self.total_words[label] + self.vocab_size
            log_prob += math.log(word_count / total)

        return log_prob

    def classify(self, text, threshold=0.5):
        tokens = self.tokenize(text)

        if not tokens:
            return "neutral"

        pos_score = self.log_probability(tokens, "pos")
        neg_score = self.log_probability(tokens, "neg")

        if abs(pos_score - neg_score) < threshold:
            return "neutral"
        return "pos" if pos_score > neg_score else "neg"


# Train once
classifier = NaiveBayesClassifier(post_comments_with_labels)

def get_sentiment(text):
    return classifier.classify(text)


# Example usage
if __name__ == "__main__":
    tests = [
        "Love this post",
        "This is horrible",
        "This post",
        "I can't believe this",
        "Amazing work",
        "What a waste",
        "!!!"
    ]

    for t in tests:
        print(f"{t!r} -> {get_sentiment(t)}")