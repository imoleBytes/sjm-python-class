# word = ("money", "good", "wealth","money", "riches", "money")
# cal = input("Input any word: ")
# print(word.count(cal))



# word = input("Enter a sentence: ")
# figure = input("Enter a word to count: ")
# print(word.count(figure))


# {"twinkle": 2, "little": 1, "star": 1}

print("***********************")
print("*****Word Counter******")
print("***********************")


def Counter():

    word_count = {}

    sentence = input("Enter a sentence: ")

    # sentence = "twinkle twinkle little star"


    for word in sentence.split():  
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    print("The frequency Count: ")
    print("*****")
    print(word_count)

c = "y"
while True:
    if c == "y":
        Counter()
    else:
        break
    c = input("Continue?: (y/n)")


print("Program end, thank you for playing")