# 1. MI PRIMER PROMPT
primer_prompt = """
ROL: Eres Ivan, unico responsable de marketing de Tostadores del Valle.
TAREA: Dame 3 ideas de publicaciones para esta semana que pueda hacer solo en 20 min.
CONTEXTO: Vendemos cafe especialidad en bolsas de 250g y 1kg, tienda en linea y 2 cafeterias en Puebla. 60% ventas en linea. Publico 25-40 anos, oficina, compra para casa. Tono cercano y sencillo, sin tecnicismos de cata y sin exceso de exclamaciones. Canales: Instagram feed/stories y boletin miercoles. Esta semana: Martes 1er aniversario segunda cafeteria, Jueves llega Lote Sierra Norte edicion limitada 200 bolsas de 250g a $210, finde sin eventos. Lo que funciona: mostrar proceso de tueste y hacer preguntas a la comunidad.
FORMATO: Tabla con Dia, Canal, Idea, Foto/video con celular, Texto ejemplo max 30 palabras.
"""

# 2. RESPUESTA QUE OBTUVE (Resumen)
respuesta_1 = """
Martes: Aniversario segunda cafeteria. Foto equipo.
Jueves: Lote Sierra Norte 200 bolsas $210.
Miercoles Boletin: Como preparar cafe en casa + pregunta a comunidad.
"""

# 3. SEGUNDA VUELTA: QUE CAMBIAR Y POR QUE
segunda_vuelta = """
Manten las 3 ideas, no empieces de cero. NO toques tono cercano ni datos de ficha.
Cambia: 1. Quita promesa "pide hoy recibe manana" y descuento 20% porque no esta en ficha. 2. En Lote Sierra Norte deja claro 200 bolsas, 250g, $210. 3. Agrega pregunta a comunidad en cada idea porque es lo que mejor funciona.
"""

# 4. REVISION
revision = """
Revise: Promesa "mejor cafe del pais" la quite por tono. Verifique cifra 200 bolsas a $210 contra ficha y corregi. Verifique que boletin solo sale miercoles, no martes/jueves.
"""

# 5. PLANTILLA CON HUECOS ENTRE CORCHETES
plantilla = """
ROL: Eres Ivan de Tostadores del Valle.
TAREA: Dame [NUMERO_DE_IDEAS] ideas para esta semana.
CONTEXTO: Cafe 250g y 1kg, 2 cafeterias Puebla, publico 25-40 oficina, tono cercano sencillo, sin tecnicismos.
Esta semana: [EVENTO_1_DIA] - [EVENTO_1_DESC], [EVENTO_2_DIA] - [EVENTO_2_DESC], finde [FINDE].
Canales: Instagram y boletin [DIA_BOLETIN].
FORMATO: Tabla Dia, Canal, Idea, Foto, Texto 30 palabras.
"""

print("Proyecto listo")
