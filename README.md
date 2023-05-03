# Convert any file to DOT file
This Python script converts the contents of any file into a directed
graph in the DOT language, which can be visualized using 
# Graphviz.

# Usage
To use this script, save it in a Python file 
(e.g., convert_to_dotfile.py) and run it from the command 
line with the input file path and output file path as arguments:

python convert_to_dotfile.py input_file.txt output_file.dot

This will create a DOT file named output_file.dot in the current 
directory with the contents of input_file.txt converted into a directed graph. 
Each non-empty line in the input file is represented as a node in the graph, 
and there is a directed edge from node i to node j if the j-th
line in the file follows the i-th line in the file.

Requirements
This script requires Python 3 and the argparse library.

License
This script is licensed under the MIT License. See the [LICENSE](https://github.com/Devurl/Convert-any-Files-into-Dotfile/blob/main/LICENSE) file for details.
