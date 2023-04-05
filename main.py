import os
import sys
import time
from datetime import datetime
import pyautogui as auto

A = True


# Adding a way to add projects into a secondary folder.

htmlfile_text = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <script src="index.js"></script>
    <title>Document</title>'''

flask_file_text = '''from flask import Flask
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()'''



def ask_for_project():
    askforp = input("Include HTML, CSS and JavaScript files? y/n:")
    if 'y' in askforp:    
            # note_directory = 'Desktop/Projects/Web_Projects'

            html_file = open(f'Desktop/Projects/Web_Projects/{name2}/index.html', 'w')
            html_file.write(htmlfile_text)
            html_file = open(f'Desktop/Projects/Web_Projects/{name2}/style.css', 'w')
            html_file = open(f'Desktop/Projects/Web_Projects/{name2}/index.js', 'w')
            askforflask = input('Add Python Flask framework files? ')
            if 'y' in askforflask:
                os.mkdir(f'Desktop/Projects/Web_Projects/{name2}/templates')
                os.mkdir(f'Desktop/Projects/Web_Projects/{name2}/static')
                app_file = open(f'Desktop/Projects/Web_Projects/{name2}/app.py', 'w')
                app_file.write(flask_file_text)
                app_file.close()
                os.system(f'python3 -m venv Desktop/Projects/Web_Projects/{name2}')
                print('done')
                
    elif 'y' not in confirm2:
        pass
    elif 'n' in confirm2:
        sys.exit()

    
def script():
    while A:
        name = input('Name of the Project: ')
        confirm = input("Make the file? y/n: ")
        if 'y' in confirm:
        # The directory has to be /Users/macbook/, Where i will be storing the code        
            dir = 'Desktop/Projects/Python_Projects'
            x1 = os.path.join(dir, name)
            os.makedirs(x1)
            # note_directory = 'Desktop/Projects/Python_Projects'
            f1 = open(f'Desktop/Projects/Python_Projects/{name}/date.txt', 'w')
            now = datetime.now()
            f1.write(f'Created at {now}')
            f1.close()
            x = input("Open in Visual Studio Code? y/n: ")
            if 'y' in x:
                auto.typewrite(f'cd Desktop/Projects/Python_Projects/{name}')
                auto.hotkey('enter')
                time.sleep(2)
                os.system('code .')
                auto.hotkey('enter')
            else:
                print(f'OK, file created')
                sys.exit()
            sys.exit()
        else:
            print("Aborted")
            sys.exit() 

    def vscode():
            # This function is later called in the script
            x = input("Open in Visual Studio Code? y/n")
            if 'y' in x:
                auto.typewrite(f'cd Desktop/Projects/Python_Projects/{name}')
                auto.hotkey('enter')
                time.sleep(2)
                auto.typewrite('code .')
                auto.hotkey('enter')
            else:
                print(f'OK, file created')
                sys.exit()


def web_app():
        global name2
        name2 = input('Name of the Project: ')
        confirm = input("Make the file? y/n: ")
        if 'y' in confirm:    
            dir2 = 'Desktop/Projects/Web_Projects'
            x2 = os.path.join(dir2, name2)
            os.makedirs(x2)
            # note_directory = 'Desktop/Projects/Web_Projects'
            f2= open(f'Desktop/Projects/Web_Projects/{name2}/date.txt', 'w')
            now2 = datetime.now()
            f2.write(f'Created at {now2}')
            f2.close()
            ask_for_project()
            x3 = input("Open in Visual Studio Code? y/n: ")
            if 'y' in x3:
                auto.typewrite(f'cd Desktop/Projects/Web_Projects/{name2}')
                auto.hotkey('enter')
                time.sleep(1)
                auto.typewrite('code .')
                auto.hotkey('enter')
            else: 
                print(f'OK, file created')
                sys.exit()
        else:
            print("Aborted")
            sys.exit() 
     




def which_folder():
    x1 = input('''What type of project? 
1. Script/Code
2. Web Development/Web App''')   
    if '1' in x1:
        script()
    else:
        if '1' not in  x1:
            print(' ')
    if '2' in x1:
        web_app()
    
if __name__ == "__main__":
    which_folder()
