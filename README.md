# pyls

[Features](https://github.com/yusha-g/pyls?tab=readme-ov-file#features)

[Code Structure](https://github.com/yusha-g/pyls?tab=readme-ov-file#code-structure)

[Setup](https://github.com/yusha-g/pyls?tab=readme-ov-file#setup)


# Features

Mimics the behaviour of `ls` command

The following arguments are implemented and categorised under argument group “pyls flags”:

| Arg | Description |
| --- | --- |
| -A | List all files, including the once starting with “.” |
| -l | Long list files with details such as `size` and `time_modified` |
| -r | Reverse listing of files |
| -t | Sort files by `time_modified` |
| -h | Makes file sizes human readable |
| --filter=<dir/file> | Filter based on content. If item contains contents, it is classified as a directory (dir), else it is a file. |
| path | Path to list out. |

All flags are stackable. 

# Code Structure

```

# basic structure of code
pyls
|-- src
    |-- pyls
        |-- json
            |-- structure.json
        |-- __init__.py
        |-- custom_exception.py
        |-- item.py
        |-- pyls_argument.py
        |-- pyls.py
|-- test
```

### pyls_arguments

Contains function to add above mentioned arguments. 

### pyls

Entrypoint

Loads the `structure.json` file and creates corresponding `Item`.

Based on provided argument, is extracts list of contents from inside an Item and displays it accordingly. 

### item

Contains structure of each item. 

Depending on the presence of `contents` inside of an item — it can be classified as either a directory or a file. 

### custom_exception

Currently only contains exception for InvalidPath which is raised if the path passed in args is not found. 

# Setup

- In terminal, navigate to `pyls/src/pyls`
- Run the following command

```bash
./pyls.py
```

- pyls is now executable as follows:

```bash
python -m pyls
```

Note:

- The above command will only work inside the pyls folder.
- This is a temporary workaround till I can figure out the error caused by `pyproject.toml`'s pip install.