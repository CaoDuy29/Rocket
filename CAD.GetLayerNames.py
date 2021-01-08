'''
CAD.GetLayerNames 21/12/2020
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
#definiciones
def tolist(x):
    if isinstance(x,list) == True: return x
    else: return [x]
#inputs
cad = UnwrapElement(tolist(IN[0]))
#mainbody
capas = [x.Category.SubCategories for x in cad]
nombres = [x.Name for x in capas[0]]
#output
OUT = sorted(nombres)