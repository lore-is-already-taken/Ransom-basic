from app.encrypter_handler import Encryption
from app.finder import Finder


def main():
    work_dir = "./app/test"
    key_dir = "./app/keys"
    target_files = [".txt", ".docx"]

    finder = Finder(work_dir)
    encrypter = Encryption(key_path=key_dir)
    files_to_encrypt = finder.find_files_with_extension(target_files)


if __name__ == "__main__":
    main()
