# langchain_experimental/utils/file_utils.py

def write_data_to_file(data, file_path):
    # Write data to a temporary CSV file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)

    return f"Data written to file: {file_path}"
