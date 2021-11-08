import json
import os


def test_rebuild_no_change(scons_runner, test_dir):
    scons_runner("sconstruct_basic")
    db_path = str(test_dir / "compile_commands.json")
    with open(db_path, "rb") as f:
        compilation_db = json.load(f)
        info = os.stat(f.fileno())
    assert compilation_db == [
        {
            "command": "gcc -o a.o -c a.c",
            "directory": str(test_dir),
            "file": str(test_dir / "a.c"),
        },
    ]
    scons_runner("sconstruct_basic")
    assert os.stat(db_path) == info


def test_rebuild(scons_runner, test_dir):
    scons_runner("sconstruct_basic")
    db_path = str(test_dir / "compile_commands.json")
    with open(db_path, "rb") as f:
        compilation_db = json.load(f)
    assert compilation_db == [
        {
            "command": "gcc -o a.o -c a.c",
            "directory": str(test_dir),
            "file": str(test_dir / "a.c"),
        },
    ]
    scons_runner("sconstruct_basic", ["CCFLAGS=-O2"])
    with open(db_path, "rb") as f:
        compilation_db = json.load(f)
    assert compilation_db == [
        {
            "command": "gcc -o a.o -c -O2 a.c",
            "directory": str(test_dir),
            "file": str(test_dir / "a.c"),
        },
    ]
