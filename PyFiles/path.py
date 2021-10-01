import pathlib

# path of the given file
print(pathlib.Path("my_file.txt").parent.absolute())

# current working directory
print(pathlib.Path().absolute())

# the path of the given file is the teree of the branch of the commited part of the coding system
