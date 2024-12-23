# Script-texto-a-una-columna

Script que convierte texto de una lista lineal de palabras a una columna, texto el cual el cual debe estar en un archivo de texto como entrada y se creará un archivo de salida con palabras separadas en columnas:

---

# **Manual de Usuario**

### **Título**: Conversión de Texto a una Columna

## **Introducción**
Este programa convierte un archivo de texto donde todas las palabras están en una sola línea (separadas por espacios) por ejemplo una lista de parquetes de Debian o Ubuntu para instalar desde la terminal, a un formato de columna, con cada palabra en una línea nueva.

---

## **Requisitos**
1. Computadora con sistema operativo Windows, macOS o Linux.
2. Python instalado en el sistema (versión 3.7 o superior).
3. Editor de texto (como Notepad, Bloc de notas, o Visual Studio Code).

---

## **Instrucciones de Uso**

### **1. Preparar el Archivo de Texto**
1. Abre tu editor de texto favorito.
2. Escribe o copia las palabras en una sola línea, separadas por espacios.  
   **Ejemplo:**
   ```text
   uno dos tres cuatro cinco
   ```
 O las que estén en una lista de pasteles a instalar para la terminal ejemplo sudo apt inslall gedit gedit-plugins meld   
   
3. Guarda el archivo con un nombre, como `texto_entrada.txt`.

---

### **2. Descargar el Script**
1. Copia el siguiente script y guárdalo como un archivo llamado `convertir_a_columna.py`.

   ```python
   # Leer el archivo de texto
   with open('texto_entrada.txt', 'r') as file:
       contenido = file.read()

   # Separar las palabras
   palabras = contenido.split()

   # Escribir las palabras en un nuevo archivo, una por línea
   with open('texto_en_columna.txt', 'w') as file:
       for palabra in palabras:
           file.write(palabra + '\n')
   ```

2. Guarda el archivo en la misma carpeta donde está tu archivo de entrada.

---

### **3. Ejecutar el Script**
1. Abre la terminal o línea de comandos:
   - En Windows: Presiona `Win + R`, escribe `cmd` y presiona Enter.
   - En macOS/Linux: Abre la aplicación **Terminal**.
2. Navega a la carpeta donde guardaste el script y el archivo de texto:
   - Usa el comando `cd` seguido de la ruta de la carpeta.
     **Ejemplo:**  
     ```bash
     cd C:\Usuarios\Alumno\MisArchivos
     ```
     
     En Linux también podría abrir una terminal con clic derecho desde el administrador de archivos.
3. Ejecuta el script con el comando:
   ```bash
   python convertir_a_columna.py
   ```
En Linux sería

   ```bash
   python3 convertir_a_columna.py
   ```
---

### **4. Resultado**
1. Se generará un archivo llamado `texto_en_columna.txt` en la misma carpeta.
2. Abre el archivo `texto_en_columna.txt` y verifica que las palabras estén en una columna.  
   **Ejemplo de salida:**
   ```text
   uno
   dos
   tres
   cuatro
   cinco
   ```

---

## **Posibles Problemas y Soluciones**
1. **Error: `python no se reconoce como un comando`**  
   - Solución: Asegúrate de haber instalado Python y de configurarlo en tu ruta del sistema.
2. **El archivo de salida está vacío**  
   - Solución: Revisa que el archivo de entrada no esté vacío y que las palabras estén separadas por espacios.

---

Dios les bendiga.