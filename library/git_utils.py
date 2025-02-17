import subprocess, os, sys

def cmd(command) -> str:
    cmd_out_txt=subprocess.run(command, shell=True, capture_output=True, text=True).stdout
    return cmd_out_txt

def cmd_bg(command) -> str:
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        print(stderr)
        sys.exit(1)
    return stdout

