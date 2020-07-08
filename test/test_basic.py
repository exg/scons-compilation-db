import json


def test_basic(scons_runner, test_dir):
    scons_runner("sconstruct_basic")
    with open(str(test_dir / "compile_commands.json")) as f:
        compilation_db = json.load(f)
    assert compilation_db == [
        {
            "command": "gcc -o a.o -c a.c",
            "directory": str(test_dir),
            "file": str(test_dir / "a.c"),
        },
    ]
