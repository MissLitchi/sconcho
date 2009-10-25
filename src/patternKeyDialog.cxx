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

/** Qt headers */
#include <QGraphicsView>
#include <QGroupBox>
#include <QHBoxLayout>
#include <QLabel>
#include <QPushButton>
#include <QSettings>
#include <QSplitter>
#include <QVBoxLayout>


/** local headers */
#include "basicDefs.h"
#include "patternKeyCanvas.h"
#include "patternKeyDialog.h"


QT_BEGIN_NAMESPACE

/**************************************************************
 *
 * PUBLIC FUNCTIONS 
 *
 **************************************************************/

//-------------------------------------------------------------
// constructor
//-------------------------------------------------------------
PatternKeyDialog::PatternKeyDialog(const QSettings& aSetting,
  QWidget* myParent)
    :
      QDialog(myParent),
      settings_(aSetting),
      mainSplitter_(new QSplitter)
{
  status_ = SUCCESSFULLY_CONSTRUCTED;
}


//--------------------------------------------------------------
// main initialization routine
//--------------------------------------------------------------
bool PatternKeyDialog::Init()
{
  if ( status_ != SUCCESSFULLY_CONSTRUCTED )
  {
    return false;
  }

  /* call individual initialization routines */
  setModal(false);
  setWindowTitle(tr("Edit pattern key"));

  /* create interface */
  create_canvas_();
  create_buttons_();

  /* generate main layout */
  mainSplitter_->addWidget(patternKeyView_);
  QVBoxLayout* mainLayout = new QVBoxLayout;
  mainLayout->addWidget(mainSplitter_);
  mainLayout->addLayout(buttonLayout_);
  setLayout(mainLayout);


  /* some plumbing */
  connect(this,
          SIGNAL(settings_changed()),
          patternKeyCanvas_,
          SLOT(update_after_settings_change())
         );


  return true;
}


/**************************************************************
 *
 * PUBLIC SLOTS
 *
 *************************************************************/

/**************************************************************
 *
 * PUBLIC MEMBER FUNCTIONS
 *
 *************************************************************/

/**************************************************************
 *
 * PROTECTED MEMBER FUNCTIONS 
 *
 *************************************************************/

/**************************************************************
 *
 * PRIVATE SLOTS
 *
 *************************************************************/

/*************************************************************
 *
 * PRIVATE MEMBER FUNCTIONS
 *
 *************************************************************/

//------------------------------------------------------------
// create the pattern key canvas and the associated 
// QGraphicsView
//------------------------------------------------------------
void PatternKeyDialog::create_canvas_()
{
  patternKeyCanvas_ = new PatternKeyCanvas(settings_, this);  
  patternKeyCanvas_->Init();
  patternKeyView_ = new QGraphicsView(patternKeyCanvas_);
}


//-------------------------------------------------------------
// create and wire up the dialog buttons
//-------------------------------------------------------------
void PatternKeyDialog::create_buttons_()
{
  buttonLayout_ = new QHBoxLayout;

  QPushButton* closeButton = new QPushButton(tr("close"));
  QPushButton* exportToCanvasButton = 
    new QPushButton(tr("export to canvas"));

  buttonLayout_->addWidget(exportToCanvasButton);
  buttonLayout_->addStretch(1);
  buttonLayout_->addWidget(closeButton);

  connect(closeButton,
          SIGNAL(clicked()),
          this,
          SLOT(hide())
         );
}



QT_END_NAMESPACE