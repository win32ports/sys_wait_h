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
