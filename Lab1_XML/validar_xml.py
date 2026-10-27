
import xml.etree.ElementTree as ET

try:
    arbol = ET.parse("Asignatura_WEB\Lab1_XML\catalogo.xml")
    raiz = arbol.getroot()

    print("XML valido: la sintaxis es correcta.")
    print("Elemento raiz:", raiz.tag)

    libros = raiz.findall("libro")
    print("Cantidad de libros:", len(libros))

    for libro in libros:
        print(
            libro.get("id"),
            "-",
            libro.findtext("titulo")
        )

except ET.ParseError as error:
    print("Error de sintaxis XML:", error)

except FileNotFoundError:
    print("No se encontro el archivo catalogo.xml.")
