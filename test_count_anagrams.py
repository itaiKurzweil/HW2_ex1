import time
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
    assert count_anagrams("aabbccaa", "ab") == 1

def test_long_text_with_short_word():
    assert count_anagrams("x" * 1000 + "for" + "x" * 1000, "for") == 1

def test_word_with_duplicate_characters():
    assert count_anagrams("aabbccaa", "aa") == 2

def test_no_common_characters():
    assert count_anagrams("xyzxyz", "abc") == 0

def test_text_equals_word():
    assert count_anagrams("word", "word") == 1
def test_multiple_words_with_anagrams():
    assert count_anagrams("the quick brown fox jumps over the lazy dog for ox", "for") == 1

def test_performance():
    long_text = "a" * 10000  # Example long text (10,000 characters of 'a')
    word = "aa"
    
    start_time = time.time()
    
    # Run count_anagrams 1000 times (or more if needed)
    for _ in range(1000):
        count_anagrams(long_text, word)
    
    end_time = time.time()
    
    elapsed_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"Time taken to run count_anagrams 1000 times: {elapsed_time_ms:.2f} ms")
    
        # Assert that the time taken is less than a certain threshold (e.g., 1000 ms)
    # If the time taken is greater than 1000 ms, this assertion will fail
    assert elapsed_time_ms < 1000, f"Test took too long: {elapsed_time_ms:.2f} ms"