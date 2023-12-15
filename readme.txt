all resources/data has a gid, which is specified by the url/domain like
foo/bar/baz.
e.g. my projects should be placed under 6e5d.com/

usually most packages do not need to know their gid
as use relative path is sufficient for finding deps.
softwares like package manager, build systems etc need to know the gid
to resolve namespace properly.

This gid package provide the definition for converting local filesystem path
to the gid string(basically equivalent to domain).

It also provides some convenient function to generate c symbols:
remove all special chars and convert `/` to `_`.
It also provides a solution to the problem that c idents cannot start with digits:
if the domain starts with number(like 6e5d.com), it

* prefix snake symbol with `c_`
* prefix PascalCase symbol with `c`(c is lower case so it becomes a hint)
* avoid camelCase in c

why use `c`? because c language is responsible for this compatibility issue.
