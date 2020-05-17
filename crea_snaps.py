#!/opt/anaconda3/bin/python3
"""
Este programa crea tantos snapshots de un FlexVol como se especifique
Uso: crea_snaps.py nombre_volumen numero_snaps
Ej:  $ python3 crea_snaps.py test_vol 10
"""

import argparse
import logging
from netapp_ontap import NetAppRestError, config, HostConnection
from netapp_ontap.resources import Volume, Snapshot


def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )


def establece_conexion(cluster: str, api_user: str, api_pass: str) -> None:
    config.CONNECTION = HostConnection(
        cluster, username=api_user, password=api_pass, verify=False,
    )


def crea_snaps(svm_name, vol_name, num_snaps) -> None:
    for i in range(1, num_snaps + 1):
        snap_name = vol_name + "__snap_" + str(i)

        volume = Volume.find(**{'svm.name': svm_name, 'name': vol_name})
        snapshot = Snapshot(volume.uuid, name=snap_name)

        try:
            snapshot.post()
            print("Snapshot %s creado satisfactoriamente" % snapshot.name)
        except NetAppRestError as err:
            print("Error: no se ha podido crear el snapshot - %s" % err)


def main() -> None:
    analiza_argumentos = argparse.ArgumentParser(prog="crea_snaps",
                                                 usage="%(prog)s nombre_volumen numero_snaps",
                                                 description="Crea un numero de snaps del volumen especificado")

    analiza_argumentos.add_argument("nombre_vol", metavar="nombre_volumen", type=str, help="nombre del volumen")
    analiza_argumentos.add_argument("num_snaps", metavar="num_snaps", type=int, help="numero de snapshots")
    argumentos = analiza_argumentos.parse_args()

    cluster = "10.67.216.10"
    usuario_api = "admin"
    pasguord = "N3tApp00"
    svm = "svm-demos"

    setup_logging()
    establece_conexion(cluster, usuario_api, pasguord)
    print()
    crea_snaps(svm, argumentos.nombre_vol, argumentos.num_snaps)


if __name__ == "__main__":
    main()
