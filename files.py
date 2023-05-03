import argparse

def convert_to_dotfile(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    with open(output_file, 'w') as f:
        f.write('digraph G {\n')
        for i, line in enumerate(lines):
            line = line.strip()
            if len(line) > 0:
                f.write('  "{}" -> "{}";\n'.format(i, line))
        f.write('}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert any file to DOT file')
    parser.add_argument('input_file', help='Input file path')
    parser.add_argument('output_file', help='Output DOT file path')
    args = parser.parse_args()

    convert_to_dotfile(args.input_file, args.output_file)
