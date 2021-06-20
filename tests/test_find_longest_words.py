import pytest

from src import longest_transpose_word

# End to End testcases to find longest word and transpose of it

test_longest_transpose_words_testdata = [
    ("../tests/input_data_files/e2e_data_testcase1.txt","asdasdasda","adsadsadsa"),
    ("../tests/input_data_files/e2e_data_testcase2.txt","fairy-tales,",",selat-yriaf"),
    ("../tests/input_data_files/e2e_data_testcase3.txt","unwrapping","gnipparwnu"),
    ("../tests/input_data_files/e2e_data_testcase4.txt","1.45333123123","32132133354.1"),
    ("../tests/input_data_files/special_characters_file.txt","$%^&*()%$^&*())","))(*&^$%)(*&^%$")
]

@pytest.mark.positive_testcase
@pytest.mark.parametrize("input_file_path,input_longest,input_transposed",test_longest_transpose_words_testdata)
def test_longest_transpose_word(input_file_path,input_longest,input_transposed):

    words_dict = longest_transpose_word(file_path=input_file_path)
    assert input_longest == words_dict.get("longest_word")
    assert input_transposed == words_dict.get("transposed_word")
