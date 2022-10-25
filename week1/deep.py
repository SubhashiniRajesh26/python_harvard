def func(ques):
    if ques == "42" or ques == "forty-two" or ques == "forty two":
        print("Yes")
    else:
        print("No")


def main():
    question = input("What is the answer to the Great Question of Life, the Universe and Everything?")
    func(question)

main()