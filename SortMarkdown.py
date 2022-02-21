"""
Usage: 
`python SortMarkdown.py --input Glossary.md --output Glossary-sorted.md --header 3`

Level 3 headings in Glossary.md will re-ordered alphabetically and saved in Glossary-sorted.md
All headings (with their sections) of a specified level are sorted.

Assumptions:
1. The section to be sorted is a contiguous level.
2. The new heading after the section to be sorted starts with level one heading = "# "

Adapted from https://github.com/Logan-Lin/SortMarkdown
"""

import sys

def sort_subsection(markdown_strings, output_filename, header_tag):
    """Adapted from @Logan-Lin (github)"""

    output_file = open(output_filename, "w")    
    lines = markdown_strings.split('\n')
    
    if lines[len(lines) - 1] is not '':
        lines.append('')

    header_indexes = find_all(lines, header_tag)
    headers = []

    # Write all lines before the sorting needs to occur
    # #lines[0:header_indexes[0]]
    # #output_file.write(lines[0] + '\n' + lines[1])
    pre_section = lines[0:header_indexes[0]]
    
    # interleave (missing) line breaks
    # ...
    # output_file.writelines(result)
    for line in pre_section:
        output_file.write('\n' + line)


    for i in range(len(header_indexes)-1):
        headers.append(lines[header_indexes[i]][len(header_tag):]) # no need of +1 because the space afte "##" is incorporated into header tag
    
    sorted_headers = sorted(headers, key=str.lower)

    for sorted_header in sorted_headers:
        index = headers.index(sorted_header)
        start = header_indexes[index]
        if index == len(header_indexes) - 1 - 1: # -1 for 0-based indexing, extra -1 beacause last entry is the start of the different heading level "# "
            # end = len(lines)
            end = header_indexes[-1]
        else:
            end = header_indexes[index + 1]
        for i in range(start, end):
            output_file.write('\n' + lines[i])
    
    # Remaining lines, after the end of the section with "###""
    for i in range(header_indexes[-1], len(lines)):
            output_file.write('\n' + lines[i])

    output_file.close()

def direct_sort(markdown_strings, output_filename, header_tag):
    """Original sorting function by @Logan-Lin (github)"""
    output_file = open(output_filename, "w")
    lines = markdown_strings.split('\n')
    
    if lines[len(lines) - 1] is not '':
        lines.append('')
   
    header_indexes = find_all(lines, header_tag)
    headers = []
    
    # Write all lines before the sorting needs to occur
    # lines[0:header_indexes[0]]
    # output_file.write(lines[0] + '\n' + lines[1])
    pre_header = lines[0:header_indexes[0]]
    # interleave (missing) line breaks
    result = [None] * (len(pre_header)*2 - 1)
    result[::2] = pre_header
    result[1::2] = ["\n"] * (len(pre_header) - 1)
    output_file.writelines(result)

    for i in range(len(header_indexes)):
        headers.append(lines[header_indexes[i]][len(header_tag) + 1:])
    sorted_headers = sorted(headers)
    
    for sorted_header in sorted_headers:
        index = headers.index(sorted_header)
        start = header_indexes[index]
        if index == len(header_indexes) - 1:
            end = len(lines)
        else:
            end = header_indexes[index + 1]
        for i in range(start, end):
            output_file.write('\n' + lines[i])
    
    output_file.close()


def file_sort(input_filename, output_filename, header_tag):
    # file = open(input_filename + ".md", "r")
    # if file is None:
    #     return False
    # strings = ''
    # line = file.readline()
    # while line != '':
    #     strings += line
    #     line = file.readline()
    with open(input_filename, "r") as inputfile:
        strings = inputfile.read()
    sort_subsection(strings, output_filename, header_tag)
    # file.close()
    return True


def find_all(string_array, sub_string):
    indexes = []
    for i in range(len(string_array)):
        # if string_array[i].find(sub_string) != -1:
        if string_array[i].startswith(sub_string): # != -1:
            indexes.append(i)
    
    
    # obtain index of the next closest heading tag
    for i in range(indexes[-1]+1, len(string_array)):
        # if string_array[i].find("# ") != -1:
        if string_array[i].startswith("# "): # != -1:
            indexes.append(i)
            break
    
    return indexes


output_name = 'output'
input_name = 'input'
header_tag_num = '3'
if '--input' in sys.argv:
    input_name = sys.argv[sys.argv.index('--input') + 1]
if '--output' in sys.argv:
    output_name = sys.argv[sys.argv.index('--output') + 1]
if '--header' in sys.argv:
    header_tag_num = sys.argv[sys.argv.index('--header') + 1]

header = '#' * int(header_tag_num) +  " "
result = file_sort(input_name, output_name, header)

if result is True:
    print("Sort success! Sorted markdown file is saved to " + output_name)
else:
    print("Sort failed.")