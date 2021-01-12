'''
CAD.CurvesFromLayerName 28/12/2020
Goal: Get dynamo curves from an import instance and a layer name.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
# bibliotecas
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import Options #Clave para acceder a las opciones de geometría del cad
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion) #Clave para convertir a curvas de dynamo
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument #Necesitamos acceder al documento
#inputs
cad = UnwrapElement(IN[0]) #Necesita un ImportInstance
capa = str(IN[1]) #Necesita un string, nos aseguramos con un Casting
geometrias, curvasDynamo = [], []
#mainbody
opciones = cad.get_Geometry(Options()) #Accedemos a las opciones de geometría
listaGeometrias = [g.GetInstanceGeometry() for g in opciones] #Obtenemos todas las geometrías almacenadas en una lista que almacena todo
for g in listaGeometrias[0]: #Separamos los solidos del resto de geometrías (los solidos son sombreados en autocad y los descartamos)
	if str(g.GetType()) != "Autodesk.Revit.DB.Solid":
		geometrias.append(g)
	else:
		pass
idCapas = [c.GraphicsStyleId for c in geometrias] #Busco el id del estilo grafico o capa de las curvas
capas = [doc.GetElement(id) for id in idCapas] #Conocido el id busco la capa
nombres = [s.GraphicsStyleCategory.Name for s in capas] #Busco el nombre de la capa de cada geometria
for n,c in zip(nombres,geometrias):
	if capa == n:
		curvasDynamo.append(c.ToProtoType()) #Convierto las curvas de revit a curvas de dynamo
	else:
		pass
#output
OUT = curvasDynamo
