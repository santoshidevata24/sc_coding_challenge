from .custom_logger import get_logger

logger = get_logger(__name__)

class StringOperations:
    """
       StringOperations class is a string utility to do the operations on the strings

       Methods
       -------
       extract_words(file_contents):
           extracts the words from the string and splits it based on whitespace and newline
       find_longest_word(words)
            find the first longest word from the list of words
       string_transpose(word)
            it will reverse/transpose the given string

    """

    @staticmethod
    def extract_words(file_contents):
        """
            Extracts the words from the given string and splits it based on whitespace
            :param file_contents: contents of the entire file including the new line character as a string
            :type file_contents: str
            :return: Returns the list of words
            :rtype: list
        """

        #spliting the string based on whitespace and newline
        words_list = file_contents.split()
        return words_list

    @staticmethod
    def find_longest_word(words):
        """
            Finds the first longest word from the list of words. If the there are no words it returns None
            :param words: list of words
            :type words: list
            :return: Returns the first longest word from the words list
            :rtype: str
        """

        longest_word = ""
        # if there are no rords in the list returning None
        if len(words) == 0:
            longest_word = None
            logger.debug("No words in the list")
        # if there is only one word in the list then returning that word
        elif len(words) == 1:
            longest_word = words[0]
            logger.debug("Found only 1 word in the list")
        # special case for checking if all words are exactly same
        # this is more for checking the special case
        elif len(set(words)) == 1:
            longest_word = words[0]
            logger.debug("All words are same")
        else:
            # finds the first longest word
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
        return longest_word

    @staticmethod
    def string_transpose(word):
        """
            Reverse/transpose the given string. If the string is None returning None
            :param word: string to transpose
            :type word: str
            :return: Returns the reverse/transpose word if the string is not None else it returns the None
            :rtype: str
        """
        return word[::-1] if word is not None else None
