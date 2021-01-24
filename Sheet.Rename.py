'''
Sheet.Rename
Goal: Select sheets with a name or a part of a name and replace it with new text.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import FilteredElementCollector, BuiltInCategory
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
#inputs
txtOriginal = str(IN[0])
txtNuevo = str(IN[1])
#mainbody
planos = FilteredElementCollector(doc).OfCategory(BuiltInCategory.OST_Sheets) # Colecto todos los planos
planosActualizados = [] # Lista vacia
TransactionManager.Instance.EnsureInTransaction(doc)
for p in planos:
    if p.Name.Contains(txtOriginal): # Si contiene el texto de entrada, pasa el filtro
        nombreNuevo = p.Name.Replace(txtOriginal,txtNuevo) # Reemplazo el trozo de texto, generando un nuevo texto
        p.Name = nombreNuevo # Asignar el nuevo texto al nombre del plano
        planosActualizados.append(p) # Almaceno los planos renombrados
    else: # Si no contiene el texto de entrada, no hagas nada
        pass
TransactionManager.Instance.TransactionTaskDone()
#output
OUT = "Se han renombrado " + str(len(planosActualizados)) + " planos.", planosActualizados