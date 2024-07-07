from sflock.abstracts import File
from sflock.ident import identify
import argparse
import os


def call_sflock_identify(file: str):
    f = File.from_path(file.encode())
    try:
        package = identify(f, check_shellcode=True)
    except Exception as e:
        print(f"Error occured while identifying file. filepath:{file}, error message:{e}")
        package = "unknown"
    return package


def get_dir_files(dir_path) -> list:
    result = [os.path.join(dp, f) for dp, dn, filenames in os.walk(dir_path) for f in filenames]
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple sflock launcher.")
    parser.add_argument("--input", "-i", help="input file path", type=str, required=True)

    args = parser.parse_args()

    print(f"[-] Result")
    if os.path.isdir(args.input):
        filelist = get_dir_files(args.input)
        for file in filelist:
            package = call_sflock_identify(file)
            print(f"{file}:{package}")
    else:
        package = call_sflock_identify(args.input)
        print(f"{args.input}:{package}")