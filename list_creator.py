# The program connects characters of two different lists which include ASCI characters.
def create_list():
    lan_char = list(map(chr, range(32, 135)))
    jau_char = random.shuffle(lan_char)
    return lan_char, jau_char