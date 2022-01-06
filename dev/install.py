import os
import shutil

from python.dev import App

# Read conf/settings.json
app = App()
app_home_path = app.home_path

build_cache = app.settings["build"]["cache"]
build_debug = app.settings["build"]["debug"]

docker_build_cache = "--no-cache=false" if build_cache else "--no-cache=true"
docker_verbosity = "plain" if build_debug else "tty"

# First Run
devcontainer = app_home_path + "/.devcontainer/devcontainer.json"
first_run = not os.path.exists(devcontainer)
if (first_run):
    source = app_home_path + "/dev/ide"
    print("Copying the following development directories into " +
          app_home_path + ": " + os.listdir(source).__str__())
    shutil.copytree(source, app_home_path, dirs_exist_ok=True)
    os.system('python dev/update_env.py')

# Docker Commands
os.environ["DOCKER_SCAN_SUGGEST"] = "false"
os.system("docker build " + docker_build_cache + " --tag " +
          os.getenv("BUILD_NAME").__str__() + " --file " + app_home_path +
          "/dev/docker/Dockerfile.app --progress=" + docker_verbosity +
          " --build-arg APP_HOME=" + os.getenv("APP_HOME").__str__() +
          " --build-arg APP_NAME_EXECUTABLE=" +
          os.getenv("APP_NAME_EXECUTABLE").__str__() +
          " --build-arg APP_NAME_DISPLAY" +
          os.getenv("APP_NAME_DISPLAY").__str__() +
          " --build-arg APP_NAME_INTERNAL=" +
          os.getenv("APP_NAME_INTERNAL").__str__() +
          " --build-arg APP_VERSION=" + os.getenv("APP_VERSION").__str__() +
          " --build-arg BUILD_NAME=" + os.getenv("BUILD_NAME").__str__() +
          " --build-arg QT_DEBUG_PLUGINS=" +
          os.getenv("QT_DEBUG_PLUGINS").__str__() + " --build-arg QT_PATH=" +
          os.getenv("QT_PATH").__str__() + " --build-arg QT_VERSION=" +
          os.getenv("QT_VERSION").__str__() + " .")

os.system("docker swarm leave --force")
os.system("docker swarm init")

os.system("docker stack deploy --compose-file " + app_home_path +
          "/dev/docker/docker-compose.yml " +
          os.getenv("APP_NAME_INTERNAL").__str__() + "_stack")

os.system("docker image prune --force")