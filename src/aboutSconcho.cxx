/***************************************************************
 *
 * (c) 2009 Markus Dittrich 
 *
 * This program is free software; you can redistribute it 
 * and/or modify it under the terms of the GNU General Public 
 * License Version 3 as published by the Free Software Foundation. 
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License Version 3 for more details.
 *
 * You should have received a copy of the GNU General Public 
 * License along with this program; if not, write to the Free 
 * Software Foundation, Inc., 59 Temple Place - Suite 330, 
 * Boston, MA 02111-1307, USA.
 *
 ****************************************************************/

/* QT headers */
#include <QString>

/* local includes */
#include "aboutSconcho.h"

QT_BEGIN_NAMESPACE

/*****************************************************************
 *
 * public member functions
 *
 *****************************************************************/

//----------------------------------------------------------------
// constructor
//----------------------------------------------------------------
AboutSconchoWidget::AboutSconchoWidget(QWidget* aParent) 
  : 
    QMessageBox(aParent)
{
  setup_contents_();
}


/*****************************************************************
 *
 * private member functions
 *
 *****************************************************************/

//----------------------------------------------------------------
// set up the main content of the GUI
//----------------------------------------------------------------
void AboutSconchoWidget::setup_contents_()
{
  QString content = 
    "<b>sconcho</b> is a versatile and extensible knitting chart "
    "design tool capable of producing print quality charts.<br><br>"
    "Copyright (C) 2009 Markus Dittrich<br><br>"
    "Big thanks go to Susan Dittrich for continued testing, advice, "
    "support, and generation of the SVG knitting symbols.<br><br>"
    "This program is free software: you can redistribute it and/or "
    "modify it under the terms of the GNU General Public License " 
    "as published by the Free Software Foundation, either version 3 "
    "of the License, or (at your option) any later version.<br><br>"
    "This program is distributed in the hope that it will be useful, "
    "but WITHOUT ANY WARRANTY; without even the implied warranty of "
    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the "
    "GNU General Public License for more details.<br>"
    "You should have received a copy of the GNU General Public "
    "License along with this program. "  
    "If not, see <a href=\"http://www.gnu.org/licenses/\">"
    "http://www.gnu.org/licenses</a><br><br>"
    "Please contact the author via <a href=\"mailto:haskelladdict@users.sourceforge.org\">"
    "email</a> for suggestions, comments, or in case of problems";
    
  setText(content);
}

QT_END_NAMESPACE
