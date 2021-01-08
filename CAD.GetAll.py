'''
CAD.GetAll 21/12/2020
Goal: Get all the import instances (CAD) and their names.
diegojsanchez@gmail.com #masalladedynamo
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector, ImportInstance
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
#mainbody
ins = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements() # Para obtener las instancias de los elementos importados
nombres = [x.Category.Name for x in ins] # Para acceder al nombre del cad
#output
OUT = ins, nombres
