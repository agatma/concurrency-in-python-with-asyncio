import time

freqs = {}

with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
    lines = f.readlines()

    start = time.time()

    for line in lines:
        data = line.split('\t')
        word = data[0]
        count = int(data[2])
        freqs[word] = freqs[word] + count if word in freqs else count
    end = time.time()
    print(f'{end-start:.4f}')
