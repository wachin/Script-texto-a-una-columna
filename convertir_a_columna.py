# Leer el archivo de texto
   with open('texto_entrada.txt', 'r') as file:
       contenido = file.read()

   # Separar las palabras
   palabras = contenido.split()

   # Escribir las palabras en un nuevo archivo, una por línea
   with open('texto_en_columna.txt', 'w') as file:
       for palabra in palabras:
           file.write(palabra + '\n')