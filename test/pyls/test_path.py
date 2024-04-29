import subprocess


def test_relative_path():
    captured_dot_path = subprocess.run(["pyls","."], capture_output=True, text=True).stdout
    expected_dot_path = "LICENSE README.md ast go.mod lexer main.go parser token\n"

    captured_parser_path = subprocess.run(["pyls","./parser"], capture_output=True, text=True).stdout
    expected_parser_path = "parser_test.go parser.go go.mod\n"

    captured_trailing_slash = subprocess.run(["pyls","./parser/"], capture_output=True, text=True).stdout
    expected_trailing_slash = "parser_test.go parser.go go.mod\n"

    assert captured_dot_path == expected_dot_path
    assert captured_parser_path == expected_parser_path
    assert captured_trailing_slash == expected_trailing_slash

def test_path_as_file_name():
    captured_file_name = subprocess.run(["pyls","./parser/parser.go"], capture_output=True, text=True).stdout
    expected_file_name = "parser.go\n"

    assert captured_file_name == expected_file_name