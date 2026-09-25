from pathlib import Path


def get_file_dir() -> Path:
    # 当前文件所在的目录路径
    return Path(__file__).resolve().parent


def get_file_path(file_name: str) -> Path:
    return Path.joinpath(get_file_dir(), file_name)


# print(get_file_dir())
