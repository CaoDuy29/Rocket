'''
CAD.GetAllImportInstances
Goal: Get all the import instances (CAD) and their names.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
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
impInstances = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements() # Para obtener las instancias de los elementos importados
nombres = [x.Category.Name for x in impInstances] # Para acceder al nombre del cad
#output
OUT = impInstances, nombres
