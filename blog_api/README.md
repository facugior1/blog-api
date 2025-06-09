# API REST - Mensajes Blog

Esta API permite realizar operaciones CRUD sobre mensajes de un blog.

## Rutas disponibles

- `GET /mensajes` - Lista todos los mensajes
- `GET /mensajes/<id>` - Muestra un mensaje por ID
- `POST /mensajes` - Crea un nuevo mensaje
- `PUT /mensajes/<id>` - Actualiza un mensaje existente
- `DELETE /mensajes/<id>` - Elimina un mensaje por ID

## Estructura del mensaje
```json
{
  "user": "Juan",
  "mensaje": "¡Hola, mundo!"
}
```

## Instalación
```bash
pip install -r requirements.txt
python app.py
```