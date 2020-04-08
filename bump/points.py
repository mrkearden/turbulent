# --
f = open("/home/titan/fea/bump/bump.csv","r")
# Point Coordinates

import math
import salome
salome.salome_init()
import GEOM
from salome.geom import geomBuilder
geompy = geomBuilder.New(salome.myStudy)

n=0
for l in f:
    x, y, z = [ float(v) for v in l.split() ]
    pt = geompy.MakeVertex(x, y, z)
    geompy.addToStudy(pt, "Pt_%s"%(n))
    n += 1
pass
import salome
salome.sg.updateObjBrowser()


