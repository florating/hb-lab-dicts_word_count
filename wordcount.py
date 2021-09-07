"""Count words in file."""

"""INSTRUCTIONS:
Write a program, wordcount.py, that opens a file and counts how many
times each space-separated word occurs in that file. Your program should
then output each word and the number of times it apperas in the file.

LINK: https://fellowship.hackbrightacademy.com/materials/serft8/exercises/dicts-word-count/
"""


def count_words(filename):
    """Return dictionary containing word keys and count values.
    
    INPUT: filename (string path)
    OUTPUT: return dictionary in format word_string:count_int
    """

    # opens a file
    the_file = open(filename)
    # ITERATE/LOOP:
    file_dict = {}
    for line in the_file:
        words_list = line.rstrip().split(' ')   # remove punctuation
        for word_str in words_list:
            # counts how many times each space-separated word occurs in that file
            file_dict[word_str] = file_dict.get(word_str, 0) + 1
    # close the file
    the_file.close()
    # output (return vs print) each word and the number of times it appears in the file (helper function?)
    return file_dict


def print_count(mydict):
    """Print list of key(words)-value(count). Returns None.
    
    INPUT: dictionary from count_words function
    OUTPUT: print list of words and their counts
    """
    for key, value in mydict.items():
        print(f"{key} {value}")


def main():
    print_count(count_words('test.txt'))


# This line of code will be hit by the interpreter (correct word?)
# but won't evaluate bc it's commented out.

if __name__ == "__main__":
    main()
    print("I opened wordcount.py!")
