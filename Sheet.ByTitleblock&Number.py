'''
Sheet.ByTitleblock&Number
Goal: Create sheets by template and number.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import ViewSheet
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
from RevitServices.Transactions import TransactionManager
doc = DocumentManager.Instance.CurrentDBDocument
#inputs
cajetin = UnwrapElement(IN[0]) #Elemento de Revit que viene desde Dynamo: UnwrapElement
n = int(IN[1]) #Cantidad de planos
#mainbody
planos = []
TransactionManager.Instance.EnsureInTransaction(doc)
for i in range(n): # range(n), crea una lista con la cantidad de elementos "n"
    p = ViewSheet.Create(doc,cajetin.Id)
    planos.append(p)
TransactionManager.Instance.TransactionTaskDone()
#output
OUT = "Se han creado " + str(len(planos)) + " planos.", planos