'''
CAD.GetDwgFilterByName
Goal: Filter by name and select the ImportInstance (CAD).
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
#input
nombre = str(IN[0]) # Introducir el nombre del archivo dwg
#mainbody
impInstances = FilteredElementCollector(doc).OfClass(ImportInstance).ToElements() # Para obtener las instancias de los elementos importados
seleccionado = [x for x in impInstances if x.Category.Name == nombre + ".dwg"] # Para seleccionar el cad solicitado
#output
OUT = seleccionado
