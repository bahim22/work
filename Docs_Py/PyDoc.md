
# Python Base Info

## Terms
<!-- cspell: disable  -->

1. High-level language and program written in C that interprets the source code, parses it (examine/analyze syntactic structure) and processes it
2. semantic: meaning of a prog.
3. syntax: rules that define the structure of the lang.
4. Translator types:
   1. interpreters: executes prog. in high level lang by translating 1 line at a time
   2. compilers: get's the prog. file, then runs a process to translate the high-level source code into machine language; afterwards it puts it into a file to be executed later in .exe or .dll files (executable and dynamic link library)
   3. machine code/low-level lang/assembly lang: the lowest level lang. for software that's directly executed by CPU
5. programs (py statements crafted to do a task) are saved to files called scripts and called by running: python <filename.py>
6. variable: a name that refers to a value. An assignment statement creates new var and gives them values
7. attribute: a value associated w/ an object; referenced by using dot expression/notation (candy.sour)
8. callback: subroutine func passed as an arg. to be ee in future
9. class: a temp for making user-defined objects. Contain method def. that operate on instances of the class
10. coercion: implicit conversion of one type to another that involves 2 args of same type
11. decorator: function returning another func. (func transformation using @wrapper syntaxl ex. classmethod(), staticmethod())
12. descriptor: Any object which defines the methods __get__(), __set__(), or __delete__()
13. dictionary comprehension: A compact way to process all or part of the elements in an iterable and return a dictionary with the results.
14. dictionary view: The objects returned from dict.keys(), dict.values(), and dict.items() are called dictionary views.
15. generator: A function which returns a generator iterator. It looks like a normal function except that it contains yield expressions for producing a series of values usable in a for-loop or that can be retrieved one at a time with the next() function.
16. immutable: An object with a fixed value. Immutable objects include numbers, strings and tuples. Such an object cannot be altered
17. Mutable objects can change their value but keep their id().
18. type: The type of a Python object determines what kind of object it is; every object has a type. An object’s type is accessible as its __class__ attribute or can be retrieved with type(obj).

<!-- /* cspell: enableCompoundWords */ -->

### To-Do

- `iterable`
An object capable of returning its members one at a time. Examples of iterables include all sequence types (such as list, str, and tuple) and some non-sequence types like dict, file objects, and objects of any classes you define with an __iter__() method or with a __getitem__() method that implements Sequence semantics.

- `iterator`
An object representing a stream of data. Repeated calls to the iterator’s __next__() method (or passing it to the built-in function next()) return successive items in the stream.

- `key function`
A key function or collation function is a callable that returns a value used for sorting or ordering. For example, locale.strxfrm() is used to produce a sort key that is aware of locale specific sort conventions. A number of tools in Python accept key functions to control how elements are ordered or grouped. They include min(), max(), sorted(), list.sort(), heapq.merge(), heapq.nsmallest(), heapq.nlargest(), and itertools.groupby().

a.list

- A built-in Python sequence. Despite its name it is more akin to an array in other languages than to a linked list
  - since access to elements is O(1)
- an ordered set of items

```py
a_list = ['a']
a_list[:] # creates copy of the list
a_l = a_l + [2.0, 3]
a_l.append('dog')
a_l.extend()
```

- `list comprehension`
A compact way to process all or part of the elements in a sequence and return a list with the results.

```py
 result = ['{:#04x}'.format(x) for x in range(256) if x % 2 == 0]
"""
 generates a list of strings containing even hex numbers (0x..) in the range  0 - 255.
 The if clause is optional. If omitted, all elements in range(256) are processed.
"""
```

- `mapping`
A container object that supports arbitrary key lookups and implements the methods specified in the Mapping or MutableMapping abstract base classes. Examples include dict, collections.defaultdict, collections.OrderedDict and collections.Counter.

- `method`
A function which is defined inside a class body. If called as an attribute of an instance of that class, the method will get the instance object as its first argument (which is usually called self).

