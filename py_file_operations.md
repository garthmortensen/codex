# py_file_operations.md

## Paths

Path.cwd() allows us to check our current working directory from where the Python program is executing.

Absolute filepath

``` python
from pathlib import Path

absolute_filepath = Path("/Resources/file.txt")
with open(absolute_filepath, 'r') as file:
	print(file.read()
```

Relative filepath

``` python
from pathlib import Path

cwd = Path.cwd()
print(f"Current Working Directory: {cwd}")

relative_filepath = Path("Resources/file.txt")
with open(relative_filepath, 'r') as file:
	print(file.read())
```

write to path

``` python
# Open the output_path as a file object in "write" mode ('w')
# Write a header line and write the contents of 'text' to the file
with open(output_path, 'w') as file:
    file.write("This is an output file.\n")
    file.write(text)
```

files can be read using a loop, or using write() alternative read()

``` python
line_num = 1
for line in file:
	print(f"line {line_num}: {line}")
	line_num += 1
    file.read(line)  # this might not work, but something like it does work.
```

Make relative path to current script location.

````python
import os
import pandas as pd

filepath = os.path.dirname(__file__)
filepath = os.path.join(filepath, "data", "input/")
filename = "OnlineNewsPopularity.csv"
df = pd.read_csv(filepath + filename)
````

## OS / File operations

run processes?
``` python
import subprocess
pscp_cmd = [
            "pscp",
            "server-ssh:/path/test_file1.txt",
            "C:/cats/dogs",
            ]
subprocess.run(pscp_cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE,) 
```

obtain python filesize
https://stackoverflow.com/questions/2104080/how-can-i-check-file-size-in-python

determine filesize of everything in dir
``` python
import os
filepath = "C/creds/"
for file in os.listdir(filepath):
    kb = os.path.getsize(filepath + file)
    print(kb)
```

list all files in immediate subdirectory
https://stackoverflow.com/a/10989155/5825523

``` python
import os
outbound = "C:/Outbound"	
immediate_subfolder = next(os.walk(outbound))[1]

subfolders = []
for sub in immediate_subfolder:
    subfolder = os.path.join(outbound, sub)
    subfolders.append(subfolder)

for subfolder in subfolders:
    for file in os.listdir(subfolder):
        if file.endswith(".txt"):
            print(file)
```

copy files and preserve metadata
``` python
i = 0
for subfolder in subfolders:
    for file in os.listdir(subfolder):
        if ".ORIGINAL." in file and file.endswith(".xml"):
            i += 1
            shutil.copy2(subfolder + "/" + file, filepath + file)  # copy2 preserves metadata
```

copy file from one directory to the next
``` python
for file in os.listdir(dir1):
    if file.lower().endswith('cats.xlsx'):
        copyfile(dir1 + file, dir2 + file)
```

list files in the source directory
``` python
from pathlib import Path
path_source = Path(r"C:\1999")
source_charts = []
for file in os.listdir(path_source):
    source_charts.append(file)
        pass
```

## CSV read/write

Read csv as list

``` python
from pathlib import Path
import csv

csvpath = Path('../Resources/accounting.csv')

with open(csvpath, 'r') as csvfile:

    # Pass in the csv file to the csv.reader() function
    # (with ',' as the delmiter/separator) and return the csvreader object
    csvreader = csv.reader(csvfile, delimiter=',')
    # Print the datatype of the csvreader
    print(type(csvreader))

    # Go to the next row from the start of the file
    # (which is often the first row/header) and iterate line_num by 1
    header = next(csvreader)
    print(f"{header} <---- HEADER")  # Print the header

    # Read each row of data after the header
    for row in csvreader:
        print(row)
```

write csv 1

``` python
output_path = Path('output.csv')

# Open the output path as a file object
with open(output_path, 'w') as csvfile:
    # Set the file object as a csvwriter object
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the header to the output file
    csvwriter.writerow(header)
    # Write the list of metrics to the output file
    csvwriter.writerow(metrics)
```

write csv 2

``` python
with open(path_csv + "folder_content.csv", "w") as f:
    wr = csv.writer(f, delimiter="\n")
    wr.writerow(everything)
```

write to csv 3. not the best way to do it.
``` python
filepath = "C:\\files\\"
filename = "testing.csv"

variable_1 = "a"
divide = ","
newline = "\n"

f = open(filepath + filename,'w')
f.write("field 1" + str(divide) + "field 2" + newline)  # headers
for x in [1, 2, 3, 4, 5]:
    cell1 = x
    cell3 = variable_1
    f.write(str(cell1) + str(divide) + str(cell3) + str(newline))
f.close()
```

## Archive / zip

extract zip content, unzip
``` python
import zipfile
filepath = "C:/scripts/"
filename = "file.zip"
wanted_zip_content = "file.xlsx"
with zipfile.ZipFile(filepath + filename) as zipObj:
    # extract the desired file
```

