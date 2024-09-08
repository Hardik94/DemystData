import sys
import json
import random, string


def generate_data(N):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(N))

def generate_raw(records, output_file='raw_data.psv'):
    file = open('spec.json', 'r')
    template = json.load(file)
    print(template)

    output = []
    for ix in range(records):
        line = "".join(generate_data(int(i)) for i in template['Offsets'])
        output.append(line.encode(template['FixedWidthEncoding'])) #+ "\n"

    output_file = open(output_file, 'wb')
    output_file.writelines(output)

if __name__ == '__main__':

    output_file_name = sys.argv[1]
    records = sys.argv[2]
    generate_raw(int(records), output_file_name)
