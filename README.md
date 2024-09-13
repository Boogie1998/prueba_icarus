Hola, en este repositorio está todo el código relacionado con mi prueba técnica

En la app libros solamente incluí los modelos que me indicaron en el archivo "models.py".

En la app tareas utilicé django rest framework para generar una api rest básica sobre el modelo "Tareas", el código principal está en "tareas/views.py"

El código de la practica 2 está en "operaciones.py" y se puede ejecutar con:

python operaciones.py

Las consultas de MySQL están en el archivo "crear_usuarios.sql"

Para ejecutar el servidor de Django, se requiere instalar las dependencias listadas en el archivo "requirements.txt"

pip install -r requirements.txt

Posteriormente inicializar la base de datos con:

python manage.py migrate

Finalmente ejecutar el servidor con:

python manage.py runserver


La rutas para acceder a la api son:

    GET /tareas/tareas - Devuelve la lista de tareas
    GET /tareas/tareas/<id> - Devuelve la tarea con el id especificado
    POST /tareas/tareas/ - Para crear una nueva tarea
    PUT /tareas/tareas/<id> - Para actualizar los datos de una tarea
    DELETE /tareas/tareas/<id> - Para eliminar una tarea


El método POST y PUT admiten un cuerpo json como el siguiente:

{
    "titulo": string
    "descripcion": string
    "completada": boolean (Opcional)
}

Ejemplo:

{
    "titulo": "Pasear al perro",
    "descripcion": "Llevar al perro al parque",
    "completada": false
}

Adicionalmente dejo aquí mis respuestas al cuestionario:

_1. Django_

¿Qué es Django y por qué se usa?

 Es un framework escrito en Python con algunas características como “DRY” para no repetir código y optimizar el uso de recursos, también “ORM” para el desarrollo de bases de datos. 


Explica brevemente el patrón MVC (Modelo-Vista-Controlador) y cómo se implementa en Django.

Como su nombre lo indica se divide en tres partes, el “Modelo” es la arquitectura, la lógica y gestión de datos, en síntesis podría llamarse “Backend”, la “Vista” por el contrario puede ser el “Frontend”, encargándose de lo que ve el usuario como una interfaz, y el controlador es un puente entre ambos interactuando con las acciones del usuario y las respuestas del modelo

¿Qué es un modelo en Django y cómo se define?

Un modelo es una “class” que permite la estructuración de bases de datos.


_2. Python_

¿Qué es un diccionario en Python y cómo se diferencia de una lista?

El diccionario almacena información de forma similar a la de una lista, sin embargo en la lista es por un índice numérico iniciando en 0, mientras que el diccionario almacena una relación clave-valor

Explica la diferencia entre append() y extend() en una lista de Python.

Son similares, pero append agrega un elemento al final de la lista, mientras que extend puede agregar secuencias

¿Qué es un decorador en Python? Proporciona un ejemplo simple.

Es una función normalmente genérica que puede implementarse en otras funciones como para complementar un “def” 

_3. MySQL_

¿Qué es una base de datos relacional?

Datos que se guardan en tablas que se relacionan entre sí

Explica la diferencia entre una clave primaria y una clave foránea.

la clave primaria son atributos únicos, mientras la clave foránea puede repetirse para relacionar unas tablas con otras

¿Cómo se realiza una consulta SELECT básica en MySQL?

se hace la consulta con la palabra SELECT, y se ponen las columnas a capturar
ejemplo:

SELECT id, name from empleados where id = 2;

_4. API_

¿Qué es una API y para qué se utiliza?

Por sus siglas en inglés “interfaz de programación de aplicaciones”, se usa para comunicar distintas aplicaciones entre sí

Explica brevemente la diferencia entre una API REST y una API SOAP.

API REST Utiliza HTTP y los métodos HTTP estándar
API SOAP protocolo XML con muchos estándares de seguridad.

¿Qué son los métodos HTTP más comunes utilizados en una API REST?

GET, POST, PUT, PATCH, DELETE
