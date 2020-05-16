#!/opt/anaconda3/bin/python3

"""
Este programa crea 100 clones de un FlexVol
"""

import argparse
import logging
from netapp_ontap import NetAppRestError, config, HostConnection
from netapp_ontap.resources import Volume


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
        for volumen in Volume.get_collection(
                **{"svm.name": svm_name}, **{"name": vol_name}, fields="uuid"):
            return volumen.uuid
    except NetAppRestError as error:
        print("Por favor, INTRODUZCA EL NOMBRE DEL VOLUMEN!\n" + error.http_err_response.http_response.text)


def clona_volumen(svm_name, vol_name, vol_uuid, num_clones) -> None:
    for i in range(1, num_clones+1):
        dataobj = {}
        clone_name = vol_name + "__clon_" + str(i)

        tmp = {'name': svm_name}
        dataobj['svm'] = tmp
        dataobj['name'] = clone_name

        clone_volume_json = {
            "is_flexclone": bool("true"),
            "parent_svm":
                {
                    "name": svm_name,
                },
            "parent_volume": {
                "name": vol_name,
                "uuid": vol_uuid
            }
        }

        dataobj['clone'] = clone_volume_json

        try:
            volume = Volume.from_dict(dataobj)
            if volume.post(poll=True):
                print("El CLON  %s se ha creado satisfactoriamente" % volume.name)
        except NetAppRestError as error:
            print('ERROR !\n {0}'.format(error.http_err_response.http_response.text))
        print("\n")


def main() -> None:
    analiza_argumentos = argparse.ArgumentParser(prog="crea_clones",
                                                 usage="%(prog)s nombre_volumen numero_clones",
                                                 description="Crea el numero de clones del volumen especificado")

    analiza_argumentos.add_argument("nombre_vol", metavar="nombre_volumen", type=str, help="nombre del volumen")
    analiza_argumentos.add_argument("num_clones", metavar="num_clones", type=int, help="numero de clones")
    argumentos = analiza_argumentos.parse_args()

    cluster = "cluster01.ntap.demolab.es"
    usuario_api = "admin"
    pasguord = "tururutururu"
    svm = "svm-demos"

    setup_logging()
    establece_conexion(cluster, usuario_api, pasguord)
    uid_vol = devuelve_uid_vol(svm, argumentos.nombre_vol)
    print()
    clona_volumen(svm, argumentos.nombre_vol, uid_vol, argumentos.num_clones)


if __name__ == "__main__":
    main()
