# from datetime import date
import os
import time

"""
path = "C:\\Users\\Ibalde\\deleteTest\\PracMain/"
{
    "path": "C:/Users/Ibalde/OneDrive-PointParkUniversity/Ibrahima/
    @PointParkUniversity/OneNote_RecycleBin",
    "pcName": "ITS-TH220-02"
}
"""

path = "C:/Users/Ibalde/deleteTest/"

files = os.listdir(path)

now = time.time()
# n = input(int)
# original var; n_days = input(int()) * 86400
# n_days *= 86400
n_days = now * 86400
for f in files:
    filepath = os.path.join(path, f)
    if not os.path.isfile(path):
        continue
    if os.stat(filepath).st_mtime < now - n_days:
        os.remove(filepath)

"""
items = [1,2,3,4]
for item in items:
    if item == 2:
        continue
    print(item)

items = [1,2,3,4]
for item in items:
    if item == 2:
        break
    print(item)
"""


def create(self, env_dir):
    """
    Create a virtualized Python environment in a directory.
    env_dir is the target directory to create an environment in.
    """
    env_dir = os.path.abspath(env_dir)
    context = self.ensure_directories(env_dir)
    self.create_configuration(context)
    self.setup_python(context)
    self.setup_scripts(context)
    self.post_setup(context)
