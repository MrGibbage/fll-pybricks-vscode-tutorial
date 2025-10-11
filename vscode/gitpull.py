import subprocess

import time


def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = "{:02d}:{:02d}".format(mins, secs)
        print(timeformat, end="\r")
        time.sleep(1)
        seconds -= 1

print("git pull in five seconds")
countdown(5)
try:
    result = subprocess.run(["git", "pull"], check=True)
    if result.returncode == 0:
        print(
            f"\033[92mSuccess! Please click down here and press any key before continuing.\033[0m"
        )
except Exception as e:
    print(f"\033[91mThere was an error\033[0m")
    print(f"\033[91m{e}\033[0m")
    print(f"\033[91mPlease close and reopen VS Code\033[0m")
