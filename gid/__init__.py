import os

root = "/usr/local/src"
if "XDG_SRC_HOME" in os.environ:
	root = os.environ["XDG_SRC_HOME"]

def path2gid(proj):
	return str(proj.relative_to(root))

def gid2c(s, style, cident):
	s = s.replace(".", "")
	match style:
		case "camel":
			s = s.split("/")
			s = [x.capitalize() for x in s]
			s = "".join(s)
			if cident and s[0].isdigit():
				s = f"c{s}"
		case "snake":
			s = s.replace("/", "_")
			if cident and s[0].isdigit():
				s = f"c_{s}"
		case x:
			raise Exception(x)
	return s
