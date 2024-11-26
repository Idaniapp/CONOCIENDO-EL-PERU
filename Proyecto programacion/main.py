from flask import Flask, render_template, request

app = Flask(__name__)

# Lista de destinos turísticos
destinos_turisticos = [
    "Machu Picchu",
    "Lago Titicaca",
    "Líneas de Nazca",
    "Valle Sagrado de los Incas",
    "Cañón del Colca",
    "Selva Amazónica de Iquitos",
    "Fortaleza Real Felipe",
    "Malecón de Miraflores",
    "Máncora",
    "Nevado de Huascarán"
]

@app.route('/', methods=['GET'])
def home():
    # Renderiza la plantilla HTML principal
    return render_template('pagina2.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    # Obtiene el valor del formulario (nombre del destino que falta por recorrer)
    destino_faltante = request.form.get('destino_faltante')

    if not destino_faltante:
        return "Por favor, ingresa un destino antes de enviar.", 400

    # Verificamos si el destino esta en la lista
    destino_encontrado = None
    for destino in destinos_turisticos:
        destino_faltante = str(destino_faltante)  # Asegúrate de que sea una cadena
        if destino_faltante.lower() in destino.lower():
            destino_encontrado = destino
            break

    if destino_encontrado:
        mensaje = f"¡Gracias por compartir! Te falta visitar: {destino_encontrado}."
    else:
        mensaje = f"El destino '{destino_faltante}' no está en nuestra lista de destinos turísticos. Lo agregaremos pronto. Gracias!"

    return render_template('respuesta.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)

