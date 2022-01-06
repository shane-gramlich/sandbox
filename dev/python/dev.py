import json
import os
import pathlib

class App:
  def __init__(self):
    self.home_path = pathlib.Path(__file__).parents[2].__str__()

    with open(self.home_path + "/conf/settings.json") as settings_file:
      settings = json.load(settings_file)

    self.settings = settings
    self.initEnvironment()

  def initEnvironment(self):
    app = self

    os.environ["APP_DEBUG"] = app.settings["build"]["debug"].__str__()
    os.environ["APP_HOME"] = app.settings["application"]["path"].__str__()
    os.environ["APP_NAME_EXECUTABLE"] = app.settings["application"]["name"]["executable"].__str__()
    os.environ["APP_NAME_DISPLAY"] = app.settings["application"]["name"]["display"].__str__()
    os.environ["APP_NAME_INTERNAL"] = app.settings["application"]["name"]["internal"].__str__()
    os.environ["APP_VERSION"] = app.settings["application"]["version"].__str__()
    os.environ["BUILD_CACHE"] = app.settings["build"]["cache"].__str__()
    os.environ["BUILD_NAME"] = app.settings["application"]["name"]["internal"] + ":" + app.settings["application"]["version"].__str__()
    os.environ["QT_DEBUG_PLUGINS"] = "1" if app.settings["build"]["debug"] else "0"
    os.environ["QT_PATH"] = app.settings["qt"]["path"].__str__()
    os.environ["QT_VERSION"] = app.settings["qt"]["version"].__str__()

  def printSettings(self):
    settings_formatted = json.dumps(self.settings, indent=2)
    print(settings_formatted)

  def saveSettings(self):
    with open(self.home_path + "/conf/settings.json", "w") as settings_file:
      json.dump(self.settings, settings_file, indent=2)
    print("settings.json saved")