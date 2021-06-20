from .validation_error import ValidationError
from .custom_logger import get_logger

logger = get_logger(__name__)

class FileOperations:
    """
       FileOperations class is a file utility to do the operations on the files

       Methods
       -------
       load_file(file_path):
           checks for the file existence and read the file contents
    """

    @staticmethod
    def load_file(file_path):
        """
            Checks for the file existence and read the file contents
            :param file_path: Location of the file
            :type file_path: str
            :return: Return the file contents
            :rtype: str
            :raises ValidationError: When the file is empty or an invalid file type is passed
            :raises FileNotFoundError: Could not find the input file at specified path
            :raises UnicodeDecodeError: Input file has non unicode characters
        """
        try:
            logger.debug("Trying to open the file")
            with open(file_path, 'r') as file_of_words:

                #checking whether the file extension is 'txt' or not
                if not file_of_words.name.endswith(".txt"):
                    raise ValidationError('Invalid file type')

                # read the file contents
                file_content = file_of_words.read()
                logger.info("File read Sucessfully: {0}".format(file_path))
                logger.debug("Contents of the file: {0}".format(file_content))

                # check the length of the file contents
                if len(file_content) == 0:
                    # raising the user defined exception if the file is empty
                    raise ValidationError("File is empty")
                return file_content

        except FileNotFoundError as file_not_found:
            logger.error("Could not find the input file at specified path: {0}".format(file_path))
            raise file_not_found
        except UnicodeDecodeError as unicode_decode_error:
            logger.error("The input file has non unicode characters.")
            raise unicode_decode_error
