#!/usr/bin/python

import sys
import dbus


class ClementineInfo():

    pattern2tag = {
        "%a": "artist",
        "%t": "title",
        "%b": "album",
        "%g": "genre",
        "%p": "position",
        "%P": "percent",
        "%l": "time",
        "%i": "arturl",
        "%f": "location",
    }

    def __init__(self):
        pass

    def process(self, pattern):

        self.pattern = pattern

        self.getMetadata()

        res = self.pattern

        for k in self.pattern2tag:
            # check tag existence
            tag = self.pattern2tag[k]
            if tag in self.metadata:
                res = res.replace(k, unicode(self.metadata[tag]))

        return res

    def getMetadata(self):
        try:
            # Clementine lives on the Session bus
            session_bus = dbus.SessionBus()

            # Get Clementine's player object, and then get an interface
            # from that object, otherwise we'd have to type out the full
            # interface name on every method call.
            player = session_bus.get_object('org.mpris.clementine', '/Player')

            iface = dbus.Interface(
                player,
                dbus_interface='org.freedesktop.MediaPlayer'
            )

            # Call a method on the interface
            self.metadata = iface.GetMetadata()
        except Exception as e:
            self.metadata = []
            # print "clementine-info error: %s" % e
            return

        # Get the position
        try:
            self.metadata["position"] = iface.PositionGet() / 1000
        except:
            self.metadata["position"] = 0

        # Get the percent
        try:
            div = float(self.metadata["position"]) /\
                float(self.metadata["time"])

            div = div * 100
            self.metadata["percent"] = "{0:.2f}".format(div)
        except:
            self.metadata["percent"] = 0

        return self.metadata

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 0:
        args = args[1:]

    argsu = []
    for arg in args:
        argsu.append(arg.decode("utf-8"))

    pattern = u" ".join(argsu)

    # default pattern
    if len(pattern) == 0:
        pattern = "%t - %a"

    app = ClementineInfo()
    sys.stdout.write(app.process(pattern).encode("utf-8"))
