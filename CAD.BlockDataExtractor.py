'''
CAD.BlockDataExtractor
Goal: Extract information from CAD blocks
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''

#biblioteca
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import Options, Element, XYZ #Options es clave para acceder a las opciones de geometría del cad
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion) #Clave para convertir a curvas de dynamo
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument #Necesitamos acceder al documento
#definiciones
def desplazamientoOrigen(geometrias):
	poCAD = cad.GetTransform().Origin.ToPoint() #Punto origen: Podemos llamarlo el internalPoint de cad o scp universal
	poRVT = XYZ(0,0,0).ToPoint() #Punto origen: InternalPoint de revit
	distancia = poRVT.DistanceTo(poCAD)
	vector = XYZ(poCAD.X - poRVT.X, poCAD.Y - poRVT.Y, poCAD.Z - poRVT.Z).ToVector() #Punto origen: InternalPoint de revit
	#vector = XYZ(poRVT.X - poCAD.X, poRVT.Y - poCAD.Y, poRVT.Z - poCAD.Z).ToVector() #Punto origen: InternalPoint de revit
	if distancia != 0:
		return [g.Translate(vector,distancia) for g in geometrias]
	else:
		return geometrias
#inputs
cad = UnwrapElement(IN[0]) #Necesita un ImportInstance
geometrias, nombreBloques, nombreCapas = [], [], []
#mainbody
	#acceder a los bloques
opciones = cad.get_Geometry(Options()) #Accedemos a las opciones de geometría
listaSimbolos = [g.GetSymbolGeometry() for g in opciones] #Obtenemos todas las geometrías almacenadas en una lista que almacena todo
bloques = [g for g in listaSimbolos[0] if str(g.GetType()) == "Autodesk.Revit.DB.GeometryInstance"] #GeometryInstance = Bloque de cad
	#datos de los bloques
origen = [b.Transform.Origin.ToPoint() for b in bloques] #Obtenemos el origen del bloque respecto al ptoOrigenCAD tendre que desplazarlos al ptoOrigenRVT
elementos = [b.Symbol for b in bloques] #Obtenemos los elementType y accedemos a la información del nombre
for e in elementos:
	nombreCompleto = Element.Name.__get__(e) #El nombre completo tiene una estructura: nombre del archivo.dwg.nombre del bloque
	lista = nombreCompleto.split(".") # Trocear string usando el punto.
	nombreBloques.append(lista[-1]) # El nombre del bloque esta al final de la lista
listaGeometrias = [b.GetInstanceGeometry() for b in bloques] #Obtenemos todas las geometrías almacenadas por listas
for lista in listaGeometrias: #Estas geometrias estan ubicadas respecto al ptoOrigenCAD tendre que desplazarlos al ptoOrigenRVT
	aux1, aux2 = [], []
	for g in lista:
		aux1.append(g.ToProtoType()) #Almaceno las curvas	
		id = (g.GraphicsStyleId) #Busco el id del estilo grafico o capa de las curvas
		capa = doc.GetElement(id) #Conocido el id busco la capa
		nCapas = capa.GraphicsStyleCategory.Name #Busco el nombre de la capa de cada geometria
		aux2.append(nCapas)
	geometrias.append(aux1)
	nombreCapas.append(aux2)
#output
OUT = desplazamientoOrigen(origen), nombreBloques, desplazamientoOrigen(geometrias), nombreCapas
