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

#ifndef KNITTING_SYMBOL_H
#define KNITTING_SYMBOL_H

/* boost includes */
#include <boost/shared_ptr.hpp>

/* QT includes */
#include <QString>
#include <QSize>



/***************************************************************
 * 
 * KnittingSymbol manages a single knitting symbol
 *
 ***************************************************************/
class KnittingSymbol 
{
  
public:

  explicit KnittingSymbol(const QString& aPath,
      const QString& aName, const QSize& aDimension,
      const QString& aDescription, const QString& aInstruction);
  bool Init();


  /* some basic accessors */
  const QString& path() { return svgPath_; }
  const QString& name() { return name_; }
  const QSize& dim() { return dimensions_; }
  const QString& desc() { return description_; }
  const QString& instructions() { return instructions_; }



private:

  /* some tracking variables */
  int status_;
  
  QString svgPath_;
  QString name_;
  QSize dimensions_;
  QString description_;
  QString instructions_;
}; 


/* convenience typedef */
typedef boost::shared_ptr<KnittingSymbol> KnittingSymbolPtr;



#endif