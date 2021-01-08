'''
CAD.GetAll 21/12/2020
diegojsanchez@gmail.com #masalladedynamo
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector,CADLinkType, ImportInstance
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
#inputs
doc = DocumentManager.Instance.CurrentDBDocument
#mainbody
cads= FilteredElementCollector(doc).OfClass(CADLinkType).ToElements() # Para recolectar los archivos de Autocad importados
iins = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements() # Para obtener las instancias de los elementos importados
nombre = [x.Category.Name for x in cads]
#output
OUT = cads, iins, nombre