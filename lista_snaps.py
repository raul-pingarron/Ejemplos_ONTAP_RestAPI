#!/opt/anaconda3/bin/python3

""" 
Este programa lista todos los snapshots de un FlexVol 
"""

import argparse, logging
from typing import List
from netapp_ontap import NetAppRestError, config, HostConnection
from netapp_ontap.resources import Svm, Volume, Snapshot

def setup_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] [%(levelname)5s] [%(module)s:%(lineno)s] %(message)s",
    )


def establece_conexion(cluster: str, api_user: str, api_pass: str) -> None:
    config.CONNECTION = HostConnection(
        cluster, username=api_user, password=api_pass, verify=False,
    )


def devuelve_uid_vol(svm_name, vol_name):
    try:
        for volume in Volume.get_collection(
                **{"svm.name":svm_name}, **{"name":vol_name}, fields="uuid"):
            print()
            print(
                "Listado de Snapshots para el volumen %s\n UUID de volumen %s" %
                (volume.name, volume.uuid))
            return volume.uuid
    except NetAppRestError as error:
        print("Por favor, INTRODUZCA EL NOMBRE DEL VOLUMEN!\n"+error.http_err_response.http_response.text)

    
def lista_snapshots(vol_uuid)-> None: 
    print()
    try:
        for snapshot in Snapshot.get_collection(vol_uuid):
            print(" - "+snapshot.name)
    except NetAppRestError as error:
        print("Volumen inexistente!\n "+error.http_err_response.http_response.text)
        print("   --- por favor, especifique un volumen valido ---")
    print("\n")


def main() -> None:

    analiza_argumentos = argparse.ArgumentParser(prog='lista_snaps',
                                    usage='%(prog)s nombre_volumen',
                                    description='Lista los snapshots del volumen especificado')

    analiza_argumentos.add_argument("Nombre_vol",metavar="nombre_volumen",type=str,help="nombre del volumen")
    argumentos = analiza_argumentos.parse_args()
    
    cluster = "10.67.216.10"
    usuario_api = "admin"
    pasguord = "N3tApp00"
    svm = "svm-demos"
    """vol = "share1_unix" """

    setup_logging()
    establece_conexion(cluster, usuario_api, pasguord)
    uid_vol = devuelve_uid_vol(svm, argumentos.Nombre_vol)
    lista_snapshots(uid_vol)

if __name__ == "__main__":
    main()
