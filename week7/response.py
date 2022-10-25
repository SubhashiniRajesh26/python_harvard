from validator_collection import validators
def main():
    mail = input("What's your email address?")
    try:
        valid_email = validators.email(mail)
        print("Valid")
    except:
        print("Invalid")

if __name__ == "__main__":
    main()