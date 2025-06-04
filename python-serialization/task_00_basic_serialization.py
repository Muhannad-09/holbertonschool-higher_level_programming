import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): Name of the JSON file to save the data to.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_and_deserialize(filename):
    """
    Load data from a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Name of the JSON file to load data from.

    Returns:
        dict: Deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
