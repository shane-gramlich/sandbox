cmake_minimum_required(VERSION 3.16)

project($ENV{APP_NAME_INTERNAL} VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)
set(CMAKE_AUTOUIC ON)

set(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$ENV{APP_NAME_INTERNAL}/lib)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$ENV{APP_NAME_INTERNAL}/lib)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/$ENV{APP_NAME_INTERNAL}/bin)

if(DEFINED ENV{QT_DIR})
  set(CMAKE_PREFIX_PATH $ENV{QT_DIR};${CMAKE_PREFIX_PATH})
  message(STATUS "QT_DIR added to CMAKE_PREFIX_PATH: ${CMAKE_PREFIX_PATH}")
endif()

find_package(Qt6 COMPONENTS
  Concurrent
  Core
  Gui
  Network
  PrintSupport
  Svg
  Test
  WebChannel
  # https://stackoverflow.com/questions/67646627/why-is-there-no-qtwebengine-in-the-qt6
  # WebEngine
  WebEngineCore
  WebEngineWidgets
  Widgets
  Xml
  REQUIRED
)

include_directories(
  ${CMAKE_SOURCE_DIR}/src
  ${CMAKE_SOURCE_DIR}/lib
)

add_subdirectory(dev)
add_subdirectory(lib)
add_subdirectory(rsrc)
add_subdirectory(src)
add_subdirectory(test)

add_executable($ENV{APP_NAME_INTERNAL}
  src/Main.cpp
)

target_link_libraries($ENV{APP_NAME_INTERNAL}
  app
)

set_target_properties($ENV{APP_NAME_INTERNAL} PROPERTIES
  OUTPUT_NAME $ENV{APP_NAME_EXECUTABLE}
)