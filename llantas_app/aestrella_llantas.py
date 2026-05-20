from arbol import Nodo


costos = {
    'Empresa1': {'T': 20, 'H': 30, 'V': 20, 'W': 40},
    'Empresa2': {'T': 50, 'H': 50, 'V': 40, 'W': 50},
    'Empresa3': {'T': 60, 'H': 55, 'V': 50, 'W': 60},
    'Empresa4': {'T': 100, 'H': 80, 'V': 60, 'W': 70}
}


def heuristica(asignacion):

    tipos = ['T', 'H', 'V', 'W']

    empresas_usadas = []

    for tipo in asignacion:
        empresas_usadas.append(asignacion[tipo])

    h = 0

    for tipo in tipos:

        if tipo not in asignacion:

            minimo = 9999

            for empresa in costos:

                if empresa not in empresas_usadas:

                    valor = costos[empresa][tipo]

                    if valor < minimo:
                        minimo = valor

            h = h + minimo

    return h


def buscar_solucion_Aestrella(estado_inicial, solucion):

    solucionado = False

    nodos_visitados = []
    nodos_frontera = []

    nodo_inicial = Nodo(estado_inicial)

    nodo_inicial.set_costo(0)

    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:

        nodos_frontera = sorted(
            nodos_frontera,
            key=lambda x: x.get_costo()
        )

        nodo = nodos_frontera[0]

        nodos_visitados.append(
            nodos_frontera.pop(0)
        )

        if len(nodo.get_datos()) == len(solucion):

            solucionado = True
            return nodo

        else:

            dato_nodo = nodo.get_datos()

            lista_hijos = []

            tipos = ['T', 'H', 'V', 'W']

            tipo_actual = tipos[len(dato_nodo)]

            empresas_usadas = []

            for tipo in dato_nodo:
                empresas_usadas.append(
                    dato_nodo[tipo]
                )

            for empresa in costos:

                if empresa not in empresas_usadas:

                    hijo_datos = dict(dato_nodo)

                    hijo_datos[tipo_actual] = empresa

                    hijo = Nodo(hijo_datos)

                    g = 0

                    for tipo in hijo_datos:

                        empresa_asignada = hijo_datos[tipo]

                        g = g + costos[empresa_asignada][tipo]

                    h = heuristica(hijo_datos)

                    f = g + h

                    hijo.set_costo(f)

                    hijo.set_padre(nodo)

                    lista_hijos.append(hijo)

                    if not hijo.en_lista(nodos_visitados):

                        if hijo.en_lista(nodos_frontera):

                            for n in nodos_frontera:

                                if n.igual(hijo) and \
                                   n.get_costo() > hijo.get_costo():

                                    nodos_frontera.remove(n)
                                    nodos_frontera.append(hijo)

                                    break

                        else:

                            nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)

    return None