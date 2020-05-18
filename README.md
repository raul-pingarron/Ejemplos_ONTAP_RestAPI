# Ejemplos de la API REST de ONTAP con Python
A partir de la versión 9.6 de ONTAP® se incluye el soporte para una API RESTful muy extensiva que permite automatizar, desplegar y administrar sistemas de almacenamiento NetApp®.   

Algunas características importantes:
- Todo el tráfico entre el cliente y el LIF de ONTAP al que se ataca está encriptado (generalmente TLS, según la configuración de ONTAP).
- La conexión se puede realizae a través del Cluster Management LIF, o del Node Management LIF o incluso del SVM Management LIF.
- La API está versionada, para acceder directamente a la última versión la ruta a utilizar es `https://<cluster_mgmt_ip_address>/api`; para acceder a otra versión la ruta es `https://<cluster_mgmt_ip_address>/api/v1`
- Es posible acceder a la documentación online de la API desde `https://<cluster_mgmt_ip_address>/docs/api`  
- El nuevo ONTAP System Manager 9.7 está completamente construido de manera nativa a partir de la API REST de ONTAP REST y el usuario puede ver las llamadas a la API que System Manager va haciendo en cada movimiento a través de la GUI. Esto ayuda al usuario a entender estas llamadas a la API y es especialmente útil para usar como ejemplo durante el desarrollo de scripts.   

![Screenshot](https://github.com/raul-pingarron/raul-pingarron.github.io/blob/master/images/ocum97_api.png)   

La documentación completa está en <a href="https://docs.netapp.com/ontap-9/topic/com.netapp.nav.api/home.html" target="_blank">https://docs.netapp.com/ontap-9/topic/com.netapp.nav.api/home.html</a>.

## Librería Python para la API REST de ONTAP
La librería de la API REST de ONTAP para Python permite acceder a las llamadas de la API a través de Python, permitiendo gestionar la conexión al clúster, el procesamiento asíncrono de peticiones y la gestión de excepciones. 

La librería se puede descargar e instalar desde el PyPi.org, el repositorio global de paquetes de Python.
La documentación y la última versión están disponibles en <a href="https://pypi.org/project/netapp-ontap/" target="_blank">https://pypi.org/project/netapp-ontap/</a>.


Este repositorio contiene algunos scripts muy básicos de ejemplo que ilustran cómo utilizar la API REST de ONTAP en Python. 

En el <a href="https://github.com/NetApp/ontap-rest-python" target="_blank">repositorio de NetApp</a> se pueden encontrar muy buenos ejemplos.
