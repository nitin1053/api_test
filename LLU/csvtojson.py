import csv
import json

# Specify the input CSV file and output JSON file
csv_file = '/home/nitin1053/Documents/LLM_Dashboard/LLM_Dashboard/train_data.csv'
json_file = '/home/nitin1053/Documents/LLM_Dashboard/LLM_Dashboard/train_data.json'

# Initialize a list to store the JSON response objects
response_list = []

# Read the CSV file and extract questions and answers
with open(csv_file, mode='r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        if len(row) == 3:  # Assuming each row has a question and an answer
            human_question = row[1]
            assistant_answer = row[2]

            # Create a response dictionary with "text" field
            response_dict = {
                "text": f"### Human: {human_question} \n### Assistant: {assistant_answer}"
            }

            response_list.append(response_dict)

# Save the JSON response list to a file
with open(json_file, mode='w') as jsonfile:
    json.dump(response_list, jsonfile, indent=4)

print(f'CSV file "{csv_file}" has been converted and saved to JSON file "{json_file}".')
