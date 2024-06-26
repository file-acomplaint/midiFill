import os

for dir in os.walk("data"):
    for filename in dir[2]:
        pathname = os.path.join(dir[0], filename)
        if not "." in pathname:
            os.rename(pathname, pathname + ".midi")