- `sequence`
An iterable which supports efficient element access using integer indices via the __getitem__() special method and defines a __len__() method that returns the length of the sequence. Some built-in sequence types are list, str, tuple, and bytes. Container w/ items stored in deterministic ordering

- `set comprehension`
A compact way to process all or part of the elements in an iterable and return a set with the results. results = {c for c in 'abracadabra' if c not in 'abc'} generates the set of strings {'r', 'd'}

```py
def f(arg):
    ...
f = staticmethod(f)

@staticmethod
def f(arg):
    ...

(int(3.15)) # converts floating pt # to integer 3
```

## Argument passing

- script name and add'l args are turned into a list of `str` then assigned to `argv` var. in `sys` module

- Shebang lines

- file starts with #!
- Linux/Unix OS have native support and the py launcher allows use with Py scripts on W10.
- virtual commands include
<!-- cspell: disable  -->

> /usr/bin/env python, /usr/bin/python, /usr/local/bin/python, python

```py
#! /usr/bin/python || usr/bin/python -v || ./.myvenv/Scripts/python.exe
```

## virtual env creation

```ps1
python3 -m venv /path/to/new/virtual/environment
c:/Python35/python -m venv c:/path/to/myenv
python -m venv c:/path/to/myenv
python -m venv -h
<venv>\Scripts\Activate.ps1
venv/Scripts/Activate.ps1
<venv>/bin/Activate.ps1
venv [-h] [--system-site-packages] [--symlinks | --copies] [--clear]
            [--upgrade] [--without-pip] [--prompt PROMPT] [--upgrade-deps]
            ENV_DIR [ENV_DIR ...]
```

```bash
source <venv>/bin/activate
venv\/Scripts\/activate.bat
venv\/Scripts\/activate.bat

source "c:/Users/uname/OneDrive -PPU/uname @PPU/moons/.venv/Scripts/activate"
source /home/ib-ub/flow/work/.venv/bin/activate
```

- positional args: ENV_DIR: a dir to create the environment in.
- optional args
- -h || --help
- --system-site-packages (give access to system site-pack dir.)
- --symlinks
- --copies
- --clear (delete contents of the env dir before creation)
- --upgrade (upgrade env dir to use newer v of py)
- --upgrade-deps (upgrade cored deps & pip setuptools)
- --prompt PROMPT (set an alt prompt prefix for the env)

```sh
pip install --upgrade-strategy eager --report ./PipRep.json --cache-dir ./.venv/pip_cache -r ./requirements.txt

pip install --require-virtualenv --python-version "3.10.0" --pre --upgrade
# only install in venv, use py -v, use pre-release -v, upgrade packages (-u), isolated mode ignores env var and user config
# --user Install to the Python user install dir Linux: ~/.local/, or W10:%APPDATA%\Python

# ERROR: When restricting platform and interpreter constraints using --python-version, --platform, --abi, or --implementation,
    # either --no-deps must be set, or --only-binary=:all: must be set and --no-binary must not be set (or must be set to :none:).
pip install --python "3.8"
#  run w/ specified python interpreter
pip install --dry-run --ignore-installed
# don't install and resolve the requirements, can use --report <file_name> to check what pip did to install req
pip install -r requirements.txt
pip install --use-feature no-binary-enable-wheel-cache truststore fast-deps
pip cache <dir, info, list, purge, remove>
pip config # (debug, edit, get, list, set, unset)
python3 -m pip install --upgrade flake8 autopep8 --upgrade-strategy=eager
# upgrade pack to latest
--no-binary <format_control> ":all:" # don't use legacy binary packs
--no-deps # don't install deps
--use-pep517  # Use PEP 517 for building source distributions
--compile # compile/don't compile Py source fi to bytecode
--check-build-dependencies  # Check the build dependencies when PEP517 is used.
--config-settings <KEY=VALUE>
pushd "$(mktemp -d)"
time python -m pip install \
      --no-cache-dir \
      --force-reinstall \
      --only-binary=cryptography \
      cryptography
# curl
curl --dns-servers 1.1.1.1,1.0.0.1 --compressed -o $file -# $url
```

