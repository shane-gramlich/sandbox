#include "App.h"

#include "ui/HelloWorld.h"

App::App(int &argc, char **argv) : QApplication(argc, argv) {
  mWidget = new HelloWorld();
  mWidget->show();
}