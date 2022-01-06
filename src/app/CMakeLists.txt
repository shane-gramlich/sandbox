add_library(app
  App.cpp
)

target_link_libraries(app
  ui
  Qt6::Widgets
)