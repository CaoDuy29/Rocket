'''
UI.StringByLanguageType
Goal: Sometimes in a company we have revit users who have revit configured 
    in English and others in Spanish or another language. Using this switch 
    the result of the output text will be according to your language.
diegojsanchez@gmail.com #masalladedynamo
v: 1.0.1
'''
# bibliotecas
import clr 
clr.AddReference('RevitAPI')
import Autodesk
clr.AddReference('RevitServices')
from RevitServices.Persistence import DocumentManager
doc = DocumentManager.Instance.CurrentDBDocument
uiapp = DocumentManager.Instance.CurrentUIApplication
app = uiapp.Application
revitLanguage = app.Language
#inputs
langType1 = IN[0] #Texto en ingles
langType2 = IN[1] #Texto en español u otro lenguaje
#mainbody
if revitLanguage == Autodesk.Revit.ApplicationServices.LanguageType.English_USA:
    salida = langType1
else:
    salida = langType2
#output
OUT = salida