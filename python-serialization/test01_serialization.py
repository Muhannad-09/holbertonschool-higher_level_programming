#!/usr/bin/env python3
from task_00_basic_serialization import load_and_deserialize, serialize_and_save_to_file

# Added a main function to encapsulate the test code
def main():
    # Sample data to be serialized
    data_to_serialize = {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }

    # Serialize the data to JSON and save it to a file
    serialize_and_save_to_file(data_to_serialize, 'data.json')
    print("Data serialized and saved to 'data.json'.")

    # Load and deserialize data from 'data.json'
    deserialized_data = load_and_deserialize('data.json')

    # Print the deserialized data
    print("Deserialized Data:")
    print(deserialized_data)

# Added this guard to only run main() when the script is executed directly,
# not when imported as a module
if __name__ == "__main__":
    main()
