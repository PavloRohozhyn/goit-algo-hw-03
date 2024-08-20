""" Task 1 """

import os
import shutil
import sys

def hendler(src_dir, dest_dir="dist") -> None :
    """ folder hendler """

    # if folder doesnt exists -> create
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    # check data inside folder
    for item in os.listdir(src_dir):
        item_path = os.path.join(src_dir, item)
        # if we have a folder -> run recursion
        if os.path.isdir(item_path):
            hendler(item_path, dest_dir)
        else:
            # get file extension
            extension = os.path.splitext(item)[1][1:]
            # if file doent has extension move his to folder  "without_extension"
            if not extension:
                extension = "without_extension"
            # make folder if doesnt exists (for extension files)
            ext_folder = os.path.join(dest_dir, extension)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            # copy operation
            shutil.copy2(item_path, ext_folder)


def main():
    """ main function """

    # parsing argument
    if len(sys.argv) < 2:
        print("Please, provide path the destination foldes as arguments.")
        return
    src_dir = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else "dist"

    try:
        hendler(src_dir, dest_dir)
        print(f"Files were sorted and copied in folder '{dest_dir}'.")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    main()
