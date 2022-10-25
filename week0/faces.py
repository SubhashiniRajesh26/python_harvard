def makingFaces(sentence):
    sentence = sentence.replace(":)", "\U0001F642")
    sentence = sentence.replace(":(", "\U0001F61F")
    return sentence
    

def main():
    sentence = input("Enter the sentence: ")
    print(makingFaces(sentence))

main()
