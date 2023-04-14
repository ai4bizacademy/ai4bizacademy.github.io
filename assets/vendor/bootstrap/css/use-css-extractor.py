import json

def extract_used_css(json_data, output_file):
    with open(output_file, 'w') as out_file:
        for file in json_data:
            if file['url'].endswith('.css'):
                used_css = ''
                css_content = file['text']
                used_ranges = file['ranges']

                for range in used_ranges:
                    used_css += css_content[range['start']:range['end']]

                out_file.write(used_css + '\n')


def main():
    input_file = 'Coverage-bootstrap.min.css.json'  # Replace with the path to your JSON file
    output_file = 'bootstrap.min.full-coverage.css'    # Replace with the path to your output file

    with open(input_file, 'r') as json_file:
        json_data = json.load(json_file)

    extract_used_css(json_data, output_file)


if __name__ == "__main__":
    main()

