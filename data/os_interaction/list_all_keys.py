import json

def extract_keys(obj, degree, keys_with_degree):
    if isinstance(obj, dict):
        for key, value in obj.items():
            keys_with_degree[key] = degree
            extract_keys(value, degree + 1, keys_with_degree)
    elif isinstance(obj, list):
        for item in obj:
            extract_keys(item, degree, keys_with_degree)

def get_keys_with_degrees(file_path):
    keys_with_degree = {}

    with open(file_path, 'r') as file:
        data = json.load(file)
        extract_keys(data, 0, keys_with_degree)

    return keys_with_degree

# Replace 'your_file.json' with your actual file path
file_path = 'data/seed.json'
keys_with_degree = get_keys_with_degrees(file_path)
for key, degree in sorted(keys_with_degree.items()):
    print(f"{key}: Degree {degree}")
