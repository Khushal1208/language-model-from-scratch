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


# This is how your code will be called.
# Your answer should be the largest value in the numbers list.
# You can edit this code to try different testing cases.
text = """
Subhaan Allaah Subhaan Allah Subhaan Allah Subhaan Allah... (x2)

Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata

Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata

Zidd Hain Ab Toh Hain Khud Ko Mitana Hona Hain Tujhmein Fanaa

Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata

Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata

Teri Adaa Bhi Hain Jhonke Wali Chhu Ke Gujar Jaane De

Teri Lachak Hain Ke Jaise Daali Dil Mein Utar Jaane De

Aaja Baahon Mein Karke Bahana Hona Hain Tujhmein Fanaa

Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata

Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata

Subhaan Allaah Subhaan Allaah Subhaan Allah Subhaan Allah... (2)

Hain Jo Iraaden Bata Doon Tumko Sharma Hi Jaaogi Tum

Dhadakanen Jo Suna Doon Tumko Ghabraa Hi Jaaogi Tum

Hamko Aata Nahi Hain Chhupana Hona Hain Tujhmein Fanaa

Chaand Sifarish Jo Karta Hamari Deta Woh Tumko Bata

Sharm-O-Haya Pe Parde Gira Ke Karni Hain Hamko Khata

Zidd Hain Ab Toh Hain Khud Ko Mitana Hona Hain Tujhmein Fanaa

Chaand chhupa badal mein
Sharma ke meri jana
Sine se lag ja tu
Balkhake meri jana

Ghumsum sa hai
gupchup sa hai
Madhosh hai
khamosh hai
Yeh sama han yeh sama
kuchh aur hai

Oh ho ho
Chaand chhupa baadal mein
Sharma ke meri jana
Sine se lag jaa tu
Balkhake meri jana

Nazdikia badh jaane de
Are nahi baba nahi
abhi nahi nahi nahi
Ye dooriya mit jane de
Are re nahi baba nahi
abhi nahi nahi nahi
Door se hi tum
ji bhar ke dekho
Tum hi kaho kaise
door se dekhu
Chand ko jaise
dekhta chakor hai

Aye ghumsum sa hai
gupchup saa hai
Madhosh hey
khamosh hey
Yeh sama ha yeh sama
kuch aur hai

Ho ho ho
chaand chhupa baadal mein
Sharma ke jane jana
Sine se lag jaa tu balkhake meri jana

Aaja re aaja re chanda
Ke jab tak tu naa aayega
Sajana ke chere toh dekhne
Yeh man tarsa jayega
Naa naa chanda tu nahi aana
Tujo aaya toh
Sanam sharma ke kahi chala jaye naa

Aaja re aaja re chanda
Tu lakh duwaye payega
Naa naa chanda tu nahi aana
Varna sanam chala jayega

Aanchal mein tu chup jane de,
Arre nahi baba nahi
abhi nahi nahi nahi
Julfo mein tum kho jane de,
Arre re nahi baba nahi
abhi nahi nahi nahi

Pyar toh nam hai
sabr kaa humdam
Wohi bhala bolo
kaise kare ham
Sawan ki rah
jaise dekhe mor hai

He rehne bhi do
jane bhi do,
Ab chhodo na
muha modo na
Ye sama ha ye sama
kuch aur hey

Aaya re aaya chanda
Ab har khwahish puri hogi
Chandni raat mein har sajani
Apne sajana ko dekhegi
Aaya re aaya chanda
Ab har khwahish puri hogi
Chandni raat mein har sajani
Apne sajana ko dekhegi
Aaya re aaya chanda
Ab har khwahish puri hogi
Chandni rat mein har sajani
Apne sajana ko dekhegi

Chaand mera naraaz hai Na baat kare, na milta hai Kaise usko samjhaun Na samjhe rishta dil ka hai.. Hafton se kitne Usne na baat ki Mujhko pata bhi nahi Kis baat ki narazagi… Chand mera naraz hai Na baat kare na milta hai Qaise usko samjhaaun Na samjhey rishta dil ka hai. Bheed hai itni Duniya main par Koyi na apna dikhta hai, Log hain paagal Kya samjhe jo Tera-mera rishta hai, Tujhko bhi toh hai na mohabbat Phir kyun doori rakhta hai Na shab mein na subha mein Na shaam dhali wo milta hai. 

"""

chain = MarkovChain()
chain.train(text)
sample_prompt = "Chand"
print(chain.generate(sample_prompt))

result = chain.generate(sample_prompt)