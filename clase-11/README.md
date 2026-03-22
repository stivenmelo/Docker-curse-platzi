# API Python - Flask con Docker

API REST sencilla construida con Flask y contenida en Docker, que expone información de perfil personal.

## Requisitos

- [Docker](https://www.docker.com/) instalado en tu máquina

## Endpoints

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/getMyInfo` | Retorna información de perfil en formato JSON |

## Construcción de la imagen

Desde la carpeta `clase-11`, ejecuta:

```bash
docker build -t api_python:1.0.0 .
```

## Correr el contenedor

```bash
docker run -it -d -p 8095:5000 --name python_api api_python:1.0.0
```

| Flag | Descripción |
|------|-------------|
| `-d` | Corre el contenedor en segundo plano |
| `-p 8095:5000` | Mapea el puerto 8095 del host al puerto 5000 del contenedor (Flask) |
| `--name python_api` | Asigna un nombre al contenedor |

## Uso

Una vez corriendo, accede a la API desde tu navegador o herramienta como Postman:

```
http://localhost:8095/getMyInfo
```

### Respuesta esperada

```json
{
  "name": "Amin",
  "lastname": "Espinoza",
  "socialMedia": [
    {"facebookUser": "stiven Melo"},
    {"instagramUser": "stiven Melo"},
    {"xUser": "stiven Melo"},
    {"linkedin": "stiven Melo"},
    {"githubUser": "stiven Melo"}
  ],
  "blog": "https://stiven-Melo.com",
  "author": "stiven Melo"
}
```

## Gestión del contenedor

```bash
# Detener el contenedor
docker stop python_api

# Volver a iniciar el contenedor
docker start python_api

# Ver logs del contenedor
docker logs python_api

# Eliminar el contenedor
docker rm python_api
```
