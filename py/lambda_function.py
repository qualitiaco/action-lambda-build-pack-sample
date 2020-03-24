import subprocess
import os


def lambda_handler(event, context):
    subprocess.call(["pwd"])
    env = {"LD_LIBRARY_PATH": os.path.join(os.getcwd(), "lib")}
    cwd = os.getcwd()
    os.chdir("/tmp")

    subprocess.call(["pwd"])
    subprocess.call([
        os.path.join(cwd, "git"),
        f"--exec-path={cwd}",
        "clone",
        "https://github.com/qualitiaco/action-lambda-build-pack-sample.git"],
        env=env)

    print(open("/tmp/action-lambda-build-pack-sample/src/build.sh", "r").read())
