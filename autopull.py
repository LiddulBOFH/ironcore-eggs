import os
import argparse

parser	= argparse.ArgumentParser("Iterates through all of the directories in the passed directory, and pulls the latest changes")
parser.add_argument("directory")

args	= parser.parse_args()
rootDir	= args.directory

print("+   Git Autopull")
print("|   Addon directory: " + rootDir)
os.chdir(rootDir)

for currentDir in filter(os.path.isdir, os.listdir(rootDir)):
	print("|   Checking: " + currentDir)
	if os.path.isdir(currentDir + "/.git"):
		os.chdir(currentDir)
		os.system("git status")
		os.system("git pull")
		os.chdir(rootDir)

print("+   Finished updating addons!")