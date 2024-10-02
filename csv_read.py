import re

def remove_invalid_characters(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            content = file.read()

        # Example: Remove non-ASCII characters
        cleaned_content = re.sub(r'[^\x00-\x7F]', '', content)

        with open(file_path, 'w', encoding=encoding) as file:
            file.write(cleaned_content)
        print("Invalid characters removed successfully.")
    except UnicodeDecodeError:
        print(f"Error decoding file with {encoding}. Try a different encoding.")

# Usage:
file_path = "test/C1HKVI01_T_N.csv"
remove_invalid_characters(file_path)