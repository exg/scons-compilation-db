from pathlib import Path
from shutil import copyfile, copytree

import pytest
import subprocess

TOOL_NAME = "scons_compilation_db.py"


@pytest.fixture
def test_dir(tmp_path):
    src = Path(__file__).parents[0]
    dst = tmp_path / "test"
    copytree(str(src), str(dst))
    copyfile(str(src.parents[0] / TOOL_NAME), str(dst / TOOL_NAME))
    return dst


@pytest.fixture
def scons_runner(test_dir):
    def runner(sconstruct):
        cmd = ["scons", "-C", str(test_dir), "-f", str(test_dir / sconstruct)]
        return subprocess.check_call(cmd)

    return runner
