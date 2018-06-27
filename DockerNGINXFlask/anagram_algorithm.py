#fancy dictionary sorting
from operator import itemgetter
import json

#This anagram alogirthm works in 3 steps. First it confirms that the word exists.
#If so, then it determines the length of the word, and pulls all other words of the same length from the db
#This is done so that comparisons are only done against words that are the same length-since other lenmgth words can't be anagrams
#After a list of all equal length words has been pulled, a single for loop is run (This keeps overall complexity at O(N)) wherein
#the iterated word is broken into an array of its letters and sorted-this array is then compared against the array of the given word
#This comparison is predicated off the fact that anagrams are words that are the same length with the same letters-consequently a
#sorted array of anagrams will be identical-therefore once identical arrays are found, they are added to the anagram list and returned
#once all equal length words are evaluated

def word_in_dictionary(word_to_check, conn):
    #quesries the database to determine if the word exists: if it does an array
    #with a len of one is returned, if not no array length is returned
    word_existence_raw = conn.execute('''SELECT * FROM "Dictionary" WHERE "Word" = '{}';'''.format(word_to_check))
    word_existence = word_existence_raw.cursor.fetchall()
    if len(word_existence) > 0:
        #returns a boolean of true is there was a record returned
        return True
    else:
        return False

def anagrams_of_word(word_to_check, conn):
    #creates a variable that captures the length of the submitted word
    word_length = len(word_to_check)
    #generates a new dataframe comprised only of words that are the same length as the submitted word
    #this is done so that comparisons are done only for relevent words (shorter or longer words can't be anagrams)
    word_list_of_equal_length_words_raw = conn.execute('''SELECT "Word" FROM "Dictionary" WHERE "word_length" = '{}';'''.format(word_length))
    word_list_of_equal_length_words = word_list_of_equal_length_words_raw.cursor.fetchall()

    #intializes a list of all words that are found
    anagrams_that_are_words = []

    #gets a list of all the letters that are in the word being evaluated
    whole_word_character_list = sorted([letter for letter in word_to_check])
    #iterates through the list of equal length words
    for words in word_list_of_equal_length_words:
        #generates a sorted listed of all letters in the iterated word
        letters = sorted([letter for letter in str(words[0])])
        #checks if the list of letters from the iterated word equals the list of letters the word being evaluated
        if letters == whole_word_character_list:
            #if both lists are equal (meaning a known words containes the same letters as the word being evaluated-it means they're anagrams of each other)
            anagrams_that_are_words.append(words[0])
    return anagrams_that_are_words

def is_string_a_word_checker(word_to_check, conn):
    #makes the word all lwoercase
    word_to_check = word_to_check.lower()
    #determines if the word exists
    word_truthiness = word_in_dictionary(word_to_check, conn)
    #Keeps it simple when returning the not found as an array vs a string or boolean
    not_found = ['None: The word is not found in the dictionary']

    #if the given word is a in fact a word
    if word_truthiness == True:
        #Gets the returned list of anagrams
        list_of_anagrams_that_are_words = anagrams_of_word(word_to_check, conn)
        #sorts the returned list of anagrams according the second letter
        sorted_list_of_anagrams_that_are_words_by_second_letter = sorted(list_of_anagrams_that_are_words, key=itemgetter(1))
        #returns the sorted list of anagrams 
        return sorted_list_of_anagrams_that_are_words_by_second_letter
    else:
        return not_found
