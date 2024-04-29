import subprocess


def test_flag_A():
    captured_output = subprocess.run(["pyls", "-A"], capture_output=True, text=True).stdout
    expected_output = ".gitignore LICENSE README.md ast go.mod lexer main.go parser token\n"

    assert captured_output == expected_output

def test_flag_l():
    captured_output = subprocess.run(["pyls", "-l"], capture_output=True, text=True).stdout
    expected_output = (
        "drwxr-xr-x 1071 Nov 14 11:27 LICENSE\n"
        "drwxr-xr-x 83 Nov 14 11:27 README.md\n"
        "-rw-r--r-- 4096 Nov 14 15:58 ast\n"
        "drwxr-xr-x 60 Nov 14 13:51 go.mod\n"
        "drwxr-xr-x 4096 Nov 14 15:21 lexer\n"
        "-rw-r--r-- 74 Nov 14 13:57 main.go\n"
        "drwxr-xr-x 4096 Nov 17 12:51 parser\n"
        "-rw-r--r-- 4096 Nov 14 14:57 token\n"
    )

    assert captured_output == expected_output

def test_flag_r():
    captured_output = subprocess.run(["pyls", "-r"], capture_output=True, text=True).stdout
    expected_output = "token parser main.go lexer go.mod ast README.md LICENSE\n"

    assert captured_output == expected_output

def test_flag_lt():
    captured_output = subprocess.run(["pyls", "-lt"], capture_output=True, text=True).stdout
    expected_output = (
        "drwxr-xr-x 1071 Nov 14 11:27 LICENSE\n"
        "drwxr-xr-x 83 Nov 14 11:27 README.md\n"
        "drwxr-xr-x 60 Nov 14 13:51 go.mod\n"
        "-rw-r--r-- 74 Nov 14 13:57 main.go\n"
        "-rw-r--r-- 4096 Nov 14 14:57 token\n"
        "drwxr-xr-x 4096 Nov 14 15:21 lexer\n"
        "-rw-r--r-- 4096 Nov 14 15:58 ast\n"
        "drwxr-xr-x 4096 Nov 17 12:51 parser\n"
    )

    assert captured_output == expected_output