from word_tools import count_anagrams

def test_empty_text():
	assert count_anagrams("", "abc") == 0
 
def test_non_empty_text_with_empty_word():
    assert count_anagrams("abcd", "") == 0

def test_text_shorter_than_word():
    assert count_anagrams("abc", "abcd") == 0

def test_text_with_anagrams():
    assert count_anagrams("forxxorfxdofr", "for") == 3

def test_text_with_no_anagrams():
    assert count_anagrams("abcdefg", "hij") == 0

def test_repeated_anagrams():
    assert count_anagrams("aabbccaa", "ab") == 4

def test_long_text_with_short_word():
    assert count_anagrams("x" * 1000 + "for" + "x" * 1000, "for") == 1

def test_word_with_duplicate_characters():
    assert count_anagrams("aabbccaa", "aa") == 4

def test_no_common_characters():
    assert count_anagrams("xyzxyz", "abc") == 0

def test_text_equals_word():
    assert count_anagrams("word", "word") == 1
def test_multiple_words_with_anagrams():
    assert count_anagrams("the quick brown fox jumps over the lazy dog for ox", "for") == 3
