from subprocess import check_output

version = '"{}"'.format(check_output(['git', 'describe']).decode('utf-8').strip().replace('v',''))

with open('setup.py', 'r') as setup_file:
    setup_text = setup_file.read().format(VERSION=version)
    
setup_text.format(version=version)
with open('setup.py', 'w') as setup_file:
    setup_file.write(setup_text)