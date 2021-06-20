import pytest

from src import FileOperations
from src import ValidationError

# Testcases for file utility module

def test_simple_file_load():
    """
       Validate program against simple file load
    """
    fileContents = FileOperations.load_file(file_path="input_data_files/simple_file.txt")
    assert "a\nab\nabc\nabcd\nabcde" == fileContents

def test_special_characters_file():
    """
       Validate program against special characters file
    """
    fileContents = FileOperations.load_file(file_path="../tests/input_data_files/special_characters_file.txt")
    assert "%%&%&&\n&^&(&(?\n$%^&*()%$^&*())" == fileContents


def test_file_not_found():
    """
        Validate program against non-existing file
    """
    with pytest.raises(FileNotFoundError):
        FileOperations.load_file(file_path="input_data_files/nofile.txt")

def test_empty_file():
    """
        Validate program against an empty file
    """
    with pytest.raises(ValidationError) as e_info:
        FileOperations.load_file(file_path="input_data_files/empty_file.txt")
        assert "File is empty" == e_info

def test_invalid_file_type():
    """
        Validate program against invalid file type
    """
    with pytest.raises(ValidationError) as e_info:
        FileOperations.load_file(file_path="input_data_files/invalid_file_type.jpg")
        assert "Invalid file type" == e_info

def test_non_unicode_file():
    """
        Validate program against non unicode characters file
    """
    with pytest.raises(UnicodeDecodeError):
        FileOperations.load_file(file_path="input_data_files/non_unicode_file.txt")

