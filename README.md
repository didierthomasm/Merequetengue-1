# Merequetenge

## Instalación

Asumiendo el uso de PowerShell:
* Clonar el repositorio, asumiendo que Git está instalado localmente:
```PowerShell
git clone ...
```

* Crear ambiente virtual.
```PowerShell
cd Merequetengue/
python venv venv/
```

* Activar ambiente virtual.
```PowerShell
.\venv\Scripts\activate
```

* Instalar requerimientos.
```PowerShell
python -m pip install -U pip
python -m pip install -r requirements.txt
```

## Planteamientos

A continuación presento una lista de planteamientos o suposiciones basadas en el requerimiento del proyecto final.
* Dado que es un sitio como un Blog y tendrá diferentes usuarios
  * Habrá un listado de todos los blogs, donde el nombre del blog será igual al username.
    * De aquí en adelante __username__ se referirá a usuario.
    * __username__ y __blog__ serán intercambiables.
  * Los listados de posts serán sólo en términos del blog al que pertenecen.
    * Esto significa que no habrá un super listado de posts.
    * Habrá un super listado de blogs, desde donde se podrá acceder al blog.
    * Cada blog tendrá una lista parcial o completa de los posts publicados en él.
  * La ruta a un post será _username/post_, donde _post_ será un __slug__ del post.
  * El __título__ de cada post se convertirá en un __slug__ para ser usado en URLs.
  * El __slug__ de cada post tendrá su campo por separado al título.
* En vista de que habrá más de un blog, y cada blog tendrá muchos posts...
  * En vez de mostrar el ID en la base de datos del post, en su lugar se mostrará el __slug__.
  * Si se usa un ID en el URL, y la combinación con __username__ válida, se redireccionará a _username/slug_.
* Por organización del proyecto, __accounts__ es una aplicación, pero es una extensión de la autenticación standard de Django.
* __Fandango__ y __accounts__ tienen sus correspondientes directorios en Templates.
* Aunque __Merequetengue__ no es una aplicación, el directorio en Templates es para los templates base.
* Las imágenes llegaran al directorio media/, que está declarado como MEDIA_ROOT en Merequetengue.settings.

## Proyecto Django y Aplicaciones

Dado que el proyecto usa Django, lo siguiente es aplicable:
* El proyecto (o sitio) es __Merequetengue__.
* La aplicación principal es __Fandango__.
* La aplicación para creación de usuarios, login y logout es __accounts__.

## Definiciones

* Un _Pegoste_ es _post_ o _page_ en un blog.
* _Pegostes_ es el plural de _Pegoste_.
* _Pegosteador_ será el _usuario_ o autor the un _Pegoste_.

## Mapeo de Proyecto con Requerimientos de Entrega Final

* En lo sucesivo, se asume que los 'puntos' son los que están listados en el documento "Entrega del Proyecto" en el orden que aparecen.
* Casos de prueba:
  * El modelo Fandango.models.Pegoste tiene 3 ejemplos, que se traducirán en Python [doctestst](https://docs.python.org/3/library/doctest.html).
  * La implementación de los tests se hace con Python [unittest](https://docs.python.org/3/library/unittest.html).
  * La ejecución de la suite de tests es con utilidades de Django test. 
* Navegación de blogs y posts:
  * El punto 6, __route pages/__ se traduce a __username/pegostes__
  * El punto 7, __route pages/\<pageId\>__ se traduce a __username/pegoste/\[slug\]__
  * El punto 10. los campos mencionados son esperados en el __modulo__, pero no todos son obligatorios al agregar contenido.

## Referencias

Django:
* Autenticación basada en la seguridad de Django: [https://docs.djangoproject.com/en/4.1/topics/auth/default/](https://docs.djangoproject.com/en/4.1/topics/auth/default/)
* Uso de vistas genéricas: [https://docs.djangoproject.com/en/4.1/ref/class-based-views/](https://docs.djangoproject.com/en/4.1/ref/class-based-views/)
* URLs standard para redireccionamiento de login y logout: [https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-LOGIN_URL](https://docs.djangoproject.com/en/4.1/ref/settings/#std-setting-LOGIN_URL)
* Uso de LoginRequiredMixin mixin para autenticación: [https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-loginrequiredmixin-mixin](https://docs.djangoproject.com/en/4.1/topics/auth/default/#the-loginrequiredmixin-mixin)

Python:
* Uso de doctest para pruebas unitarias: [https://docs.python.org/3/library/doctest.html](https://docs.python.org/3/library/doctest.html)
* Ejecución de suites de pruebas con unittest: [https://docs.python.org/3/library/unittest.html](https://docs.python.org/3/library/unittest.html)
* Implementación de doctest como suite de pruebas en unittest: [https://docs.python.org/3/library/doctest.html#unittest-api](https://docs.python.org/3/library/doctest.html#unittest-api)