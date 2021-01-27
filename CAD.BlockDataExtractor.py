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
from Autodesk.Revit.DB import * #Options #Clave para acceder a las opciones de geometría del cad
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.GeometryConversion) #Clave para convertir a curvas de dynamo
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import Line #Necesario para el desplazamiento de geometrias
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument #Necesitamos acceder al documento
#definiciones
def desplazamientoOrigen(geometrias):
	ptoOrigenCAD = cad.GetTransform().Origin.ToPoint() #Podemos llamarlo el internalPoint de cad o scp universal
	ptoOrigenRVT = XYZ(0,0,0).ToPoint() #InternalPoint de revit
	linea = Autodesk.DesignScript.Geometry.Line.ByStartPointEndPoint(ptoOrigenRVT, ptoOrigenCAD)
	return [g.Translate(linea.Direction,linea.Length) for g in geometrias]
#inputs
cad = UnwrapElement(IN[0]) #Necesita un ImportInstance
geometrias, nombres, idCapas = [], [], []
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
	nombres.append(lista[-1]) # El nombre del bloque esta al final de la lista
listaGeometrias = [b.GetInstanceGeometry() for b in bloques] #Obtenemos todas las geometrías almacenadas por listas
for lista in listaGeometrias: #Estas geometrias estan ubicadas respecto al ptoOrigenCAD tendre que desplazarlos al ptoOrigenRVT
	for g in lista:
		idCapas.append(g.GraphicsStyleId) #Busco el id del estilo grafico o capa de las curvas
		geometrias.append(g.ToProtoType()) #Almaceno las curvas
capas = [doc.GetElement(id) for id in idCapas] #Conocido el id busco la capa
nombreCapas = [s.GraphicsStyleCategory.Name for s in capas] #Busco el nombre de la capa de cada geometria
#output
OUT = desplazamientoOrigen(origen), nombres, desplazamientoOrigen(geometrias), nombreCapas
