import subprocess

if input('Are you sure you want to delete the windows folder\nIt may damage you computer (y/n)') == 'y':
    if input('Last Warning. Are you sure you want to delete the windows folder\nIt may damage you computer (y/n)') == 'y':
        subprocess.call(['runas', '/user:Administrator', '"rmdir /s /q C:\Windows"'])
