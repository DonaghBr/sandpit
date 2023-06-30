import csv

def extract_comments(yaml_data):
    comments = []
    parameter = None
    description = ''
    for line in yaml_data.splitlines():
        line = line.strip()
        if line.startswith('#'):
            if parameter is not None:
                comments.append((parameter, description.strip()))
            parameter = line.split(':')[0].strip()
            description = ''
        else:
            if parameter is not None:
                description += line + ' '
    if parameter is not None and description.strip():
        comments.append((parameter, description.strip()))
    return comments

def yaml_to_csv(yaml_file, csv_file):
    with open(yaml_file, 'r') as file:
        yaml_data = file.read()
    
    comments = extract_comments(yaml_data)
    
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Description', 'Parameter'])
        for comment in comments:
            writer.writerow(comment)

# Example usage
yaml_file = 'YAML_Input/sample.yaml'
csv_file = 'CSV_Output/output.csv'
yaml_to_csv(yaml_file, csv_file)