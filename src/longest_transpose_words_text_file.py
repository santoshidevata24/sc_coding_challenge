from .file_utils import FileOperations
from .string_utils import StringOperations
from src import custom_logger

logger = custom_logger.get_logger(__name__)

def longest_transpose_word(file_path="./tests/input_data_files/words_file.txt"):
    """
        Finds the longest word in a file and transposes it.
        Longest word is named as longest_word and it's transpose is named as transposed_word
        :param file_path: Location of the file
        :type file_path: str
        :return: Returns a dictionary containing the longest word and its transpose
        :rtype: dict
    """
    words_dict = {}
    try:
        # load the file
        file_contents = FileOperations.load_file(file_path=file_path)
        # extract the words
        words = StringOperations.extract_words(file_contents)

        # find the longest word
        longest_word = StringOperations.find_longest_word(words=words)
        # transpose the word
        transposed_word = StringOperations.string_transpose(word=longest_word)

        #Adding the longest_word and transposed_word to dict
        words_dict["longest_word"] = longest_word
        words_dict["transposed_word"] = transposed_word
        logger.info("Successfully found the longest word")
    except Exception as e:
        logger.error("longest_transpose_word exception: {0}".format(e))
    finally:
        return words_dict

