def text_indentation(text):
    """Imprime el texto con dos saltos de línea después de los caracteres ., ?, :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    
    # Reemplazamos las puntuaciones con un salto de línea
    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    
    # Eliminamos los espacios adicionales al principio y final de las líneas
    print("\n".join(line.strip() for line in text.split("\n") if line.strip()))

