# %% [markdown]
# # OS Python prac
#

# %%
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

os.remove('one', )  # os.unlink('path')
os.removedirs('../new')
os.rmdir('Test')

os.path.join(os.path.dirname('one'))
# converts relative pathname to absolute

os.rename('srcDir', 'dstDir', src_dir_fd=None, dst_dir_fd=None)
os.renames('oldName', 'newName')

os.removedirs('../.venv/pipCache/http/')


# %%
os.path.join('../sample1/', 'sample3/')


# %%
os.renames('../Docs2/OsScriptDoc.md', '../Docs2/os_install.md')


# %%
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
os.statvfs('sysprac.ipynb')
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

# %% [markdown]
# execl() command format:
#
# ```py
# execl(file: StrOrBytesPath, __arg0: StrOrBytesPath, *args: StrOrBytesPath)
#
# # Other options:
#
# execvpe() | execlpe()
#
# # Exit the command by calling
#
# sys.exit() | os._exit(n) | os.abort()
# ```
#

# %%


def run_exe():
    os.execl('./openPrac.py', './dev.env')


sys.exit()


# %% [markdown]
# # Exec command
#
# - exec: runs a new program, while replacing the current one
# - won't return anything if data is buffered on the open files
# - data can be flushed by running the cmds below prior to next exec func call
#
# ```py
# sys.stdout.flush() | os.fsync()
#
# content = run_exe().getvalue()
# ```
#

# %%

output = io.StringIO()
output.write('line one.\n')
print('line two.', file=output)

content = output.getvalue()
# close obj & discard mem buff
output.close


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


# %%
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
