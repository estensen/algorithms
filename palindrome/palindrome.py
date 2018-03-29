from data_structures.deque import Deque


def palindrome(text_string):
    char_deque = Deque()

    for c in text_string:
        char_deque.add_rear(c)

    still_equal = True

    while char_deque.size() > 1 and still_equal:
        first_c = char_deque.remove_front()
        last_c = char_deque.remove_rear()
        if first_c != last_c:
            still_equal = False

    return still_equal


def palindrome2(text_string):
    return text_string == text_string[::-1]
