@echo off 
reg add "hkcu\control panel\desktop" /v wallpaper /d %cd%\bg\bg.png /f 
RunDll32.exe USER32.DLL,UpdatePerUserSystemParameters
exit
