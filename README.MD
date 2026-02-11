# File Batch Splitter (Python)

Split all files in a directory into subdirectories containing a fixed number of files (default: 500). Files are moved, not copied, ensuring no duplication.

## Features

Works with any number of files

Automatically creates required batch folders

Configurable batch size via .env

Built-in error handling

Deterministic ordering (files sorted before processing)

## Requirements

Python 3.8+

python-dotenv

Install dependency:

pip install python-dotenv

### Project Structure
project/
│
├── split_files.py
├── .env
└── README.md

## Configuration

Create a .env file in the same directory as the script.

Example .env
SOURCE_DIR=C:\path\to\your\source_folder
FILES_PER_FOLDER=500

### Variables

SOURCE_DIR (required)
Absolute path to the directory containing files.

FILES_PER_FOLDER (optional)
Number of files per batch folder. Default is 500.

## Usage

Run the script:

python split_files.py

The script will:

Load configuration from .env

Validate the source directory

Read all files (top-level only)

Sort them

Create folders named:

batch_1
batch_2
batch_3
...


Move files into batches of the specified size

Place any remainder in the final folder

### Example

If the directory contains 5,610 files and batch size is 500:

11 folders with 500 files

1 folder with 110 files

Total folders created: 12

The script automatically adjusts to any number of files.

### Error Handling

Execution stops if:

SOURCE_DIR is missing from .env

The directory does not exist

The path is not a directory

If zero files are found, the script exits cleanly.

## Notes

Only processes files in the top level of the source directory.

Nested folders are ignored.

Uses shutil.move() — files are relocated, not duplicated.

Safe to run on any file count.