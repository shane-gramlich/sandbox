//
// Author: Shane Gramlich
//

#ifndef APP_H
#define APP_H

#include <QApplication>

class HelloWorld;

class App : public QApplication {
 public:
  App(int &argc, char **argv);

 private:
  HelloWorld *mWidget = 0;
};

#endif