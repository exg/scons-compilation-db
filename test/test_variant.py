import json


def test_variant(scons_runner, test_dir):
    scons_runner("sconstruct_variant")
    with open(str(test_dir / "compile_commands.json")) as f:
        compilation_db = json.load(f)
    assert compilation_db == [
        {
            "command": "gcc -o build/a.o -c a.c",
            "directory": str(test_dir / "build"),
            "file": str(test_dir / "a.c"),
        },
        {
            "command": "gcc -o build/x.o -c build/x.c",
            "directory": str(test_dir / "build"),
            "file": str(test_dir / "build" / "x.c"),
        },
    ]
