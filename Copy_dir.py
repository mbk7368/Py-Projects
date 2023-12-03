import os
import subprocess
from multiprocessing import Pool

def run(args):
    src, dest = args
    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    src = "/data/prod/"
    dest = "/data/prod_backup/"

    # Create a pool of specific number of CPUs
    pool = Pool()

    tasks = []
    # Iterate over the source directory and its subdirectories using os.walk
    for root, directories, files in os.walk(src):
        # Create the corresponding directory structure in the destination directory
        dest_root = os.path.join(dest, os.path.relpath(root, src))
        os.makedirs(dest_root, exist_ok=True)

        # Backup files in the current directory using multiprocessing
        for file in files:
            source_file = os.path.join(root, file)
            dest_file = os.path.join(dest_root, file)

            tasks.append((source_file, dest_file))

    # Start each task within the pool
    pool.map(run, tasks)

    # Close the multiprocessing pool
    pool.close()
    pool.join()