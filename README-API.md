<a name="top"></a>
# Servicio de estadisticas v0.1.0

Microservicio de estadisticas

- [RabbitMQ_GET](#rabbitmq_get)
	- [Logout](#logout)
	
- [Sells](#sells)
	- [Generar estadistica de ventas](#generar-estadistica-de-ventas)
	


# <a name='rabbitmq_get'></a> RabbitMQ_GET

## <a name='logout'></a> Logout
[Back to top](#top)

<p>Escucha de mensajes logout desde auth. Invalida sesiones en cache.</p>

	FANOUT auth/logout



### Examples

Mensaje

```
{
  "type": "resumen_exist",
  "message" : "tokenId"
}
```




# <a name='sells'></a> Sells

## <a name='generar-estadistica-de-ventas'></a> Generar estadistica de ventas
[Back to top](#top)



	GET /v1/stats/sells



### Examples

Header Autorización

```
Authorization=bearer {token}
```


### Success Response

Respuesta

```
        HTTP/1.1 200 OK
        {
"sells":[{
"order_id": "id de la orden"
"total": "El dinero total obtenido por la orden"

}]
"total_sales":"Dinero total obtenido de todas las ordenes"
        }
```


### Error Response

401 Unauthorized

```
HTTP/1.1 401 Unauthorized
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "path" : "{Nombre de la propiedad}",
    "message" : "{Motivo del error}"
}
```
400 Bad Request

```
HTTP/1.1 400 Bad Request
{
    "error" : "{Motivo del error}"
}
```
500 Server Error

```
HTTP/1.1 500 Server Error
{
    "error" : "{Motivo del error}"
}
```
