import sys


# ctrl+D посылает EOF
content = sys.stdin.read()

print(len(content.split()), 'слов')

# piping
# windows
# type 6_oop\PRACTICE.txt | python 7_files\2_stdin_stdout.py
# unix
# cat 6_oop\PRACTICE.txt | python 7_files\2_stdin_stdout.py