## Pip commands

| Commands | info |
| --- | --- |
|  install  | Install packages.|
|  download | Download packages.|
|  uninstall  | Uninstall packages.|
|  freeze | Output installed packages in requirements format.|
|  inspect | Inspect the python environment.|
|  list   | List installed packages.|
|  show   | Show information about installed packages.|
|  check  | Verify installed packages have compatible dependencies.|
|  config | Manage local and global configuration.|
|  search | Search PyPI for packages.|
|  cache  | Inspect and manage pip's wheel cache.|
|  index  | Inspect information available from package indexes.|
|  wheel  | Build wheels from your requirements.|
|  hash   | Compute hashes of package archives.|
|  completion | A helper command used for command completion.|
|  debug | Show info useful for debugging.|

## system

```py
import sys
sys.path
```

```sh
where python && which python
```

## Print

```py
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
```

- Prints the values to a stream, or to sys.stdout by default
- Optional keyword arguments:
  - file: a file-like object (stream); defaults to the current sys.stdout.
  - sep: string inserted between values, default a space.
  - end: string appended after the last value, default a newline
  - flush: whether to forcibly flush the stream.

## Class

```py
int([x]) -> integer int(x, base=10) -> integer
# Convert a number or string to an integer
```

## Sequence types: strings, lists, tuples, bytes sequences, bytes arrays, range() objects

### Strings
<!-- cspell: disable  -->

- `'str'.join`

Concatenate any number of strings.

The string whose method is called is inserted in between each given string. The result is returned as a new string.

```py
Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
```

- `'str'.format()`
S.format(*args, **kwargs) -> str
Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

- `'str'.split()`
S.format(*args, **kwargs) -> str
Return a formatted version of S, using substitutions from args and kwargs. The substitutions are identified by braces ('{' and '}').

- `'str'.lstrip()`
Return a copy of the string with leading whitespace removed.
- `'str'.upper()` | `'str'.capatilize()` to cap only first letter in str
Return a copy of the string converted to uppercase.
- 'str'.isupper, isalphanum, isnumeric, isalpha, isdigit etc.
  - returns True or False

- Use double quotes, or an escape char (\)
  - Everything inside the double quote will be printed to stdout
- \n for new line
  - use print() func for \n to work
- raw string: add r before the first quote so chars prefaced by \ aren't viewed as special chars
- triple quotes allow string literals to span multiple lines
  - use \ to prevent the end of line at start
- in indexing and slicing
  - start is always included, and the end always excluded.
  - an omitted first index defaults to zero, an omitted second index defaults to size of the string being sliced

```py
'hasn\'t'
"hasn't"
print('''\
    Topic: Python
    Date: Oct. 06
''')
print(r'C:\some\name')
```

## File Handling

- "r" Read - default value; Opens a file for reading, error if file !exist
- "a" Append - opens for appending; creates if !exist
  - open for writing, appending to the end of the file if it exists
- "w" write - opens a file for writing and creates if it doesn't exit
  - truncating the file first
- "x" Create - creates specified file; error if file == exist
  - can specify if file should be handled as binary(ex. images) or text mode
- 'b' binary mode
- 't' text mode (default)
- '+' open a disk file for updating (reading and writing)

```py
f = open("demo.txt")
print(f.read())

def ex_pr(file):
  return print(f.readline('file'))

fa = open("D:/Docs/welcome.txt", "r")
print(f.read(5))
# open and read file => view first 5 chars

fa.close()
```

----------

## API Info

1. Bus info to practice requests [PortAuthority][stop_times]

[stop_times]: https://stoptimes.portauthority.org/default?address=345%20Sixth%20Ave%2015222
