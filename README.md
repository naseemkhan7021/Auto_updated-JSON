# Auto_updated-JSON  Main work
Using the python make the JSON auto apdated. 
Data will be related to the file info like modifie data, created data, file name and more you can add.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install schedule.

```bash
pip install schedule 
```

## How to use
make folder where you can store any type of file
in my case
```python
newfils = os.listdir('jsonfiles')
```
you can change the file name
```python
newfils = os.listdir('you_folder_name')
```
and run the programe. Then try to add some file in that folder.
Then you will see that the details of the files are being added to your JSON file.
