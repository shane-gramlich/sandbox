********************************************************************************
# Build Instructions
********************************************************************************
## Requirements
* Docker (20.10.7+)
* Python (3.9.9+)
* X11 Server
  * VcXsrv X Server (Windows)
  * [WSL.exe](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-containers) (Windows)
  * Native (Unix)

## Installation
* Ensure that the required technologies above are added to the system path
* Start the x11 Server of your choice
* At the command line, execute the following python script from the root of the application directory:
```python dev/install.py```
* This will build a docker image from scratch and then deploy the image to a single node docker swarm. If configured correctly, the application window should appear in aproximately 5-10 minutes.
* After verifying a successful installation, close the application and/or terminate the docker swarm with the following command:
```docker swarm leave --force```

## Build
* Executing the build.py python script from the root directory of the application will trigger a rebuild. The docker service should automatically update and trigger a restart of the application window.  
```python dev/build.py```

## Developement
The docker image built by running ```python dev/install.py``` can be used as a fully functional development environment. Many Integrated Development Environments (IDE) can attach to running containers if internal coding and debugging is preferred. Be aware that closing the application or killing the swarm will likely close the development container. Selecting a [supported IDE](./development_environments.md) is highly recommended.