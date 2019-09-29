import sys
import os

from cx_Freeze import setup, Executable

with open("tsu/__init__.py", "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip(" '\"")
            break
    else:
        version = "0.0.1"
progName = "tsu"
libName = "tsuexec"

if os.environ["TSU_ENV"] == "dev":
    progName = "tsudev"
    libName = "tsuexec-dev"

options = {
    "build_exe": {
        "optimize": 2,
        "includes": ["consolejs", "docopt"],
        "namespace_packages": ["ruamel.yaml"],
    }
}

executables = [Executable(script="tsu/main.py", targetName=progName,)]

setup(
    name=libName,
    version=version,
    description="tsu - A script to run shell in stuff",
    executables=executables,
    options=options,
)
