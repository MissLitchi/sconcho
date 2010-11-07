# -*- coding: utf-8 -*-
######################################################################## #
# (c) 2010 Markus Dittrich
#
# This program is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public
# License Version 3 as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License Version 3 for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free
# Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.
#
#######################################################################


from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import

import operator
from PyQt4.QtCore import (Qt, QRect, QSize, QPointF, QSizeF) 
from PyQt4.QtGui import (QGraphicsView, QRubberBand)




#########################################################
## 
## class for managing the actual pattern canvas
##
#########################################################
class PatternView(QGraphicsView):


    def __init__(self, parent = None):

        super(PatternView, self).__init__()

        # initialize the rubberBand
        self.rubberBand = QRubberBand(QRubberBand.Rectangle, self)
        self.rubberBand.hide()
        self.rubberBandOrigin = None


    def mousePressEvent(self, event):
        """ Handles mouse press events.

        We override this function to check if the user requested
        a rubberBand selection.
        NOTE: We only propagate the event if no rubberBand was selected
        to avoid selection of the pattern grid item where the click
        occured.
        """

        if event.modifiers() & Qt.ShiftModifier:
            self.rubberBandOrigin = event.pos()
            self.rubberBand.setGeometry(QRect(self.rubberBandOrigin, QSize()))
            self.rubberBand.show()
        else:
            QGraphicsView.mousePressEvent(self, event)



    def mouseMoveEvent(self, event):
        """ Handle mouse move events.

        If a rubberBand is active we adjust the size otherwise
        we just hand off the signal.
        """

        if self.rubberBandOrigin:
            self.rubberBand.setGeometry(QRect(self.rubberBandOrigin,
                                              event.pos()).normalized())

        QGraphicsView.mouseMoveEvent(self, event)
        


    def mouseReleaseEvent(self, event):
        """ Handle mouse release events.

        If a rubberBand is active we tell our GraphicsScene what are
        was selected and then disable the rubberBand.
        """
        
        if self.rubberBandOrigin:
            self.scene().select_region((self.mapToScene(
                self.rubberBand.geometry())))
            self.rubberBandOrigin = None
            self.rubberBand.hide()
        
        QGraphicsView.mouseReleaseEvent(self, event)
        


    def adjust_scene(self):
        """ Make sure we have some space around the grid. """

        sceneRect = self.scene().sceneRect()
        sceneRect.adjust(-100, -100, 100, 100)
        self.setSceneRect(sceneRect)
