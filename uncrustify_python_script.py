"""Module runs the below script creating beautified code during build."""

import os
import subprocess

# Folder/File locations
SOURCE_DIR = "submodules/psoc6hal"
UNCRUSTIFY_PATH = "/home/runner/work/create_pipeline_repo/create_pipeline_repo/uncrustify/build/uncrustify"
CONFIG_PATH = "mystyle.cfg"

def find_files(base_dir, extensions):
    """Recursively find all files with the given extensions."""
    for root, _, files in os.walk(base_dir):
        for file in files:
            if any(file.endswith(ext) for ext in extensions):
                yield os.path.join(root, file)

def run_uncrustify(files):
    """Run uncrustify on a list of files."""
    for file in files:
        output_file = f"{file}.unc"
        try:
            subprocess.run(
                [UNCRUSTIFY_PATH, "-c", CONFIG_PATH, "-f", file, "-o", output_file],
                check=True
            )
            print(f"Processed: {file} -> {output_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {file}: {e}")

if __name__ == "__main__":
    """Main Function to run uncrustify on each .c and .h file."""
    files_to_process = find_files(SOURCE_DIR, [".c", ".h"])
    run_uncrustify(files_to_process)
