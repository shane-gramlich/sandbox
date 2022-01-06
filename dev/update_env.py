import os

from python.dev import App

app = App()

# .env
file = open(os.path.join(app.home_path, ".devcontainer", ".env"), "w+")
for k, v in sorted(os.environ.items()):
    file.write(k + "=" + v + "\n")

# docker-compose.extended.yml
with open(os.path.join(app.home_path, "dev", "docker", "docker-compose.yml"), 'r') as file :
  filedata = file.read()
filedata = filedata.replace('${BUILD_NAME}', os.getenv("BUILD_NAME").__str__())
filedata = filedata.replace('//var/run/docker.sock:/var/run/docker.sock', "/var/run/docker.sock:/var/run/docker.sock")
with open(os.path.join(app.home_path, ".devcontainer", "docker-compose.yml"), 'w+') as file:
  file.write(filedata)

# .devcontainer.json
with open(os.path.join(app.home_path, "dev", "ide", ".devcontainer", "devcontainer.json"), 'r') as file :
  filedata = file.read()
filedata = filedata.replace('${APP_NAME_DISPLAY}', os.getenv("APP_NAME_DISPLAY").__str__())
with open(os.path.join(app.home_path, ".devcontainer", "devcontainer.json"), 'w+') as file:
  file.write(filedata)