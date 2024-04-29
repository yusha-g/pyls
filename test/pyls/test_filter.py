import difflib
import subprocess


def test_filter_dir():
    captured_result = subprocess.run(
        ["pyls", "--filter=dir"], capture_output=True, text=True
    ).stdout
    expected_result = "ast lexer parser token\n"
    assert captured_result == expected_result


def test_filter_dir_lost_reverse_time():
    captured_result = subprocess.run(
        ["pyls", "-lrt", "--filter=dir"], capture_output=True, text=True
    ).stdout
    expected_result = (
        "drwxr-xr-x 4096 Nov 17 12:51 parser\n"
        "-rw-r--r-- 4096 Nov 14 15:58 ast\n"
        "drwxr-xr-x 4096 Nov 14 15:21 lexer\n"
        "-rw-r--r-- 4096 Nov 14 14:57 token\n"
    )
    assert captured_result == expected_result


def test_filter_file():
    captured_result = subprocess.run(
        ["pyls", "--filter=file"], capture_output=True, text=True
    ).stdout
    expected_result = "LICENSE README.md go.mod main.go\n"
    assert captured_result == expected_result


def test_filter_file_lost_reverse_time():
    captured_result = subprocess.run(
        ["pyls", "-lrt", "--filter=file"], capture_output=True, text=True
    ).stdout
    expected_result = (
        "-rw-r--r-- 74 Nov 14 13:57 main.go\n"
        "drwxr-xr-x 60 Nov 14 13:51 go.mod\n"
        "drwxr-xr-x 83 Nov 14 11:27 README.md\n"
        "drwxr-xr-x 1071 Nov 14 11:27 LICENSE\n"
    )
    assert captured_result == expected_result
