import json


def test_multi(scons_runner, test_dir):
    scons_runner("sconstruct_multi")
    with open(str(test_dir / "compile_commands.json"), "rb") as f:
        compilation_db = json.load(f)
    assert compilation_db == [
        {
            "command": "gcc -o a.o -c a.c",
            "directory": str(test_dir),
            "file": str(test_dir / "a.c"),
        },
        {
            "command": "g++ -o b.o -c b.cpp",
            "directory": str(test_dir),
            "file": str(test_dir / "b.cpp"),
        },
    ]
