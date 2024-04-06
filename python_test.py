def sample():
    yield "おはよう"
    yield "こんにちは"
    yield "こんばんは"

A = sample()

for text in A:
    print(text)