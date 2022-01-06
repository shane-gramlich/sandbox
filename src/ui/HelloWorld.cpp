#include "ui/HelloWorld.h"

#include <QHBoxLayout>
#include <QLabel>

HelloWorld::HelloWorld() {
  setAttribute(Qt::WA_DeleteOnClose);
  setMinimumSize(1280, 720);

  auto *hello = new QLabel("Hello", this);
  hello->setAlignment(Qt::AlignCenter);

  auto *world = new QLabel("World", this);
  world->setAlignment(Qt::AlignCenter);

  auto *layout = new QHBoxLayout(this);
  layout->addWidget(hello);
  layout->addWidget(world);
}

HelloWorld::~HelloWorld() = default;