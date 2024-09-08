import sys
import json
import random, string

class FileParser:
    def __init__(self, spec='spec.json'):
        """
        A Class to load the spec json in its object and parse the specified encoding file to CSV format.

        :param spec: A json file name , which has all metadata
        """
        file = open(spec, 'r')
        template = json.load(file)
        self.columns = template.get('ColumnNames', [])
        self.offset = template.get('Offsets', [])
        self.fixed_encoding = template.get('FixedWithEncoding', 'cp1252')
        self.headers = template.get('IncludeHeaders', 'True')
        self.delimeter_encoding = template.get('DelimitedEncoding', 'utf-8')

        assert len(self.columns) == len(self.offset), "Columns length and offset values mismatch !!!"
        assert len(self.columns) != 0, "Columns are not specified !!!"
        assert len(self.offset) != 0, "Offset are not specified !!!"

    def load(self, input_file, output_file):
        """
        A method to load the input file and share output in specified format and manner

        :param input_file: fixed with encoding file name
        :param output_file: CSV file with comma separated values
        """
        sfile = open(input_file, 'rb')
        sobj = sfile.read().decode(self.fixed_encoding)
        
        # print(sobj)
        len_lines = sum(int(i) for i in self.offset)
        lines = int(len(sobj)/sum(int(i) for i in self.offset))
        print(f"Procssing lines {lines}")
        output = ""
        if self.headers:
            output = ",".join(self.columns) + "\n"
            
        previous = 0
        for ln in range(0, len(sobj), len_lines):
            if ln == 0:
                continue

            line = sobj[previous:ln]
            # print(line)
            stringitr = iter(line)
            line_item = ",".join(["".join(next(stringitr) for i in range(int(l))) for l in self.offset])
            
            output += line_item + "\n"
            previous = ln

        ofile = open(output_file, 'wb').write(output.encode(self.delimeter_encoding))

if __name__ == '__main__':

    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]

    tm = FileParser()
    tm.load(input_file_name, output_file_name)
