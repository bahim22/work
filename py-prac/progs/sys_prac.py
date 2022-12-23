# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% [markdown]
# # OS Python prac
#

# %%
import time
import io
import sys
import getpass
import os

# getpass.getuser()
os.uname()


# %%
os.getcwd()


# %%
os.lstat(os.getcwd())


# %%
# from os import mkdir

os.makedirs('one', mode=0o777, exist_ok=False)
os.mkdir('../new')

os.remove('one')  # os.unlink('path')
os.removedirs('../new')
os.rmdir('test')

# os.path.join(os.path.dirname('one'), result)
# convert relative pathname to absolute

os.rename('srcDir', 'dstDir', src_dir_fd=None, dst_dir_fd=None)
os.renames('oldName', 'newName')


# %%
# from os import mkdir

os.makedirs('one', mode=0o777, exist_ok=False)
os.mkdir('../new')

os.remove('one', )  # os.unlink('path')
os.removedirs('../new')
os.rmdir('Test')

os.path.join(os.path.dirname('one'))
# converts relative pathname to absolute

os.rename('srcDir', 'dstDir', src_dir_fd=None, dst_dir_fd=None)
os.renames('oldName', 'newName')

os.removedirs('../.venv/pipCache/http/')

os.path.join('../sample1/', 'sample3/')


# %%


# %%
os.renames('prac9.ipynb', 'sysprac.ipynb')
os.renames('../Docs2/OsScriptDoc.md', '../Docs2/os_install.md')

# os.renames('prac9.ipynb', 'sysprac.ipynb')
os.renames('prac01_1.ipynb', 'file_open.ipynb')


# %%
# scan dir for files and print output

# os.scandir('../new') |

with os.scandir(os.getcwd()) as sc_it:
    for file_name in sc_it:
        if not file_name.name.startswith('.') and file_name.is_file():
            print(file_name)


# %%

statinfo = os.stat('dev.env')
print(statinfo, sep='next item: ')
# print(statinfo.st_size)

# %% [markdown]
# os.stat_result class is an object that has attributes that correspond w/ stat structure
#
# - st_mode = file mode, permissions
# - st_uid<gid> = user id of file | group owner
# - st_size = size in bytes
# - st_atime,mtime, atime_ns, birthtime, creator, type
#

# %%
os.statvfs('./')
# returns object whose attributes describe fs (statvfs structure)


# %%
os.symlink('src', 'dst')


# %%
os.walk('top', topdown=True, onerror=None, followlinks=False)
# create filenames in dir tree; yields 3-tuple (dirpath, dirnames, filenames)
os.path.join('dirpath', 'name')
# get full path to file or dir in dirpath attributes

# %% [markdown]
# # Process Management
#

# %%


def run_exe():
    os.execl('./openPrac.py', './dev.env')


sys.exit()

# os._exit(n)
# or os.abort()

# execvpe, execlpe
# execl(file: StrOrBytesPath, __arg0: StrOrBytesPath, *args: StrOrBytesPath)

'''
exec new program, replacing current one and don't return
if data is buffered on the open files, flush them w/ sys.stdout.flush() or os.fsync() prior to next exec func call

content = run_exe().getvalue()
'''


# %%

output = io.StringIO()
output.write('line one.\n')
print('line two.', file=output)

content = output.getvalue()
output.close  # close obj & discard mem buff

# %% [markdown]
# # Misc OS interfaces
#
# ```py
# import os
#
# os.kill(__pid: int, __signal: int, /)
#
# os.startfile(path[, operation][, arguments][, cwd][, show_cmd])
# os.system('command')
# os.times()
# ```
#

# %%
os.cpu_count()  # 12 return n of CPUs in system
len(os.sched_getaffinity(0))  # n of usable CPUs
os.confstr_names  # dict mapping names accepted by confstr() to the int val defined for the names by the host OS
os.getloadavg(), os.sysconf('name'), os.sysconf_names


# %%
os.getrandom(size=888, flags=0), os.urandom(1024)


# %%

os.remove('../requirements3.txt')
os.removedirs('./Dirname')
os.renames('../PipRep.json', '../.venv/Reports')

# To-Do: Need to decide what I want it to do and adjust


def try_path(head, tail):
    # old = str(input('Enter # of hours worked per week: '))
    old = str(input('Enter name of old dir: '))
    new = str(input('Enter new name for old dir: '))
    if head and tail and not os.path.exists(head):
        os.makedirs(head)
    os.rename(old, new)
    head, tail = os.path.split(old)
    if head and tail:
        print('file renamed')


# %%
def os_info():
    return os.uname(), os.getpid(), os.getuid()


os_info()


# %%


def dir_info(dir=os.getcwd(), file='./convFunc.ipynb'):
    opath = os.path
    return opath.isdir, opath.curdir, opath.getsize(file)


# %%
dir_info()


# %%


def dir_info2(req_dir, dir='/home/ib-ub/flow/work', file='./convFunc.ipynb'):
    opath = os.path
    # new_dir(req_dir, dir)
    cwdir = os.getcwd()
    if opath.isdir(cwdir):
        return opath.curdir, opath.getsize(file)
    else:
        print(f'Directory: {cwdir} doesn\'t exist')


# %%
dir_info2(req_dir='dev.env')


# %%
def new_dir(dir_name, req_dir=''):
    if dir_name != os.getcwd():
        base_dir = os.path.join(dir_name, req_dir)
    else:
        base_dir = req_dir + dir_name
        if os.path.isdir(base_dir):
            isDir = print(f'Directory: {base_dir} exists')
        else:
            isNotDir = print(f'{base_dir} doesn\'t exist')


new_dir('/home/ib-ub/flow/work', req_dir='Docs2/')


# %%
def new_dir(dir_name, req_dir=''):
    if dir_name == os.getcwd():
        base_dir = os.path.join(dir_name, req_dir)
    else:
        base_dir = dir_name + req_dir
    print(f'{base_dir}')


# %%
def new_dir(dir_name=os.getcwd(), req_dir=''):
    if dir_name == os.getcwd():
        base_dir = os.path.join(dir_name, req_dir)
    else:
        base_dir = dir_name + req_dir
        return os.path.isdir(base_dir)
    print(f'{base_dir}')


# %%
new_dir(dir_name=os.getcwd(), req_dir='dev.env')


# %%
new_dir(dir_name=os.getcwd(), req_dir='dev.env')


# %%
def new_dir(dir_name=os.getcwd(), req_dir=''):
    if dir_name == os.getcwd():
        base_dir = os.path.join(dir_name, req_dir)
    else:
        base_dir = dir_name + req_dir
    print(f'{os.path.isdir(base_dir)}')
    print(f'{base_dir}')
    print(f'{base_dir} is not a dir')


# %%
new_dir(req_dir='dev.env')


# %%
dir_info2('./black')


# %%
dir_info('./black')


# %%
# def get_file_time(file, opath):
#     file_info = opath.getmtime(file)
#     print(time.ctime.file_info)


def get_file_time(file='./dev.env', opath=os.path):
    file_info = opath.getmtime(file)
    # print(time.ctime(file_info))
    return time.ctime(file_info)


get_file_time()


# %%
get_file_time('prac9.ipynb')
