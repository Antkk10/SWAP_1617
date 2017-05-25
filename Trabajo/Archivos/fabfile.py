# coding: utf-8

from fabric.api import sudo, cd, env, run, shell_env
import os

def Clonar():
    """ Descarga el repositorio. """
    run('git clone https://github.com/Antkk10/BotPaisesYCapitales.git')
    run('cd BotPaisesYCapitales/ && pip install -r requirements.txt')

def EjecutarApp():
    """ Función para ejecutar el Bot. """
    with shell_env(TOKENBOT=os.environ['TOKENBOT']):
        run('sudo supervisorctl reload')
        run('sudo supervisorctl update')
        run('sudo supervisorctl start botpaisesycapitales')

def StopApp():
    """ Función que para el bot. """
    run('sudo supervisorctl stop botpaisesycapitales')

def borrar():
    run('rm -Rf BotPaisesYCapitales/')
