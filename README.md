3dRoboSimWithPhysics
====================

3D Robot Simulator implementing ODE physics

## Requirements:

* Open Dynamics Engine (ODE), with python bindings
    - http://ode-wiki.org/wiki/index.php?title=Manual:_Install_and_Use#Install_with_Python_bindings
    - In Ubuntu 14.04 you need to pick the single precision ODE package
      and manually building the PyODE sources is recommended:
        - Install packages `python-pyrex`, `libode1sp` and `libode-sp-dev`
        - Download the PyODE sources from http://pyode.sourceforge.net/
        - Build & install the PyODE sources per their INSTALL file
* Vpython
    - http://www.vpython.org
    - package `python-visual` in Ubuntu 14.04
* Numpy
    - http://www.numpy.org/
    - installed by vpython installer on Windows
    - package `python-numpy` in Ubuntu 14.04
* Python Image Library
    - http://www.pythonware.com/products/pil/
    - package `python-pil` in Ubuntu 14.04

* Vpyode files, modified by TwoShanks.  Included in this repo.

## Instructions:
Run `python simulator.py`.

Robot behaviour can be customised by editing the `usercode0` function
in simulator.py.
