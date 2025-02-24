# This script adds a new, blank changelog entry, and enables devmode
# It needs to be run in the same directory as the changelog that should be updated
# Folder structure needs to be the same as FP for the devmode-enabling to work

import re
from pathlib import Path

cwd = Path.cwd()

def update_changelog():
    # Update changelog file for further development
    changelog_path = cwd / "changelog.txt"
    new_changelog_entry = ("-----------------------------------------------------------------------------------------------"
                           "----\nVersion: 0.17.00\nDate: 00. 00. 0000\n  Features:\n    - \n  Changes:\n    - \n  "
                           "Bugfixes:\n    - \n\n")
    with (changelog_path.open("r")) as changelog:
        old_changelog = changelog.readlines()
    old_changelog.insert(0, new_changelog_entry)
    with (changelog_path.open("w")) as changelog:
        changelog.writelines(old_changelog)
    print("- changelog entry added")

    # Disable devmode
    tmp_path = cwd / "data" / "tmp"
    init_file_path = cwd / "data" / "init.lua"
    with tmp_path.open("w") as new_file, init_file_path.open("r") as old_file:
        for line in old_file:
            line = re.sub(r"^--devmode = true", "devmode = true", line)
            new_file.write(line)
    init_file_path.unlink()
    tmp_path.rename(init_file_path)
    print("- devmode enabled")


if __name__ == "__main__":
    proceed = input("Sure to update the changelog? (y/n): ")
    if proceed == "y":
        update_changelog()
