import subprocess, os, sys, fcntl

_rooptest="""export c=0; while true; do echo "count: $((++c))"; sleep 1; done"""

def foreground(command) -> str:
    cmd_out_txt=subprocess.run(command, shell=True, capture_output=True, text=True).stdout
    return cmd_out_txt

def background(command) -> str:
    class bg_process_manager:
        def __init__(self):
            self.process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.output=""
            flag = fcntl.fcntl(self.process.stdout.fileno(), fcntl.F_GETFL)
            fcntl.fcntl(self.process.stdout.fileno(), fcntl.F_SETFL, flag | os.O_NONBLOCK)
        def is_in_progress(self) -> bool:
            return self.process.poll() is None
        def status(self) -> int | None:
            return self.process.poll()
        def kill(self) -> None:
            self.process.kill()
        def readline(self) -> str:
            btext=self.process.stdout.readline()
            if btext != b"":
                return btext.rstrip().decode()
            else:
                return ""
        def read(self) -> str:
            btext=self.process.stdout.read()
            if btext != None:
                self.output+=str(btext,encoding="utf-8")
            return self.output
        def result(self) -> str | None:
            if self.is_in_progress:
                return None
            else:
                return self.process.stdout.read().rstrip().decode()
    return bg_process_manager()
