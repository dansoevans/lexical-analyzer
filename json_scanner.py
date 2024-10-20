import re

# Define token types using regular expressions
TOKEN_REGEX = [
    ("WHITESPACE", r"\s+"),  # Ignore spaces, tabs, newlines
    ("STRING", r'"(\\.|[^"\\])*"'),  # Strings enclosed in double quotes
    ("NUMBER", r"-?\d+(\.\d+)?([eE][+-]?\d+)?"),  # Integers, floats, scientific notation
    ("TRUE", r"true"),  # Boolean true
    ("FALSE", r"false"),  # Boolean false
    ("NULL", r"null"),  # Null value
    ("LBRACE", r"\{"),  # Left brace '{'
    ("RBRACE", r"\}"),  # Right brace '}'
    ("LBRACKET", r"\["),  # Left bracket '['
    ("RBRACKET", r"\]"),  # Right bracket ']'
    ("COMMA", r","),  # Comma ','
    ("COLON", r":"),  # Colon ':'
]

# Compile the regular expressions
token_regex = [(name, re.compile(pattern)) for name, pattern in TOKEN_REGEX]

# Tokenize function
def tokenize(json_input):
    position = 0
    tokens = []

    while position < len(json_input):
        match = None
        for token_type, regex in token_regex:
            match = regex.match(json_input, position)
            if match:
                if token_type != "WHITESPACE":  # Skip whitespace
                    tokens.append((token_type, match.group()))
                position = match.end()
                break
        if not match:
            raise ValueError(f"Unexpected character at position {position}: {json_input[position]}")

    return tokens

# Main function to get user input
if __name__ == "__main__":
    user_input = input("Enter a JSON object: ")
    try:
        tokens = tokenize(user_input)
        for token in tokens:
            print(token)
    except ValueError as e:
        print(f"Error: {e}")
