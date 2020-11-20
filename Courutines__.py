
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

#------------------------------------------------GFG----------------------------------------------
#Chaining
# Python3 program for demonstrating
# coroutine chaining

def producer(sentence, next_coroutine):
    '''
    Producer which just split strings and
    feed it to pattern_filter coroutine
    '''
    tokens = sentence.split(" ")
    for token in tokens:
        next_coroutine.send(token)
    next_coroutine.close()

def pattern_filter(pattern="ing", next_coroutine=None):
    '''
    Search for pattern in received token
    and if pattern got matched, send it to
    print_token() coroutine for printing
    '''
    print("Searching for {}".format(pattern))
    try:
        while True:
            token = (yield)
            if pattern in token:
                next_coroutine.send(token)
    except GeneratorExit:
        print("Done with filtering!!")

def print_token():
    '''
    Act as a sink, simply print the
    received tokens
    '''
    print("I'm sink, i'll print tokens")
    try:
        while True:
            token = (yield)
            print(token)
    except GeneratorExit:
        print("Done with printing!")

pt = print_token()
pt.__next__()
pf = pattern_filter(next_coroutine = pt)
pf.__next__()

sentence = "Bob is running behind a fast moving car"
producer(sentence, pf)



#-----------------------------------------------------------PRACTICING---------------------------------------------------------------------------------
#READING AND FINDING THE INPUT GIVEN.

def search():
    book = "my name is arnav finding lamo shit hehe damn! "
    print("Welcome to finder")
    while True:
        Word =(yield )
        if Word in book:
            print("YAY your name was in the book!! CONGO")
        else:
            print("No such word")

SEARCHER= search()
SEARCHER.__next__()

for ii in range(3):
    print("enter the word to be found:")
    ww=input()
    SEARCHER.send(ww)






























