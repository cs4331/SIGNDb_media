import os

current_dir = os.path.dirname(os.path.realpath(__file__)) + "/videos"

for filename in os.listdir(current_dir):
    print(filename + "--> _" + filename.lower())
    os.rename(current_dir + "/" + filename, current_dir + "/_" + filename.lower())
