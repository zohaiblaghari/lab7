def count_alphabets(sentence):
    frequency = {}

    for char in sentence:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    return frequency

if __name__ == "__main__":
    sentence = input("Enter a sentence:")
    alphabet_frequency = count_alphabets(sentence)

    print("Alphabet Frequency:")
    for char, freq in sorted(alphabet_frequency.items()):
        print(f"{char}: {freq}")