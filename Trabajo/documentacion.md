
## Despliegue en IaaS-Google Compute Enfine ##

### Herramientas ###

Para realizar el despliegue de una aplicación en el IaaS, debemos de tener instalado:

- [vagrant](https://www.vagrantup.com/downloads.html) que debemos acceder a la página web y descargar el software. Permite generar entornos de desarrollo reproducibles y compartibles de forma muy sencilla.
- [vagrant-google](https://github.com/mitchellh/vagrant-google), este es el plugin para poder desplegar una máquina virtual en el IaaS de Google. Para instalarlo basta con poner en el terminal:
    vagrant plugin install vagrant-google

- pip de python. Esto es necesario para instalar Ansible y Fabric que veremos más adelante.
    sudo easy_install pip

- Ansible es una herramienta open-source que automatiza tareas dentro de nuestra máquina virtual (en este caso nuestro IaaS). Instalación:

    sudo pip install ansible --quiet

- [Fabric](http://www.fabfile.org/installing.html) permite empaquetar, implementar y administrar microservicios escalables y confiables. Instalación:

    sudo pip install fabric

- Clave ssh para poder conectarnos de forma remota al IaaS de google.
