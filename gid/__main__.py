from pathlib import Path
from . import path2gid, gid2c

s = Path(".").resolve()
gid = path2gid(s)
print(gid)
s = gid2c(gid, "camel")
print(s)
s = gid2c(gid, "snake")
print(s)
