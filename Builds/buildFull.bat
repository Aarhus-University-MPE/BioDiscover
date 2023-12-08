"C:\Program Files\7-Zip\7z.exe" a "Installer.7z" -t7z ".\bin\Installer"
"C:\Program Files\7-Zip\7z.exe" a "Update.7z" -t7z ".\bin\Update"
copy /b .\config\7zSD.sfx + .\config\configFull.txt + Installer.7z Installer.exe
copy /b .\config\7zSD.sfx + .\config\configUpdate.txt + Update.7z Update.exe
del "./Installer.7z"
del "./Update.7z"
pause