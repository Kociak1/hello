import time
from datetime import datetime

file_path = 'abc.txt'

while True:
    with open(file_path, 'a') as f:
        f.write(f'{datetime.now()}\n')
    
    # Commit changes
    from subprocess import run
    run(['git', 'add', file_path])
    run(['git', 'commit', '-m', 'Update abc.txt with current date and time'])
    run(['git', 'push'])
    
    # Wait for 20 seconds
    time.sleep(20)
