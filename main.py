import os, time, wget
from os import path, access, R_OK

windows_prog = "notepad.exe"
download_location = "ftp://ftp.f-secure.com/support/tools/fsdiag/"
support_tool = "fsdiag_standalone.exe"
tool_logfile = "fsdiag.zip"


def program_dowmload(location, tool):
    get_file = wget.download(location + tool)
    return get_file


def program_executor(program):
    os.system("start " + program)


def program_killer(program):
    time.sleep(3)
    os.system("taskkill /im " + program + " /f")


def check_logfile(logfile):
    location = path.expanduser('~/Desktop/' + logfile)
    if path.isfile(location) and access(location, R_OK):
        return ("File exists and is readable")
    else:
        return ("File is missing or is not readable")


if __name__ == '__main__':

    file_name = program_dowmload(download_location, support_tool)

while not file_name:
    time.sleep(0.1)

print("1. Tool " + file_name + " is loaded")

program_executor(windows_prog)

print("2. Program " + windows_prog + " is loaded")

program_executor(support_tool)

print("3. Program " + support_tool + " is loaded")

program_killer(windows_prog)

time.sleep(5)

verification_result = check_logfile(tool_logfile)

print("4. " + verification_result)
