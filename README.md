# SCons Compilation Database Tool

scons-compilation-db is a SCons tool to generate a database of
compilation commands for `C` and `C++` build targets in the format
introduced by Clang:

https://clang.llvm.org/docs/JSONCompilationDatabase.html

# Usage

The tool extends a SCons environment with three methods:

- `CompilationDB(path)` - writes the compilation commands for the
  targets defined at the time of the call to the file named by the
  path argument
- `GetCompilationDB()` - returns the compilation database
- `SetCompilationDB(db)` - sets the compilation database using a value
  returned by `GetCompilationDB`

The methods to get and set the compilation database can be used to
merge the compilation databases of two or more environments. For example:
```
a = Environment(tools=["default", "scons_compilation_db"], toolpath=["."])
a.Program("a.c")
b = Environment(tools=["default", "scons_compilation_db"], toolpath=["."])
b.SetCompilationDB(a.GetCompilationDB())
b.Program("b.c")
b.CompilationDB("compile_commands.json")
```