search content of zip files
``` python
from zipfile import ZipFile
indiv_file_content = []
for file in zip_files_path:
    try:
    except:
```

powershell: extract directory of zip files from source to destination
https://stackoverflow.com/questions/28448202/i-want-to-extract-all-zip-files-in-a-given-directory-in-temp-using-powershell

``` ps
Get-ChildItem 'C:\new' -Filter *.zip | Expand-Archive -DestinationPath 'D:\new\new' -Force
```

zip a df or csv
``` python
df_all.to_csv(filepath + "/" + pull_date + "_" + table + ".zip", compression=compression_options)
```

## Logging, exceptions

Standard stream: https://en.wikipedia.org/wiki/Standard_streams#/media/File:Stdstreams-notitle.svg

standard in, standard out, standard error.

### Quality logging

log exception info at CRITICAL log level
https://stackoverflow.com/a/29556251/5825523

``` python
import logging
from datetime import datetime

LOG_FILENAME = datetime.now().strftime('c:/data/logfile_%Y%m%d_%H%M%S.log')

for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)    

try:
    1/0
except Exception as e:
    logging.critical(e, exc_info=True) 
```

### Exceptions

L B Y L = look before you leap. If I add this and that, will there be an error? What if strings are fed? What if a tuple is provided? Problems! So write some code to handle it.

The pythonic way:
E A F P = Easier to Ask Forgiveness than Permission. Let plus sign do what it needs to do, but if there's a mistake, ask for forgiveness using exception handling.

If you want to take standard out, split it between 2 destinations for standard out and standard error, you can do this:

```python
try:
    convert(temps1)
    convert(temps2)
except ValueError:
    print("there was a ValueError", file=sys.stderr)
```

$ python program.py >outlog 2>errorlog

Exercise 7.1 talks about raise, and how to handle errors at multiple levels.
visual: https://en.wikipedia.org/wiki/Standard_streams#/media/File:Stdstreams-notitle.svg
https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/

sys.stdin and sys.stdout are always open. 

age = input("enter your age"). `Age = input` comes from stdin. `"enter your age"` comes from stdout.

So, this is awesome and you need to keep researching logging. TODO

Details error message and number.
```python
try:
infile = open('Incorrectfilename')
except IOError as ioe:
	print('Unable to open the file')
	print('Error number', ioe.args[0])
	print('Message', ioe.args[1])
	print('Filename in error', ioe.filename)
```

Aside: One way to read in lines of a text file.
`lines = split(filename.read())`
This removes the \n which result from .readlines()

Using finally.
```python
try:
	infile = open('C:/Course/1905/Data/simple.txt', 'r')
	try:
		print(infile.readline().rstrip())
		infile.write('line 5\n')
	except IOError:
		print('Read or Write error on file')
	finally:  # happens either way. It's guaranteed to run.
		infile.close()
except IOError as ioe:  # if infile fails
	print('Failed to open the file', ioe.args)
```
However, `finally` is complicated, nested. There's a cleaner way, which is using a "Context Manager" (`with`). The with statement wraps a block of statements with methods defined by a context manager. If you make it in, you make it out! Exceptions are delayed until you finish the block.
```python
try:
	# infile = "open file handle"
	with open('C:/Course/1905/Data/simple.txt', 'r') as infile:
		print(infile.readline().rstrip())
		infile.write('line 5\n')  # if no exception, just close anyways

# close first, then except IOError happens
except IOError as ioe:
	print('Read or Write error on file', ioe.args)
```
Much cleaner syntax. More robust. Everyone uses this now. There are other "Context Managers", __exit__, __enter__(?). However, this doesn't apply to pandas.

Open text files (not binaries) are also iterators.

### Useful automation libraries
```python
import subprocess
.Popen() - process open
.call()
.callcheck()
```

## Utililities

``` python
print memory, cpu
# https://stackoverflow.com/questions/276052/how-to-get-current-cpu-and-ram-usage-in-python
import psutil
print(int(psutil.cpu_percent()))
# you can calculate percentage of available memory
print(int(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total))
```

timer, beep, sound
``` python
import time  # for stopwatch and sleep
import winsound
t1 = time.perf_counter()
step = 1  # for logging how long it takes to run each step
timer = str(round(time.perf_counter() - t1))
timers = {step: timer}
winsound.Beep(5000, 15)  # hertz, millisec, for when you are attentive. otherwise, higher and longer
timer += 1
timers[step] = timer
winsound.Beep(5000, 15)
```

timer minimal
``` python
import time  # for stopwatch and sleep
t1 = time.perf_counter()  # track execution time
t2 = time.perf_counter()  # end of db operations
execution_time = t2 - t1  # script runs ~30 secs
print(f"\nexecution_time: {execution_time}")
```