import random
from string import punctuation
from collections import defaultdict


class MarkovChain:
    def __init__(self):
        self.graph = defaultdict(list)

    def _tokenize(self, text):
        return (
            text.lower()
            .translate(str.maketrans("", "", punctuation + "1234567890"))
            .replace("\n", " ")
            .split()
        )

    def train(self, text):
        tokens = self._tokenize(text)
        for i in range(len(tokens) - 1):
            self.graph[tokens[i]].append(tokens[i + 1])

    def generate(self, prompt, length=10):
        current = self._tokenize(prompt)[-1]
        output = prompt

        for _ in range(length):
            options = self.graph.get(current, [])
            if not options:
                break
            next_word = random.choice(options)
            output += " " + next_word
            current = next_word

        return output


# ---- DEMO ----
mc = MarkovChain()

training_text = """
I learn AI every day
I learn Python every day
I build projects
"""

mc.train(training_text)

print(mc.generate("I", 6))