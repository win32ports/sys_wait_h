#define _XOPEN_SOURCE 500

#include <stdlib.h>

#ifdef __MINGW32__
#include <sys/types.h>
#endif /* __MINGW32__ */

#include <sys/wait.h>

#include <windows.h>
#include <tchar.h>

void run_process(TCHAR * name)
{
    STARTUPINFO si;
    memset(&si, 0, sizeof(si));
    si.cb = sizeof(STARTUPINFO);

    PROCESS_INFORMATION pi;
    memset(&pi, 0, sizeof(pi));

    if (CreateProcess(NULL, name, NULL, NULL, FALSE, 0, NULL, NULL, &si, &pi))
    {
        CloseHandle(pi.hProcess);
        CloseHandle(pi.hThread);
    }
}

int main(int argc, char * argv[])
{
    run_process(_T("notepad.exe"));
    run_process(_T("mspaint.exe"));

    while (wait(0) > 0) {}

    return EXIT_SUCCESS;
}
