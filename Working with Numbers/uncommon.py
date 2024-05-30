def fill_alphabets_word_by_word(S):
    
    words = S.split()
    num_words = len(words)


    result_words = [[] for _ in range(num_words)]

    all_chars = [char for word in words for char in word]

    index = 0

    for i in range(max(len(word) for word in words)):
        for j in range(num_words):
            if len(result_words[j]) < len(words[j]):
                result_words[j].append(all_chars[index])
                index += 1

    result_words = [''.join(word) for word in result_words]

    result_string = ' '.join(result_words)


    print(result_string)


S = "a bc def ghij kl mnopq rs"
fill_alphabets_word_by_word(S)

S = "this is pure cotton"
fill_alphabets_word_by_word(S)
