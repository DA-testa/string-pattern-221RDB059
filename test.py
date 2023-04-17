def hash(pattern):
    output = 1
    count = len(pattern) - 1

    for i in range(len(pattern)):
        curr_hash += ord(pattern[i]) * 2

        count -= 1

    return output


text = "bruhabcdefghi"
pattern = "defg"
i = 4
text_part = text[i:i+len(pattern)]
print(text_part)
