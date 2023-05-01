from mfrc522 import MFRC522
import time

lector = MFRC522(spi_id=0, sck=2, miso=4, mosi=3, cs=1, rst=0)

print("Lector activo...\n")

usuarios_admitidos = [2853815699]

usuarios_trabajando = []

while True:
    lector.init()
    (stat, tag_type) = lector.request(lector.REQIDL)
    if stat == lector.OK:
        (stat, uid) = lector.SelectTagSN()
        if stat == lector.OK:
            print('LEYENDO...')
            time.sleep(2) 
            identificador = int.from_bytes(bytes(uid), "little", False)

            if identificador not in usuarios_admitidos:
                print('ERROR: ACCESO NO AUTORIZADO PARA ' + str(identificador))
            elif identificador not in usuarios_trabajando and identificador in usuarios_admitidos:
                usuarios_trabajando.append(identificador)
                print('ACCESO OTORGADO A: ' + str(identificador))
            elif identificador in usuarios_trabajando:
                usuarios_trabajando.remove(identificador)
                print('SALIDA REGISTRADA DE: ' + str(identificador))

            t = time.localtime()

            # Mostrar la hora actual en formato HH:MM:SS
            hora_actual = "{:02d}:{:02d}:{:02d}".format(t[3], t[4], t[5])
            print("HORA:", hora_actual)
