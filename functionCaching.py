
import time
from functools import lru_cache

@lru_cache(maxsize=32)    ## MAXSIZE MEANS IT REMEMBERS LAST n(Here=32) VALUES and caches those.
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    some_work(1)
    some_work(6)
    some_work(2)
    print("Done... Calling again")
    input()
    some_work(3)
    print("Called again")




#For better understanding ------------------------------------------------>

class Record:
    __dct = None

    def __init__(self, dict):
        self.dct = dict

    @lru_cache(maxsize  =  int(input("Please enter the cache size: \n")))
    def lastName (self, firstName):
        time.sleep(3)
        if firstName in self.dct:
            return self.dct[firstName]
        else:
            return "Not Found"


if __name__ == "__main__" :
    dict = {"Harry": "Skillf", "Miracle": "Jr", "Obama": "Champion", "Rohan": "Friend"}
    record = Record(dict)

    print(record.lastName("Harry"))
    print(record.lastName("Miracle"))
    print(record.lastName("Obama"))
    print(record.lastName("Miracle"))