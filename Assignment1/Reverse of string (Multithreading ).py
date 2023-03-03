import threading
def reverse_string(s):
    return s[::-1]

def reverse_words(p):
    words = p.split()
    threads = []
    reversed_words = [''] * len(words)
    for i, word in enumerate(words):
        t = threading.Thread(target=lambda i, word: reversed_words.__setitem__(i, reverse_string(word)), args=(i, word))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    return ' '.join(reversed_words)

paragraph= input()
reversed_paragraph = reverse_words(paragraph)
print(reversed_paragraph)
