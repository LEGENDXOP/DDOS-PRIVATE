# starter file

import subprocess

def runMyFile():
    tries = 0
    while tries < 5:
        try:
            result =  subprocess.run(["python3", "m.py"], capture_output=True, text=True)
            print(result.stdout)
        except Exception as e:
            print(e)
            tries += 1

runMyFile()
