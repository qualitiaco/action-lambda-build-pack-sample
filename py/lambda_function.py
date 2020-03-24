import subprocess
import os


def lambda_handler(event, context):
    print("abcdefg")
    subprocess.call(["pwd"])
    env = {"LD_LIBRARY_PATH": os.path.join(os.getcwd(), "lib")}
    os.chdir("/tmp")

    subprocess.call(["pwd"])
    subprocess.call(["./git", "clone", "https://github.com/qualitiaco/action-lambda-build-pack-sample.git"], env=env)
