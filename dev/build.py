import os

from python.dev import App

app = App()
app_internal_name = app.settings["application"]["name"]["internal"]

# Docker Commands
os.system("docker exec $(docker ps -q -f name=" + app_internal_name +
          "_stack_app) ninja -j 0 -C build/debug/cmake")

os.system("docker service update " + app_internal_name + "_stack_app")

os.system("docker container prune --force --filter 'until=5m")