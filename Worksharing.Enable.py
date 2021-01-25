'''
Worksharing.Enable
Goal: Enable worksharing.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
#bibliotecas
import clr
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
#input
accion = IN[0]
#mainbody
if accion == True:
	doc.EnableWorksharing("Rejillas","Subproyecto") #(worksetNameGridLevel, worksetName)
else:
	pass
#output
OUT = "Worksharing activo" if doc.IsWorkshared else "Marcar True para iniciar"