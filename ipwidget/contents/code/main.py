# -*- coding: utf-8 -*-
# <Copyright and license information goes here.>
import os, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from PyKDE4.plasma import *
from PyKDE4 import plasmascript
from PyKDE4.kdecore import *
from PyKDE4.kdeui import *
 
class ipwidgetPython(plasmascript.Applet):
    def __init__(self,parent,args=None):
        plasmascript.Applet.__init__(self,parent)
 
    def init(self):
        plasmascript.Applet.init(self)
        self.setHasConfigurationInterface(True)
        self.resize(350, 150)
        self.config().writeEntry("url", QString("test"))
        self.url = self.config().readEntry("url", "")
        self.debug=self.url.toString()
        print self.debug
        #self.setAspectRatioMode(Plasma.Square)
 
    def paintInterface(self, painter, option, rect):
        painter.save()
        painter.setPen(Qt.green)
        # painter.drawText(rect, Qt.AlignVCenter | Qt.AlignHCenter, "Your current ip:\nx.x.x.x\n"+self.debug)
        painter.restore()
        
        
    def createConfigurationInterface(self, parent):
        self.config_widget = QWidget(parent)
        self.config_ui = uic.loadUi(self.package().filePath('ui', 'ip.ui'), self.config_widget)
        self.debug=self.config_ui.url
        self.config_ui.url.setText(self.url.toString())
        parent.addPage(self.config_widget, i18n('ipwidgetPython'), 'text-x-python')
 
def CreateApplet(parent):
    return ipwidgetPython(parent)