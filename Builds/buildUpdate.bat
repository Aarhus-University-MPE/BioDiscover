"C:\Program Files\7-Zip\7z.exe" a "Update.7z" -t7z ".\bin\Update"
copy /b .\config\7zSD.sfx + .\config\configUpdate.txt + Update.7z Update.exe
del "./Update.7z"
pause