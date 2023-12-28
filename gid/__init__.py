import os

root = "/usr/local/src"
if "XDG_SRC_HOME" in os.environ:
	root = os.environ["XDG_SRC_HOME"]

def path2gid(proj):
	result = []
	if not proj.is_relative_to(root):
		return None
	for idx, path in enumerate(proj.relative_to(root).parts):
		assert len(path) > 0
		word = path.lower()
		if idx == 0:
			for field in reversed(list(word.split("."))):
				assert field.isalnum()
				result.append(field)
			continue
		else:
			assert path.isalnum()
		result.append(word)
	assert result[0][0].islower()
	return result

def gid2c(gid, style):
	assert isinstance(gid, list)
	assert len(gid) >= 1
	result = ""
	for idx, word in enumerate(gid):
		assert len(word) > 0
		if idx == 0:
			assert word[0].islower()
		else:
			if style == "camel" and word[0].isdigit():
				result += "_"
		if style == "camel":
			result += word.capitalize()
		elif style == "snake":
			if idx > 0:
				result += "_"
			result += f"{word}"
		else:
			raise Exception(style)
	return result
