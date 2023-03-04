import shutil
import subprocess
import tempfile
from pathlib import Path

from PIL import Image


def _get_args(file_path, region):
    if region:
        programs = [["maim", "-s"], ["scrot", "-s"]]
    else:
        programs = [["maim"], ["scrot"]]
    for program in programs:
        result = shutil.which(program[0])
        if result:
            return program + [file_path]


def make_screenshot(region=False):
    with tempfile.TemporaryDirectory() as tmp_dir:
        file_path = Path(tmp_dir) / "screenshot.png"
        args = _get_args(file_path, region)
        pipe = subprocess.Popen(args)
        pipe.wait()
        return Image.open(file_path)
