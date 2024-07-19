import re

def extract_text_between_markers(file_path, start_marker, end_marker):
    with open(file_path, 'r') as file:
        content = file.read()

    pattern = re.compile(f'{re.escape(start_marker)}(.*?){re.escape(end_marker)}', re.DOTALL)
    matches = pattern.findall(content)

    return matches

# Usage
file_path = 'gpt_output_latest_3.txt'
start_marker = '----------------------------------------------------------------------------------------'
end_marker = '************ SCALE SIM Run Complete ****************'

extracted_texts = extract_text_between_markers(file_path, start_marker, end_marker)
for text in extracted_texts:
    print(text)
