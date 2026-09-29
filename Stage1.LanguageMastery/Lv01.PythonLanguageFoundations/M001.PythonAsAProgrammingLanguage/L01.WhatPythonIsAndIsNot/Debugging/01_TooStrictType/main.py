# ⚠️ 2 bugs: both fight duck typing.


def average_length(words):
    """Average length of the words in ANY iterable of strings; 0.0 when there are none."""
    
    # store the total number of characters
    total = 0

    #store how many words we have seen
    count = 0
    # Read one word ata time
    for word in words:
        # Add this word's length to the total 
        total += len(word)

        # Count this word
        count += 1

    if count == 0:
        return 0.0
    
    return total / count

# print(average_length(["hi", "hello"]))            # → 3.5
# print(average_length(("a", "bb", "ccc")))         # → 2.0
# print(average_length(w for w in ["ab", "cdef"]))  # → 3.0   (a generator!)
# print(average_length([]))   
