from django.shortcuts import render

from .aestrella_llantas import (
    buscar_solucion_Aestrella,
    costos
)


def index(request):

    resultado = None

    total = 0

    if request.method == 'POST':

        try:

            # --------------------------------
            # EMPRESA 1
            # --------------------------------

            costos['Empresa1']['T'] = int(
                request.POST.get('E1T', 0)
            )

            costos['Empresa1']['H'] = int(
                request.POST.get('E1H', 0)
            )

            costos['Empresa1']['V'] = int(
                request.POST.get('E1V', 0)
            )

            costos['Empresa1']['W'] = int(
                request.POST.get('E1W', 0)
            )

            # --------------------------------
            # EMPRESA 2
            # --------------------------------

            costos['Empresa2']['T'] = int(
                request.POST.get('E2T', 0)
            )

            costos['Empresa2']['H'] = int(
                request.POST.get('E2H', 0)
            )

            costos['Empresa2']['V'] = int(
                request.POST.get('E2V', 0)
            )

            costos['Empresa2']['W'] = int(
                request.POST.get('E2W', 0)
            )

            # --------------------------------
            # EMPRESA 3
            # --------------------------------

            costos['Empresa3']['T'] = int(
                request.POST.get('E3T', 0)
            )

            costos['Empresa3']['H'] = int(
                request.POST.get('E3H', 0)
            )

            costos['Empresa3']['V'] = int(
                request.POST.get('E3V', 0)
            )

            costos['Empresa3']['W'] = int(
                request.POST.get('E3W', 0)
            )

            # --------------------------------
            # EMPRESA 4
            # --------------------------------

            costos['Empresa4']['T'] = int(
                request.POST.get('E4T', 0)
            )

            costos['Empresa4']['H'] = int(
                request.POST.get('E4H', 0)
            )

            costos['Empresa4']['V'] = int(
                request.POST.get('E4V', 0)
            )

            costos['Empresa4']['W'] = int(
                request.POST.get('E4W', 0)
            )

            # --------------------------------
            # EJECUTAR A*
            # --------------------------------

            estado_inicial = {}

            solucion = ['T', 'H', 'V', 'W']

            nodo_solucion = buscar_solucion_Aestrella(
                estado_inicial,
                solucion
            )

            datos = nodo_solucion.get_datos()

            resultado = []

            for tipo in datos:

                empresa = datos[tipo]

                precio = costos[empresa][tipo]

                total = total + precio

                resultado.append(
                    (tipo, empresa, precio)
                )

        except Exception as e:

            print("ERROR:", e)

    return render(
        request,
        'llantas_app/index.html',
        {
            'resultado': resultado,
            'total': total
        }
    )