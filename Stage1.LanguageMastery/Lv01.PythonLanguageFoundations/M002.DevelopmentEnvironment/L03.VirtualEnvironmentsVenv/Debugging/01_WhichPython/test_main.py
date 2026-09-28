# Run with:  python -m pytest
import os


def make_folders(tmp_path, *names_with_python):
    folders = {}
    for name in ["storefront", "python313", "windows"]:
        folder = tmp_path / name
        folder.mkdir()
        if name in names_with_python:
            (folder / "python.exe").write_text("fake")
        folders[name] = str(folder)
    return folders


def test_first_match_wins(main, tmp_path):
    f = make_folders(tmp_path, "storefront", "python313")
    path_value = os.pathsep.join([f["storefront"], f["python313"], f["windows"]])
    assert main.which("python.exe", path_value) == os.path.join(f["storefront"], "python.exe")


def test_skips_folders_without_it(main, tmp_path):
    f = make_folders(tmp_path, "python313")
    path_value = os.pathsep.join([f["storefront"], f["python313"], f["windows"]])
    assert main.which("python.exe", path_value) == os.path.join(f["python313"], "python.exe")


def test_not_found(main, tmp_path):
    f = make_folders(tmp_path)
    assert main.which("python.exe", os.pathsep.join(f.values())) is None
