# python3

def read_input():
    # this function needs to aquire input both from keyboard and file
    # as before, use capital i (input from keyboard) and capital f (input from file) to choose which input type will follow

    # after input type choice
    # read two lines
    # first line is pattern
    # second line is text in which to look for pattern

    # return both lines in one return

    # this is the sample return, notice the rstrip function
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def hash(pattern):
    output = 0
    count = len(pattern) - 1

    for i in range(len(pattern)):
        curr_hash = ord(pattern[i]) - 65
        curr_hash *= 2**(count/2)
        curr_hash += 65
        curr_hash *= 2**(count/2)
        output *= curr_hash

        count -= 1

    return output


def get_occurrences(pattern, text):
    output = []
    pattern_hash = hash(pattern)
    for i in range(len(text) - len(pattern)):
        text_part = text[i:i+len(pattern)]
        curr_hash = hash(text_part)
        if curr_hash == pattern_hash:
            output.append(i)
    return output


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
