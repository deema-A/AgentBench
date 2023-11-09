import os
import json
import argparse

def count_entries_in_json_files(folder_path):
    total_entries = 0

    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.json'):
                json_file_path = os.path.join(root, file_name)
                print("file_name: ", file_name)
                if file_name == "6-backup.json":
                    print(file_name, " SKIPPED")
                    continue
                with open(json_file_path, 'r') as json_file:
                    data = json.load(json_file)
                    if isinstance(data, list):
                        print(len(data))
                        total_entries += len(data)
                    elif isinstance(data, dict):
                        print(len(data.keys()))
                        total_entries += len(data.keys())

    return total_entries

def main():
    parser = argparse.ArgumentParser(description='Count the total number of entries in JSON files within a folder.')
    parser.add_argument('folder_path', type=str, help='Path to the folder containing JSON files')

    args = parser.parse_args()
    folder_path = args.folder_path

    total_entries = count_entries_in_json_files(folder_path)
    print(f'Total entries in JSON files within {folder_path}: {total_entries}')

if __name__ == "__main__":
    main()

# python script.py /path/to/your/folder
# Total entries in JSON files within /scratch/bbzy/deema/projects/linuxworld/AgentBench/data/os_interaction/data: 191