#Amanda Miloserny
string = " I # love # to # go # on walks"
def count_hashtag (string, hashtag):
    total = 0
    index = 0
    while index < len(string):
        if string [index : index + len(hashtag)] == hashtag:
            total += 1
            index  += len(hashtag)
        else:
            index +=1
    return total

print(count_hashtag(string, "#"))
