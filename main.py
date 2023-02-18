# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next_char, i+1))
            else if next_char in ")]}":
                if not opening_brackets_stack:
                    return i+1
                pedejais = opening_bracket_stack.pop()
                if not are_matching(pedejais.char, next.char):
                    return i +1
             if opening_brackets_stack:
                retrun opening_brackets_stack[0].position
            else :
                retrun "Success"
          
def main():
    text = input()
    mismatch = find_mismatch(text)
   print(mismatch)


if __name__ == "__main__":
    main()
