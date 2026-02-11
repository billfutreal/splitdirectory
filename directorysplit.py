import os
import shutil
from dotenv import load_dotenv

# Load .env file
load_dotenv()

SOURCE_DIR = os.getenv("SOURCE_DIR")
FILES_PER_FOLDER = int(os.getenv("FILES_PER_FOLDER", 500))


def split_files(source_dir, files_per_folder):
    # ---- Error Checking ----
    if not source_dir:
        raise ValueError("SOURCE_DIR not set in .env file.")

    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory not found: {source_dir}")

    if not os.path.isdir(source_dir):
        raise NotADirectoryError(f"Path is not a directory: {source_dir}")
    # ------------------------

    files = [
        f for f in os.listdir(source_dir)
        if os.path.isfile(os.path.join(source_dir, f))
    ]

    files.sort()

    total_files = len(files)
    print(f"Total files found: {total_files}")

    if total_files == 0:
        print("No files to process.")
        return

    folder_count = 0

    for i in range(0, total_files, files_per_folder):
        folder_count += 1
        new_folder_name = f"batch_{folder_count}"
        new_folder_path = os.path.join(source_dir, new_folder_name)

        os.makedirs(new_folder_path, exist_ok=True)

        batch_files = files[i:i + files_per_folder]

        for file_name in batch_files:
            src_path = os.path.join(source_dir, file_name)
            dst_path = os.path.join(new_folder_path, file_name)
            shutil.move(src_path, dst_path)

        print(f"Created {new_folder_name} with {len(batch_files)} files")

    print("Done.")


if __name__ == "__main__":
    split_files(SOURCE_DIR, FILES_PER_FOLDER)
