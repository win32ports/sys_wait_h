[![Build status](https://ci.appveyor.com/api/projects/status/y90h99r4gkq9x8ii?svg=true)](https://ci.appveyor.com/project/SSE4/sys-wait-h)

header-only Windows implementation of the `<sys/wait.h>` header.

tested on the following compilers:
- Visual Studio
- Clang for Windows (clang-cl)
- GCC (MinGW)

implements the following functions:
- wait
- waitpid
- waitid
- wait3
- wait4

currently, doesn't implement process group based wait.
