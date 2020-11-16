# -*- coding: utf-8 -*-
# API
API_DEBUG = True
# REDIS
REDIS_IP = 'redis'  # Le llamo así porque todo está orquestado por el docker-compose y en el archivo docker-compose.yml
                    # llamo así al servicio Redis
REDIS_DB_ID = 0  # Es un identificador para la base de datos
REDIS_PORTS = 6379  # Son los puertos que por defecto vienen para redis
REDIS_QUEUE = 'service_queue'  # Asigno nombre a la cola de redis
SERVER_SLEEP = 1  # Seteo los segundos de idle hasta que se borra los mensajes ya leidos de la cola de redis
