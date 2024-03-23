import pytest
from pathlib import Path

def _is_repo_root(p: Path) -> bool:
    """Returns true if it sees the files listed below, defining a "repo root" """
    file_to_search_for = ["src", "tests", "setup.cfg", "pyproject.toml", ".git"]
    return all(
            len(list(p.glob(folder))) >= 1
            for folder in file_to_search_for
    )


@pytest.fixture(scope="session")
def test_folder() -> Path:
    """Recurses until it finds a directory with setup.cfg and a folder called src

    Mainly just a protector in case this file gets moved
    """
    original_file_path = Path(__file__).expanduser().resolve()
    path = original_file_path

    while not _is_repo_root(path) and str(path) != "/":
        path = path.parent
    if str(path) == "/":
        raise OSError(f"can't find a valid repo root starting from {str(original_file_path)}")
    else:
        return path / "tests"
