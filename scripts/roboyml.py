
from contextlib import contextmanager
import yaml
from pathlib import Path

def load(file: Path):
    with file.open('r') as f:
        data = yaml.safe_load(f)
    return data

def save(file: Path, data):
    with file.open('w') as f:
        yaml.dump(data, f)

@contextmanager
def open(file: Path):
    try:
        if not file.exists():
            file.touch()
        data = load(file)
        yield data
    finally:
        save(file, data)
