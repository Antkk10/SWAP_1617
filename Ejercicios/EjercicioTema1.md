
# Ejercicios TEMA 1 #

### 1. ¿Cuándo es mejor usar cada uno de estos servicios? ###

 * **Apache**: Es el servidor web HTTP más usado en la actualidad. Características:
   * Es usado para servir contenido tanto estático como dinámico. Aunque como veremos más adelante, Nginx funciona mejor para servir contenido estático.
   * Permite el uso de muchos lenguajes en el lado del servidor, como PHP, Perl, Python, Ruby...
   * La capa frontal (front end) del motor de búsqueda de Google está basada en una versión modificada de Apache.


 * **Nginx**:
   * Nginx es muy recomendable usarlo con contenido estático que se quiera servir a los usuarios.
   * Balanceador de carga, lo que permite mayor escalabilidad.
   * Como proxy inverso, lo que nos permite:
      * Añadir seguridad y evitar posibles ataques de usuarios.
      * Además nos permite securizar el acceso a las aplicaciones web con HTTPS, es decir, enruta la petición HTTP a HTTPS mejorando la seguridad entre dos puntos.
   * Nginx como server de streaming. Netflix utiliza actualmente Nginx debido a que necesita una conexión rápida y estable con sus usuarios para enviar el contenido.


  * **Node.js**: es un entorno Javascript del lado del servidor, basado en eventos. Sus características son:
    * Compila y ejecuta javascript a alta velocidad. Utiliza un motor desarrollado por Google llamado V8. El aumento de velocidad se debe a que V8 compila Javascript en código de máquina nativo, en lugar de interpretarlo o ejecutarlo como bytecode.
    * Posee un modelo de eventos, lo que permite la programación asíncrona.
    * Todas las operaciones intensivas de E/S se llevan a cabo de forma asíncrona, como se ha comentado anteriormente.
    * Utiliza menos recursos que otros servicios, esto permite reducir costes de infraestructura. Un ejemplo sería Linkedin (por el año 2012) que pasó de tener 30 servidores a 3.

  * **Cherokee**: Es un servidor web multiplataforma, desarrollado completamente en C y software libre. Se caracteriza por:
    * Soporta más usuarios concurrentes, más peticiones por segundo y consume menos memoria que otros servidores web.
    * Actualizaciones sin parada de servicio, esto es muy importante cuando tenemos el servidor en producción y necesitamos que los servicios sigan respondiendo a las necesidades de los usuarios.

  * **IIS (Internet Information Services)**: Es un servidor web desarrollado por Microsoft. Los servicios que ofrece son FTP, SMTP, NNTP y HTTP/HTTPS. Sus características son:
    * La seguridad web es mejor que otros servidores web, debido al aislamiento automático de las aplicaciones.
    * Este aislamiento se logra al proporcionar a los procesos de trabajo una identidad única y una configuración en espacio aislado de manera reducida.
    * Almacenado en caché dinámica integrada, lo que permite una mayor velocidad de respuesta.






#### Bibliografía ####

* Test con contenido estático Nginx vs Apache [test contenido estático](https://help.dreamhost.com/hc/en-us/articles/215945987-Web-server-performance-comparison).
* Netflix usa Nginx para el streaming [enlace](https://www.nginx.com/blog/why-netflix-chose-nginx-as-the-heart-of-its-cdn/)
* Linkedin pasa de tener 30 servidores a 3, cambiando Ruby on rails por Node.js [noticia](https://www.infoq.com/news/2012/10/Ruby-on-Rails-Node-js-LinkedIn)
* Información de Cherokee en [wikipedia](https://es.wikipedia.org/wiki/Cherokee_(servidor_web))
* IIS [enlace](https://msdn.microsoft.com/es-es/library/hh831725(v=ws.11).aspx)
