# -*- coding: utf-8 -*-
# <Copyright and license information goes here.>
from PyQt4.QtCore import Qt
from PyKDE4.plasma import Plasma
from PyKDE4 import plasmascript
 
class ipwidgetPython(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        self.setHasConfigurationInterface(True)
        self.resize(350, 150)
        #self.setAspectRatioMode(Plasma.Square)
 
    def paintInterface(self, painter, option, rect):
        painter.save()
        painter.setPen(Qt.green)
        painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Your current ip:\nx.x.x.x")
        painter.restore()
 
def CreateApplet(parent):
    return ipwidgetPython(parent)