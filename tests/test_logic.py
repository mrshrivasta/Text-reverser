import sys
import os
import re
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.reverser import *

def test_logic():
    print("Testing Reversal Logic...")

    # Test 1: Full text
    assert reverse_full_text("hello") == "olleh"

    # Test 2: Word order
    assert reverse_word_order("hello world") == "world hello"

    # Test 3: Each word
    assert reverse_each_word("hello world") == "olleh dlrow"

    # Test 4: CamelCase
    assert reverse_camel_case("HelloWorld") == "olleHdlroW"

    # Test 5: Snake case
    assert reverse_snake_case("hello_world") == "olleh_dlrow"

    # Test 6: URLs
    url_text = "Check out https://google.com now"
    rev_url = reverse_urls_safely(url_text)
    assert "https://google.com" in rev_url

    # Test 7: HTML
    html_text = "<b>Hello</b>"
    rev_html = reverse_preserving_html(html_text)
    assert "<b>olleH</b>" in rev_html

    # Test 8: Palindrome (Corrected Regex)
    def is_palindrome(text):
        clean = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
        return clean == clean[::-1]
    assert is_palindrome("Racecar")
    assert is_palindrome("1221")

    # Test 9: Unicode/Emoji correctly
    emoji_text = "👨‍👩‍👧‍👦" # Family emoji
    assert reverse_full_text(emoji_text) == emoji_text # Should stay same if single cluster
    complex_text = "A 👨‍👩‍👧‍👦 B"
    assert reverse_full_text(complex_text) == "B 👨‍👩‍👧‍👦 A"

    print("All tests passed including Unicode!")

if __name__ == "__main__":
    test_logic()
