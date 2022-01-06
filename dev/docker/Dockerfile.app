# Variable dance to pass arguments to Dockerfile
# https://github.com/moby/moby/issues/34129
ARG APP_HOME
ARG APP_NAME_DISPLAY
ARG APP_NAME_EXECUTABLE
ARG APP_NAME_INTERNAL
ARG APP_VERSION
ARG BUILD_NAME
ARG QT_DEBUG_PLUGINS
ARG QT_PATH
ARG QT_VERSION

FROM ubuntu:22.04

# Redeclared arguments after being wiped by the FROM statement
ARG APP_HOME
ARG APP_NAME_DISPLAY
ARG APP_NAME_EXECUTABLE
ARG APP_NAME_INTERNAL
ARG APP_VERSION
ARG BUILD_NAME
ARG QT_DEBUG_PLUGINS
ARG QT_PATH
ARG QT_VERSION

# Dockerfile Arguments
ARG APP_BINARY=${APP_HOME}/build/debug/cmake/${APP_NAME_INTERNAL}/bin/${APP_NAME_EXECUTABLE}
ARG QT_MODULES=all
ARG QT_HOST=linux
ARG QT_TARGET=desktop
ARG QT_ARCH=gcc_64
ARG QT_DIR=${QT_PATH}/${QT_VERSION}/${QT_ARCH}

# Path Variable
ENV PATH ${APP_BINARY}:\
    ${QT_DIR}/bin:\
    $PATH

# Persistent Environment Variables
ENV APP_BINARY=${APP_BINARY}
ENV APP_HOME=${APP_HOME}
ENV APP_NAME_DISPLAY=${APP_NAME_DISPLAY}
ENV APP_NAME_EXECUTABLE=${APP_NAME_EXECUTABLE}
ENV APP_NAME_INTERNAL=${APP_NAME_INTERNAL}
ENV APP_VERSION=${APP_VERSION}
ENV BUILD_NAME=${BUILD_NAME}
ENV QML_IMPORT_PATH ${QT_DIR}/qml/
ENV QML2_IMPORT_PATH ${QT_DIR}/qml/
ENV QT_DEBUG_PLUGINS ${QT_DEBUG_PLUGINS}
ENV QT_DIR=${QT_DIR}
ENV QT_PLUGIN_PATH ${QT_DIR}/plugins/
ENV QT_VERSION=${QT_VERSION}

# Print all variables
RUN printenv

# Packages
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get install -y \
    git \
    cmake \
    ninja-build \
    python-is-python3 \
    python3 \
    python3-pip \
    build-essential \
    gdb \
    docker.io \
    clang-format \
    clang-tidy \
    libdbus-1-3 \
    libpulse-mainloop-glib0 \
    libglu1-mesa-dev \
    libgl1-mesa-dev \
    mesa-common-dev \
    libxkbcommon-dev \
    libxkbfile-dev \
    libvulkan-dev \
    libvulkan1 \
    libssl-dev \
    libxcb-icccm4-dev \
    libxkbcommon-x11-dev \
    libxcb-image0-dev \
    libxcb-keysyms1-dev \
    libxcb-render0-dev \
    libxcb-shape0-dev \
    libxcb-xkb-dev \
    libxcb-render-util0-dev

RUN pip3 install yapf aqtinstall

# Another Qt Installer (AQT) https://github.com/miurahr/aqtinstall
# aqt list-qt linux desktop --modules 6.2.2 gcc_64 
RUN aqt install-qt --outputdir ${QT_PATH} ${QT_HOST} ${QT_TARGET} \
    ${QT_VERSION} ${QT_ARCH} -m ${QT_MODULES}

# These commands copy your files into the specified directory in the image
# and set that as the working location
COPY . ${APP_HOME}
WORKDIR ${APP_HOME}

# Extract shared IDE settings
COPY dev/ide/ ${APP_HOME}

# This command compiles your app using GCC, adjust for your source code
RUN cmake -GNinja -DCMAKE_BUILD_TYPE=Debug \
    -DCMAKE_PREFIX_PATH=${QT_DIR} -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -S . -B build/debug/cmake
RUN ninja -j 0 -C build/debug/cmake

# This command runs your application, comment out this line to compile only
ENV DISPLAY=host.docker.internal:0.0
CMD ${APP_BINARY}

# Defining an entrypoint forces the container to continue running
# ENTRYPOINT ["tail", "-f", "/dev/null"]