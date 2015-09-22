# -*- coding: utf-8 -*-
from zope.interface import Interface, Attribute


class IIolApplication(Interface):
    """
    marker interface for iol document
    """
    iol_app = Attribute("Application Name")

    def __init__(self,app):
        self.iol_app = app or ""

    def getIolApp(self):
        return self.iol_app or ""
    
    def setIolApp(self,app):
        self.iol_app = app or ""
        
        
        
class IIolApplicationLayer(Interface):
    """Marker interface for the Browserlayer
    """
