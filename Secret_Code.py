import string
import random
import sys

def main():
    while True:
        message_type = input("Encode or Decode a message(or type 'exit'): ")

        if message_type.lower() == "exit":
            print("\nThank your for using the service!")
            sys.exit()
        elif message_type.capitalize() == "Encode":
            message = input("Enter your message: ").strip().split()
            if not message:
                print("No Input! Try Again!")
                continue
            encode(message)
        elif message_type.capitalize() == "Decode":
            message = input("Enter your message: ").strip().split()
            if not message:
                print("No Input! Try Again!")
                continue
            decode(message)
        else:
            print("Invalid Input!")
            continue


def encode(sentence):
    encoded = []
    for word in sentence:
        if len(word) >= 3:
            start_encode = random.choices(string.ascii_letters, k=3)
            start_word = ""
            for char in start_encode:
                start_word += char
            end_encode = random.choices(string.ascii_letters, k=3)
            end_word = ""
            for char in end_encode:
                end_word += char
            each_word = start_word + word[1:] + word[0] + end_word
            encoded.append(each_word)
        else:
            each_word = word[::-1]
            encoded.append(each_word)

    print(f"Original Message: {' '.join(sentence)}")
    print(f"Encoded Message: {' '.join(encoded)}")


def decode(message):
    decoded = []
    for word in message:
        if len(word) >= 7:
            start_end_decode = word[3:-3]
            decoded_word = start_end_decode[-1] + start_end_decode[:-1]
            decoded.append(decoded_word)
        elif len(word) < 3:
            decoded_word = word[::-1]
            decoded.append(decoded_word)
        else:
            print("Invalid Encoded Message!")
            return

    print(f"Encoded Message: {' '.join(message)}")
    print(f"Decoded Message: {' '.join(decoded)}")


if __name__ == "__main__":
    main()