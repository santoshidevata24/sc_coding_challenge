import pytest

from src import StringOperations

# Testcases for string utility module

test_extract_words_testdata = [
    ("a\nab\nabc\nabcd\nabcde",["a", "ab", "abc", "abcd", "abcde"]),
    ("a\nab\nabc xyz\nabcd\nabcde",["a", "ab", "abc", "xyz", "abcd", "abcde"])
]

test_find_longest_words_positive_testcase_testdata = [
    (["a", "ab", "abc", "abcd", "abcde"],"abcde"),
    (["abc"],"abc"),
    (["abc", "abc", "abc", "abc"],"abc"),
    (["a", "vwxyz", "ab", "abc", "abcd", "abcde"],"vwxyz"),
    (["123", "1234", "1", "12", "12345", "123456"],"123456"),
    (["%%&%&&","&^&(&(?","******","$%^&*()%$^&*())"],"$%^&*()%$^&*())")

]

test_find_longest_words_negative_testcase_testdata = [
    ([], None),
    ([                                  ],None)
]

test_transpose_word_postive_testdata = [
    ("abcde","edcba"),
    ("234234?","?432432")
]

test_transpose_word_negative_testdata = [
    (None,None)
]

@pytest.mark.positive_testcase
@pytest.mark.parametrize("file_contents,expected_words_list",test_extract_words_testdata)
def test_extract_words(file_contents,expected_words_list):
    """
       Validate the program against multiple sets of words list
    """
    words_list = StringOperations.extract_words(file_contents)
    assert all([a == b for a, b in zip(expected_words_list, words_list)])


@pytest.mark.positive_testcase
@pytest.mark.parametrize("words_list,expected_word",test_find_longest_words_positive_testcase_testdata)
def test_find_longest_word_postive_testdata(words_list,expected_word):
    """
        Validate the program against multiple sets of words to find the longest word
    """
    longest_word = StringOperations.find_longest_word(words_list)
    assert expected_word == longest_word

@pytest.mark.negative_testcase
@pytest.mark.parametrize("words_list,expected_word",test_find_longest_words_negative_testcase_testdata)
def test_find_longest_word_negative_testdata(words_list,expected_word):
    """
        Validate the program against multiple sets of words to find the longest word
    """
    longest_word = StringOperations.find_longest_word(words_list)
    assert expected_word == longest_word

@pytest.mark.positive_testcase
@pytest.mark.parametrize("word,expected_transpose_word",test_transpose_word_postive_testdata)
def test_transpose_word_postive_testdata(word,expected_transpose_word):
    """
        Validate the program against multiple sets of words to transpose it
    """
    actual_transposed_word = StringOperations.string_transpose(word)
    assert expected_transpose_word == actual_transposed_word

@pytest.mark.negative_testcase
@pytest.mark.parametrize("word,expected_transpose_word",test_transpose_word_negative_testdata)
def test_transpose_word_negative_testdata(word,expected_transpose_word):
    """
        Validate the program against multiple sets of words to transpose it
    """
    actual_transposed_word = StringOperations.string_transpose(word)
    assert expected_transpose_word == actual_transposed_word