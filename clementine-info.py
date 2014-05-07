#!/usr/bin/python

import sys
import os
import dbus

class ClementineInfo():

    pattern2tag = {
        "%a" : "artist",
        "%t" : "title",
        "%b" : "album",
        "%g" : "genre",
        "%p" : "position",
        "%P" : "percent",
        "%l" : "time",
        "%i" : "arturl",
        "%f" : "location",
    }

    def __init__(self, pattern):
        self.pattern = pattern

    def process(self):

        self._getMetadata()

        res = self.pattern

        for k in self.pattern2tag:
            res = res.replace(k, unicode(self.metadata[self.pattern2tag[k]]))

        return res

    def _getMetadata(self):
        # Clementine lives on the Session bus
        session_bus = dbus.SessionBus()

        # Get Clementine's player object, and then get an interface from that object,
        # otherwise we'd have to type out the full interface name on every method call.
        player = session_bus.get_object('org.mpris.clementine', '/Player')
        iface = dbus.Interface(player, dbus_interface='org.freedesktop.MediaPlayer')

        # Call a method on the interface
        self.metadata = iface.GetMetadata()

        # Get the position
        self.metadata["position"] = iface.PositionGet() / 1000

        # Get the percent
        div = float(self.metadata["position"]) / float(self.metadata["time"])
        div = div * 100
        self.metadata["percent"] = "{0:.2f}".format(div)

if __name__=="__main__":
    args = sys.argv
    if len(args)>0:
        args = args[1:]

    argsu = []
    for arg in args:
        argsu.append(arg.decode("utf-8"))

    pattern = u" ".join(argsu)

    app = ClementineInfo(pattern)
    print app.process()
