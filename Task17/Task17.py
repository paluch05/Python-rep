def longest_sentence_and_most_common_word():
    stream = open('artykul.txt', 'r', encoding='utf-8')
    try:
        content = stream.read()
        n = content.split(".")
        length_of_sentence = [len(i) for i in n]
        from collections import Counter
        count = Counter(content.lower().strip().split())
    finally:
        stream.close()
    return count, length_of_sentence, n


if __name__ == '__main__':
    count, length_of_sentence, n = longest_sentence_and_most_common_word()
    print('The longest sentence in this article is: ', n[length_of_sentence.index(max(length_of_sentence))])
    print('Most common words are:', count.most_common(10))
