def longest_sentence():
    stream = open('artykul.txt', 'r', encoding='utf-8')
    try:
        content = stream.read()
    finally:
        stream.close()
    n = content.split(".")
    length_of_sentence = [len(i) for i in n]
    print('The longest sentence in this article is: ', n[length_of_sentence.index(max(length_of_sentence))])


def most_common():
    from collections import Counter
    with open('artykul.txt', 'r', encoding='utf-8') as input_file:
        count = Counter(word for line in input_file
                        for word in line.split())
    print('Most common words are:', count.most_common(10))


if __name__ == '__main__':
    longest_sentence()
    most_common()
