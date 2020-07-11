print("para candidato A vote 1, para candidato B vote 2, para candidato C vote 3")
c1 = 0
c2 = 0
c3 = 0
quantidade_de_eleitores = 0
ciclo = 0
ciclo_voto = 0
while ciclo == 0:
    ciclo_voto = int(input("Iniciar votação? (0 = sim, 1 = não): "))
    while ciclo_voto == 0:
        voto = int(input("vote em um candidato: "))
        if voto == 1:
            confirma = int(input("Confirmar voto em candidato A? (0 = sim, 1 = não): "))
            if confirma == 1:
                print("Voto Cancelado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            elif confirma == 0:
                quantidade_de_eleitores = quantidade_de_eleitores + 1
                c1 = c1 + 1
                print("Voto Confirmado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            else:
                print("Opção indisponível")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
        elif voto == 2:
            confirma = int(input("Confirmar voto em candidato B? (0 = sim, 1 = não): "))
            if confirma == 1:
                print("Voto Cancelado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            elif confirma == 0:
                quantidade_de_eleitores = quantidade_de_eleitores + 1
                c2 = c2 + 1
                print("Voto Confirmado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            else:
                print("Opção indisponível")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
        elif voto == 3:
            confirma = int(input("Confirmar voto em candidato C? (0 = sim, 1 = não): "))
            if confirma == 1:
                print("Voto Cancelado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            elif confirma == 0:
                quantidade_de_eleitores = quantidade_de_eleitores + 1
                c3 = c3 + 1
                print("Voto Confirmado")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
            else:
                print("Opção indisponível")
                ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))
        else:
            print("Opção indisponível.")
            ciclo_voto = int(input("Votar novamente ou encerrar? (0 = Votar, 1 = Encerrar): "))

    else:
        if ciclo_voto == 1:
            print("votação encerrada")
            print("o total de eleitores foi ", quantidade_de_eleitores)
            print("o candidato A teve ", c1, "votos.")
            print("o candidato B teve ", c2, "votos.")
            print("o candidato C teve ", c3, "votos.")
            ciclo = 1

        else:
            print("Opção indisponível")
            ciclo_voto = int(input("Iniciar votação? (0 = sim, 1 = não): "))