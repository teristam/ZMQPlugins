import sys
import ZMQPlugins.simple_plotter_zmq

if __name__ == '__main__':
    pl = ZMQPlugins.simple_plotter_zmq.SimplePlotter(20000.)
    pl.startup()
