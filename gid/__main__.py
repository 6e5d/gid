from pathlib import Path
from . import path2gid, gid2c

s = Path(".").resolve()
s = path2gid(s)
s = gid2c(s, "camel", True)
print(s)
