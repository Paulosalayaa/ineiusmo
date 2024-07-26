import json

def parse(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

json_string = '{"name": "Alice", "age": 30}'
parsed_data = parse(json_string)
print(parsed_data)  # Output: {'name': 'Alice', 'age': 30}
