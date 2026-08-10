# Save this as test_valid_word_square.py
from typing import List

def validWordSquare(words: List[str]) -> bool:
    for row in range(len(words)):
        wd = ""
        for col in range(len(words)):
            if col < len(words) and row < len(words[col]):
                wd = wd + words[col][row]
        if wd != words[row]:
            return False
    return True

# Test all examples
test_cases = [
    (["abcd", "bnrt", "crmy", "dtye"], True),
    (["abcd", "bnrt", "crm", "dt"], True),
    (["abc", "bde", "cef"], True),
    (["abc", "bde", "ce"], False),
]

for i, (words, expected) in enumerate(test_cases, 1):
    result = validWordSquare(words)
    status = "✅ PASS" if result == expected else "❌ FAIL"
    print(f"Test {i}: {status} - {words} -> {result} (expected {expected})")