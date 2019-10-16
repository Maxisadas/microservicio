# Microservicio de Estadisticas

Es un microservicio que realiza estadisticas de ventas, productos mas vendidos, etc...

[Documentación de API](./README-API.md)

La documentación de las api también se pueden consultar desde el home del microservicio
que una vez levantado el servidor se puede navegar en [localhost:5000](http://localhost:5000/)

##Casos de uso.

###Caso de uso 1: Consultar total de ventas.

El CU 1 se encarga de enviar al usuario, un resumen de todo el dinero generado por las ventas en total, describiendo las ventas por unidad y el total. 
###Caso de uso 2:Consultar productos más vendidos.

El caso de uso se encarga de enviar al usuario, un ranking de los productos más vendidos ordenados de mayor cantidad de productos vendidos,  al menor.


## Apidoc

Apidoc es una herramienta que genera documentación de apis para proyectos node (ver [Apidoc](http://apidocjs.com/)).
Este proyecto utiliza apidoc para documentar los servicios rest.

El microservicio muestra la documentación como archivos estáticos si se abre en un browser la raíz del servidor [localhost:3002](http://localhost:3002/)

Ademas se genera la documentación en formato markdown.

Para que funcione correctamente hay que instalarla globalmente con npm

```bash
npm install -g apidoc
npm install -g apidoc-markdown2
```

Luego podemos generar la documentación usando

```bash
apidoc -o public
apidoc-markdown2 -p public -o README-API.md
```

Esto nos genera una carpeta con la documentación, esta carpeta debe estar presente desde donde se ejecute el servidor, el mismo busca ./public para localizarlo, aunque se puede configurar desde el archivo de properties.

## Archivo config.ini

Este archivo permite configurar los parámetros del servidor, ver ejemplos en config.ini.
El servidor busca el archivo "./config.ini".