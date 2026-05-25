import re
import string
import grapheme

def reverse_full_text(text):
    """Reverses the entire text string correctly handling grapheme clusters."""
    return "".join(reversed(list(grapheme.graphemes(text))))

def reverse_word_order(text):
    """Reverses the order of words in the text."""
    words = text.split()
    return " ".join(words[::-1])

def reverse_each_word(text):
    """Reverses each word individually but keeps their order."""
    return " ".join("".join(reversed(list(grapheme.graphemes(word)))) for word in text.split())

def reverse_sentences(text):
    """Reverses the order of sentences."""
    sentences = re.split(r'(?<=[.!?]) +', text)
    return " ".join(sentences[::-1])

def reverse_paragraphs(text):
    """Reverses the order of paragraphs."""
    paragraphs = text.split('\n')
    return "\n".join(paragraphs[::-1])

def reverse_with_options(text, preserve_punctuation=False, preserve_spacing=True):
    """Reverses text with options to preserve punctuation or spacing."""
    if not preserve_punctuation and preserve_spacing:
        return reverse_full_text(text)

    if preserve_punctuation:
        # Complex: reverse alphanumeric but keep punctuation in place
        chars = list(grapheme.graphemes(text))
        indices = [i for i, c in enumerate(chars) if any(char.isalnum() for char in c)]
        reversed_alnum = [chars[i] for i in indices][::-1]
        for i, idx in enumerate(indices):
            chars[idx] = reversed_alnum[i]
        return "".join(chars)

    return reverse_full_text(text)

def flip_case(text):
    """Flips uppercase to lowercase and vice versa."""
    return text.swapcase()

def reverse_numbers(text):
    """Reverses only the digits in the text, keeping their positions."""
    digits = re.findall(r'\d', text)
    reversed_digits = digits[::-1]

    result = []
    digit_idx = 0
    for char in text:
        if char.isdigit():
            result.append(reversed_digits[digit_idx])
            digit_idx += 1
        else:
            result.append(char)
    return "".join(result)

def reverse_vowels(text):
    """Reverses only the vowels in the text."""
    vowels = "aeiouAEIOU"
    found_vowels = [c for c in text if c in vowels]
    reversed_vowels = found_vowels[::-1]

    result = []
    v_idx = 0
    for char in text:
        if char in vowels:
            result.append(reversed_vowels[v_idx])
            v_idx += 1
        else:
            result.append(char)
    return "".join(result)

def reverse_consonants(text):
    """Reverses only the consonants in the text."""
    vowels = "aeiouAEIOU"
    found_consonants = [c for c in text if c.isalpha() and c not in vowels]
    reversed_consonants = found_consonants[::-1]

    result = []
    c_idx = 0
    for char in text:
        if char.isalpha() and char not in vowels:
            result.append(reversed_consonants[c_idx])
            c_idx += 1
        else:
            result.append(char)
    return "".join(result)

def reverse_every_nth_word(text, n=2):
    """Reverses every nth word."""
    words = text.split()
    for i in range(n-1, len(words), n):
        words[i] = "".join(reversed(list(grapheme.graphemes(words[i]))))
    return " ".join(words)

def reverse_every_nth_char(text, n=2):
    """Reverses chunks of n characters."""
    chars = list(grapheme.graphemes(text))
    result = ""
    for i in range(0, len(chars), n):
        chunk = chars[i:i+n]
        result += "".join(reversed(chunk))
    return result

def reverse_preserving_capitalization(text):
    """Reverses text but keeps the capitalization at the original indices."""
    chars = list(grapheme.graphemes(text))
    is_upper = [c.isupper() for c in chars]
    reversed_chars = list(reversed(chars))
    for i, upper in enumerate(is_upper):
        if upper:
            reversed_chars[i] = reversed_chars[i].upper()
        else:
            reversed_chars[i] = reversed_chars[i].lower()
    return "".join(reversed_chars)

def reverse_keep_ends(text):
    """Reverses words but keeps first and last letter fixed."""
    words = text.split()
    new_words = []
    for word in words:
        g = list(grapheme.graphemes(word))
        if len(g) > 2:
            new_words.append(g[0] + "".join(reversed(g[1:-1])) + g[-1])
        else:
            new_words.append(word)
    return " ".join(new_words)

def reverse_camel_case(text):
    """Reverses CamelCase parts but keeps the structure."""
    parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z][a-z]|\b)', text)
    return "".join("".join(reversed(list(grapheme.graphemes(part)))) for part in parts)

