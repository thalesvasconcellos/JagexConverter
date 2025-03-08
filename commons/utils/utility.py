import random
import re

common_words = [
    "apple", "banana", "cherry", "dog", "elephant", "flower", "guitar",
    "happiness", "island", "jazz", "kangaroo", "lemon", "mountain", "notebook",
    "ocean", "piano", "quilt", "rainbow", "sunshine", "tiger", "umbrella", "violet",
    "waterfall", "xylophone", "yellow", "zebra"
]

symbols = "!@#$%^&*_-+=<>?"
digits = "0123456789"

def is_valid_email(email):
    return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email)

def generate_random_password(num_words=3, num_digits=2, num_symbols=1):
    # Select random words, digits, and symbols
    words = [random.choice(common_words) for _ in range(num_words)]
    digits_part = ''.join(random.choice(digits) for _ in range(num_digits))
    symbols_part = ''.join(random.choice(symbols) for _ in range(num_symbols))

    # Combine all parts
    password_parts = words + [digits_part, symbols_part]

    # Shuffle the password parts
    random.shuffle(password_parts)

    # Join the parts to create the password
    password = ''.join(password_parts)

    return password
