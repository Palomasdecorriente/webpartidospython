import webbrowser

def redirigir_a_youtube():
    url = "https://www.youtube.com/@palomas.de.corriente"
    webbrowser.open(url)

def main():
    respuesta = input("¿Quieres que te redirija a YouTube? (si/no): ")
    if respuesta.lower() == "si":
        redirigir_a_youtube()
    else:
        print("No se redirigirá a YouTube.")

if __name__ == "__main__":
    main()