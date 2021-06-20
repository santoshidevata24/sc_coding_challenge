# from src import longest_transpose_words
# from src import file_operations
# from src import string_operations
from src import longest_transpose_word
from src import custom_logger
import argparse,sys
import os

logger = custom_logger.get_logger(__name__)
def main():
    """
        This is the staring point of the application.
        It calls the functionality to find the longest word and its transpose
    """

    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--file_location', help='location of the file', default="tests/input_data_files/words_file.txt")
        args = parser.parse_args()

        file_location = args.file_location

        words_dict = longest_transpose_word(file_path=file_location)
        if len(words_dict) != 0:
            print("Largest Word: {0}".format(words_dict.get("longest_word")))
            print("Transpose of largest Word: {0}".format(words_dict.get("transposed_word")))
        else:
            print("Couldn't find the longest word")

    except Exception as e:
        logger.error(e)


if __name__ == "__main__":
    main()


