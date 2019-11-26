# ZMQInterface

A plugin for open-ephys enabling the interfacing of [ZeroMQ](http://zeromq.org) clients to open ephys. 

Forked from [anjaldoshi's github repository](https://github.com/anjaldoshi/ZMQPlugins).

The interface exposes all data and events and allows to provide events to the application, enabling the creation of advanced visualization and monitoring add-ons.

The code in the examples under the `python_clients` directory may serve as tutorial for now. Note that the application may be written in any language/platform supporting ZeroMQ.

This repository also contains the source code from the old EventBroadcaster and NetworkEvents, which may be removed in the future.

## Installation Instruction

The original plugin is compatible with the Linux, MacOSX versions of Open Ephys. The plugin was ported to Visual Studio/Windows and updated in 2018-2019 to a current Open Ephys version with modified plugin architecture. Some features were disabled during the process.

### Compile from source code

The Plugin is organized so that it can be compiled as much as possible outside of the main open-ephys source tree. Under Linux, a symlink to the Source/Plugins directory is however necessary. 


To compile, extract in a folder just outside the Open Ephys plugin-GUI source tree
e.g. 

```
$ ls src
plugin-GUI/
ZMQInterface/
etc...
```

Call `cmake` in the `Build` folder with the appropriate generator for your platform:

```
cmake -G "<GENERATOR>"
```

<GENERATOR> can be one of the following options:

- "Visual Studio 12 2013 Win64"

- "Visual Studio 14 2015 Win64"

- "Visual Studio 15 2017 Win64"

- "Xcode"

- "Unix Makefiles" 

  - For linux you may need to set the GCC version before calling cmake, as gcc-9 is not support in the current version of JUCE used by open-ephys

    ```
    export CC=gcc-8
    export CXX=g++-8
    ```

After generating the build files, the actual building process depends on your platform

#### Linux

- In the `Build` folder, call `make` and then `make install`

#### Windows

- Open `OE_ZMQ.sln` and compile the solution

#### MacOS

- Open the Xcode project and compile

### Binary installation 
Binary files are provided in the `bin` folder of this repository. The Linux file is compiled in Ubuntu 19 with gcc-8. Windows binary is compiled with Visual Studio 2015.

- Copy the binary file of respective platform (.so for Linux, .dll for Windows) to the `plugins` directory of open-ephys

 



