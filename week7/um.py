"""regular expression module"""
import re

def main():
    """methon to call count()"""
    print(count(input("Text: ")))

# pylint: disable-next=unbalanced-tuple-unpacking
# a, b = ...


def count(string):
    """method to count the number of 'um' from the given string"""
    um_lst = re.findall(r"\b\W*um\W*", string, re.IGNORECASE)
    return len(um_lst)

def test():
    
    #  Disable all the no-member violations in this function
    # pylint: disable=no-member
    ...



if __name__ == "__main__":
    main()