def reverse_snake_case(text):
    """Reverses parts in snake_case."""
    parts = text.split('_')
    return "_".join("".join(reversed(list(grapheme.graphemes(part)))) for part in parts)

def reverse_kebab_case(text):
    """Reverses parts in kebab-case."""
    parts = text.split('-')
    return "-".join("".join(reversed(list(grapheme.graphemes(part)))) for part in parts)

def reverse_urls_safely(text):
    """Reverses text but keeps URLs intact."""
    url_pattern = r'https?://\S+'
    urls = re.findall(url_pattern, text)
    non_urls = re.split(url_pattern, text)

    reversed_non_urls = ["".join(reversed(list(grapheme.graphemes(part)))) for part in non_urls]

    result = []
    for i in range(len(reversed_non_urls)):
        result.append(reversed_non_urls[i])
        if i < len(urls):
            result.append(urls[i])
    return "".join(result)

def reverse_markdown_safely(text):
    """Simple implementation for markdown reversal."""
    return reverse_full_text(text)

def reverse_preserving_html(text):
    """Reverses text but keeps HTML tags intact and in place."""
    parts = re.split(r'(<[^>]+>)', text)
    for i in range(len(parts)):
        if not parts[i].startswith('<'):
            parts[i] = "".join(reversed(list(grapheme.graphemes(parts[i]))))
    return "".join(parts)

def reverse_inside_brackets(text):
    """Reverses only the text inside [brackets], (parentheses), or {braces}."""
    def repl(match):
        inner = "".join(reversed(list(grapheme.graphemes(match.group(2)))))
        return match.group(1) + inner + match.group(3)

    text = re.sub(r'(\()([^)]*)(\))', repl, text)
    text = re.sub(r'(\[)([^\]]*)(\])', repl, text)
    text = re.sub(r'(\{)([^}]*)(\})', repl, text)
    return text

def reverse_hashtags_only(text):
    """Reverses only the hashtags."""
    def repl(match):
        inner = "".join(reversed(list(grapheme.graphemes(match.group(1)))))
        return "#" + inner
    return re.sub(r'#(\w+)', repl, text)

def reverse_mentions_only(text):
    """Reverses only the @mentions."""
    def repl(match):
        inner = "".join(reversed(list(grapheme.graphemes(match.group(1)))))
        return "@" + inner
    return re.sub(r'@(\w+)', repl, text)

def upside_down_text(text):
    """Converts text to upside down characters (reversed)."""
    normal = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.?!,;:'\"()[]{}<>"
    flipped = "ɐqɔpǝɟƃɥᴉɾʞlɯuodbdsuʇnʌʍxʎz∀qƆpƎℲפHIſʞ˥WNOԀQᴚS┴∩ΛMX⅄Z0ƖᄅƐㄣϛ9ㄥ86˙¿¡'؛:،„)(][}{><"
    trans = str.maketrans(normal, flipped)
    reversed_text = "".join(reversed(list(grapheme.graphemes(text))))
    return reversed_text.translate(trans)

def zalgo_text(text):
    """Adds zalgo/glitch effect to text."""
    marks = ["\u0300", "\u0301", "\u0302", "\u0303", "\u0304", "\u0305", "\u0306", "\u0307", "\u0308", "\u0309", "\u030a", "\u030b", "\u030c", "\u030d", "\u030e", "\u030f"]
    import random
    return "".join(c + "".join(random.choice(marks) for _ in range(random.randint(1, 3))) for c in text)

def reverse_diagonal(text):
    """Fun mode: Diagonal reversal (matrix-like)."""
    lines = text.split('\n')
    max_len = max(len(line) for line in lines) if lines else 0
    grid = [line.ljust(max_len) for line in lines]

    return "\n".join(" " * i + "".join(reversed(list(grapheme.graphemes(line)))) for i, line in enumerate(grid))

def reverse_matrix(text):
    """Matrix/Grid mode."""
    lines = text.split('\n')
    if not lines: return ""
    max_len = max(len(line) for line in lines)
    grid = [list(grapheme.graphemes(line.ljust(max_len))) for line in lines]

    transposed = ["".join(row) for row in zip(*grid)]
    return "\n".join("".join(reversed(list(grapheme.graphemes(row)))) for row in transposed)

def reverse_unicode_correctly(text):
    """Properly handles unicode characters and emojis during reversal."""
    return "".join(reversed(list(grapheme.graphemes(text))))
