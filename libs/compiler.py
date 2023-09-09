import os

def compile(c_file: str) -> str:
    """From a given file written in c compile and return the new path to execute ctype"""
    path, _ = os.path.splitext(c_file) # path, extension
    os_name = os.name
    if os_name == "posix": # linux
        out_path = path + ".os"
    elif os_name == "nt":
        out_path = path + ".dll"
    else:
        raise Exception("No valid S.O. Please use Linux or Windows!")
    command = f"gcc -fPIC -shared -o {out_path} {c_file}"
    os.system(command)
    return out_path