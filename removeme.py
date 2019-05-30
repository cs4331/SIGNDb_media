import os

current_dir = os.path.dirname(os.path.realpath(__file__)) + "/videos"

for filename in os.listdir(current_dir):
    print(filename + "--> " + filename.lower()[2:])
    os.rename(current_dir + "/" + filename, current_dir + "/" + filename.lower()[2:])
