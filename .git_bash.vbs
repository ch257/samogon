Set objShell = WScript.CreateObject("WScript.Shell")
objShell.Run "cmd /c cd /D c:\Churilin\Progs\Portable\PSBQuik\", 0, True
objShell.Run "cmd /c C:\Churilin\Progs\Portable\PortableGit\git-bash.exe", 0, True
Set objShell = Nothing