pacientes = []
dias_marcados = []
horarios_marcados = []
dias_disponiveis = []
profissionais = []
profissionais_lista = []
repetir_operacao = 1
repetir_psicologo = 0
repetir_tudo = 0
dom = []
seg = []
ter = []
qua = []
qui = []
sex = []
sab = []
dom_marc = []
seg_marc = []
ter_marc = []
qua_marc = []
qui_marc = []
sex_marc = []
sab_marc = []
while repetir_operacao == 1:
    dias = input("escolha o dia da semana para disponibilizar (usando apenas as 3 primeiras letras do dia, ex: domingo = dom): ")
    dias.lower()
    if dias == "dom":
        if "dom" in dias_disponiveis:
            reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
            if reestabelecer == 1:
                dom.clear()
                print("Horários do dia mantido.")
            else:
                if reestabelecer == 0:
                    print("Horários apagados")
                    s_n_remarcar = 0
                    while s_n_remarcar == 0:
                        horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                        if horario in dom:
                            print("Esse horário já esta ocupado.")
                            s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        else:
                            if horario >= 25:
                                print("Esse horário não existe.")
                                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            else:
                                dom.append(horario)
                                print("Horário marcado")
                                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                    if s_n_remarcar == 1:
                        print ("Horários marcados")
                    else:
                        print ("Opção inválida.")
                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
        else:
            dias_disponiveis.append("dom")
            s_n_remarcar = 0
            while s_n_remarcar == 0:
                horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                if horario in dom:
                    print("Esse horário já esta ocupado.")
                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                else:
                    if horario >= 25:
                        print("Esse horário não existe.")
                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                    else:
                        dom.append(horario)
                        print("Horário marcado")
                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
            if s_n_remarcar == 1:
                print("Horários marcados")
                repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
            else:
                print("Opção inválida.")
                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
    else:
        if dias == "seg":
            if "seg" in dias_disponiveis:
                reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                if reestabelecer == 1:
                    seg.clear()
                    print("Horários do dia mantido.")
                else:
                    if reestabelecer == 0:
                        print("Horários apagados")
                        s_n_remarcar = 0
                        while s_n_remarcar == 0:
                            horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                            if horario in seg:
                                print("Esse horário já esta ocupado.")
                                s_n_remarcar = int(
                                    input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            else:
                                if horario >= 25:
                                    print("Esse horário não existe.")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                else:
                                    seg.append(horario)
                                    print("Horário marcado")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        if s_n_remarcar == 1:
                            print("Horários marcados")
                        else:
                            print("Opção inválida.")
            else:
                dias_disponiveis.append("seg")
                s_n_remarcar = 0
                while s_n_remarcar == 0:
                    horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                    if horario in seg:
                        print("Esse horário já esta ocupado.")
                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                    else:
                        if horario >= 25:
                            print("Esse horário não existe.")
                            s_n_remarcar = int(
                                input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        else:
                            seg.append(horario)
                            print("Horário marcado")
                            s_n_remarcar = int(
                                input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                if s_n_remarcar == 1:
                    print("Horários marcados")
                    repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                else:
                    print("Opção inválida.")
                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                    repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
        else:
            if dias == "ter":
                if "ter" in dias_disponiveis:
                    reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                    if reestabelecer == 1:
                        ter.clear()
                        print("Horários do dia mantido.")
                    else:
                        if reestabelecer == 0:
                            print("Horários apagados")
                            s_n_remarcar = 0
                            while s_n_remarcar == 0:
                                horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                                if horario in ter:
                                    print("Esse horário já esta ocupado.")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                else:
                                    if horario >= 25:
                                        print("Esse horário não existe.")
                                        s_n_remarcar = int(
                                            input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    else:
                                        ter.append(horario)
                                        print("Horário marcado")
                                        s_n_remarcar = int(
                                            input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            if s_n_remarcar == 1:
                                print("Horários marcados")
                            else:
                                print("Opção inválida.")
                else:
                    dias_disponiveis.append("ter")
                    s_n_remarcar = 0
                    while s_n_remarcar == 0:
                        horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                        if horario in ter:
                            print("Esse horário já esta ocupado.")
                            s_n_remarcar = int(
                                input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        else:
                            if horario >= 25:
                                print("Esse horário não existe.")
                                s_n_remarcar = int(
                                    input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            else:
                                ter.append(horario)
                                print("Horário marcado")
                                s_n_remarcar = int(
                                    input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                    if s_n_remarcar == 1:
                        print("Horários marcados")
                        repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                    else:
                        print("Opção inválida.")
                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
            else:
                if dias == "qua":
                    if "qua" in dias_disponiveis:
                        reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                        if reestabelecer == 1:
                            qua.clear()
                            print("Horários do dia mantido.")
                        else:
                            if reestabelecer == 0:
                                print("Horários apagados")
                                s_n_remarcar = 0
                                while s_n_remarcar == 0:
                                    horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                                    if horario in qua:
                                        print("Esse horário já esta ocupado.")
                                        s_n_remarcar = int(
                                            input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    else:
                                        if horario >= 25:
                                            print("Esse horário não existe.")
                                            s_n_remarcar = int(
                                                input(
                                                    "Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        else:
                                            qua.append(horario)
                                            print("Horário marcado")
                                            s_n_remarcar = int(
                                                input(
                                                    "Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                if s_n_remarcar == 1:
                                    print("Horários marcados")
                                else:
                                    print("Opção inválida.")
                    else:
                        dias_disponiveis.append("qua")
                        s_n_remarcar = 0
                        while s_n_remarcar == 0:
                            horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                            if horario in qua:
                                print("Esse horário já esta ocupado.")
                                s_n_remarcar = int(
                                    input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            else:
                                if horario >= 25:
                                    print("Esse horário não existe.")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                else:
                                    qua.append(horario)
                                    print("Horário marcado")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                        if s_n_remarcar == 1:
                            print("Horários marcados")
                            repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                        else:
                            print("Opção inválida.")
                            s_n_remarcar = int(
                                input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                else:
                    if dias == "qui":
                        if "qui" in dias_disponiveis:
                            reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                            if reestabelecer == 1:
                                qui.clear()
                                print("Horários do dia mantido.")
                            else:
                                if reestabelecer == 0:
                                    print("Horários apagados")
                                    s_n_remarcar = 0
                                    while s_n_remarcar == 0:
                                        horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                                        if horario in qui:
                                            print("Esse horário já esta ocupado.")
                                            s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        else:
                                            if horario >= 25:
                                                print("Esse horário não existe.")
                                                s_n_remarcar = int(
                                                    input(
                                                        "Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                            else:
                                                qui.append(horario)
                                                print("Horário marcado")
                                                s_n_remarcar = int(
                                                    input(
                                                        "Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    if s_n_remarcar == 1:
                                        print("Horários marcados")
                                    else:
                                        print("Opção inválida.")
                        else:
                            dias_disponiveis.append("qui")
                            s_n_remarcar = 0
                            while s_n_remarcar == 0:
                                horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                                if horario in qui:
                                    print("Esse horário já esta ocupado.")
                                    s_n_remarcar = int(
                                        input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                else:
                                    if horario >= 25:
                                        print("Esse horário não existe.")
                                        s_n_remarcar = int(
                                            input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    else:
                                        qui.append(horario)
                                        print("Horário marcado")
                                        s_n_remarcar = int(
                                            input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                            if s_n_remarcar == 1:
                                print("Horários marcados")
                                repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                            else:
                                print("Opção inválida.")
                                s_n_remarcar = int(
                                    input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                    else:
                        if dias == "sex":
                            if "sex" in dias_disponiveis:
                                reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                                if reestabelecer == 1:
                                    sex.clear()
                                    print("Horários do dia mantido.")
                                else:
                                    if reestabelecer == 0:
                                        print("Horários apagados")
                                        s_n_remarcar = 0
                                        while s_n_remarcar == 0:
                                            horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                                            if horario in sex:
                                                print("Esse horário já esta ocupado.")
                                                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                            else:
                                                if horario >= 25:
                                                    print("Esse horário não existe.")
                                                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                                else:
                                                    sex.append(horario)
                                                    print("Horário marcado")
                                                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        if s_n_remarcar == 1:
                                            print("Horários marcados")
                                        else:
                                            print("Opção inválida.")
                            else:
                                dias_disponiveis.append("sex")
                                s_n_remarcar = 0
                                while s_n_remarcar == 0:
                                    horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                                    if horario in sex:
                                        print("Esse horário já esta ocupado.")
                                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    else:
                                        if horario >= 25:
                                            print("Esse horário não existe.")
                                            s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        else:
                                            sex.append(horario)
                                            print("Horário marcado")
                                            s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                if s_n_remarcar == 1:
                                    print("Horários marcados")
                                    repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                                else:
                                    print("Opção inválida.")
                                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                        else:
                            if dias == "sab":
                                if "sab" in dias_disponiveis:
                                    reestabelecer = int(input("Esse dia já está ocupado, deseja redefinir o horários? (0 = sim, 1 = não): "))
                                    if reestabelecer == 1:
                                        sab.clear()
                                        print("Horários do dia mantido.")
                                    else:
                                        if reestabelecer == 0:
                                            print("Horários apagados")
                                            s_n_remarcar = 0
                                            while s_n_remarcar == 0:
                                                horario = int(input("Deseja disponibilizar qual horário para o dia? "))
                                                if horario in sab:
                                                    print("Esse horário já esta ocupado.")
                                                    s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                                else:
                                                    if horario >= 25:
                                                        print("Esse horário não existe.")
                                                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                                    else:
                                                        sab.append(horario)
                                                        print("Horário marcado")
                                                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                            if s_n_remarcar == 1:
                                                print("Horários marcados")
                                            else:
                                                print("Opção inválida.")
                                else:
                                    dias_disponiveis.append("sab")
                                    s_n_remarcar = 0
                                    while s_n_remarcar == 0:
                                        horario = int(input("Qual horário gostaria de disponibilizar para esse dia? "))
                                        if horario in sab:
                                            print("Esse horário já esta ocupado.")
                                            s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        else:
                                            if horario >= 25:
                                                print("Esse horário não existe.")
                                                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                            else:
                                                sab.append(horario)
                                                print("Horário marcado")
                                                s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                    if s_n_remarcar == 1:
                                        print("Horários marcados")
                                        repetir_operacao = int(
                                            input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                                    else:
                                        print("Opção inválida.")
                                        s_n_remarcar = int(input("Deseja disponibilizar outra hora nesse dia? (0 = sim, 1 = não): "))
                                        repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))
                            else:
                                print("opção inválida")
                                repetir_operacao = int(input("Finalizar operação ou escolher outro dia? (0 = finalizar, 1 = escolher outro dia): "))

else:
    if repetir_operacao == 0:
        nome = str(input("Nome do profissional: "))
        if nome in profissionais:
            print("Nome já escolhido, insira outro nome")
            repetir_operacao = 0
        else:
            profissionais.append(nome)
            nome = []
            profissionais_lista.append(nome)
        repetir_agenda = int(input("Criar agenda para outro psicólogo ou marcar consulta? (0 = criar agenda, 1 = marcar consulta): "))
        if repetir_agenda == 1:
            print("Operação finalizada.")
            print(profissionais)
            repetir_mostra = 0
            while repetir_mostra == 0:
                psicologos = input("escolha um dos psicólogos acima: ")
                if psicologos in profissionais:
                    print(dias_disponiveis)
                    dias_marcar = input("Escolha um dos dias acima para vizualizar os horários disponíveis: ")
                    if dias_marcar in dias_disponiveis:
                        if dias_marcar == "dom":
                            print("os horários de Domingo são: ", dom)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in dom:
                                    dom.remove(marcar_horario)
                                    dom_marc.append(marcar_horario)
                                    dias_marcados.append("dom")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "seg":
                            print("os horários de Segunda-Feira são: ", seg)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in seg:
                                    seg.remove(marcar_horario)
                                    seg_marc.append(marcar_horario)
                                    dias_marcados.append("seg")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "ter":
                            print("os horários de Terça-Feira são: ", ter)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(
                                    input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in ter:
                                    ter.remove(marcar_horario)
                                    ter_marc.append(marcar_horario)
                                    dias_marcados.append("ter")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(
                                        input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(
                                        input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "qua":
                            print("os horários de Quarta-Feira são: ", qua)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(
                                    input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in qua:
                                    qua.remove(marcar_horario)
                                    qua_marc.append(marcar_horario)
                                    dias_marcados.append("qua")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(
                                        input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(
                                        input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "qui":
                            print("os horários de Quinta-Feira são: ", qui)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(
                                    input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in qui:
                                    qui.remove(marcar_horario)
                                    qui_marc.append(marcar_horario)
                                    dias_marcados.append("qui")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(
                                        input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(
                                        input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "sex:":
                            print("os horários de Sexta-Feira são: ", sex)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(
                                    input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in sex:
                                    sex.remove(marcar_horario)
                                    sex_marc.append(marcar_horario)
                                    dias_marcados.append("sex")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        elif dias_marcar == "sab":
                            print("os horários de Sábado são: ", sab)
                            marcar_horario_s_n = int(input("deseja marcar um horário? (0 = sim, 1 = não)"))
                            if marcar_horario_s_n == 0:
                                marcar_horario = int(
                                    input("em qual horário desse dia você deseja marcar sua consluta? "))
                                if marcar_horario in sab:
                                    sab.remove(marcar_horario)
                                    sab_marc.append(marcar_horario)
                                    dias_marcados.append("sab")
                                    print("Horário marcado.")
                                else:
                                    marcar_horario_s_n = int(
                                        input("Horário indisponível, deseja marcar outro horário? (0 = sim, 1 = não)"))
                            else:
                                if marcar_horario_s_n == 1:
                                    repetir_mostra = int(
                                        input("Visualizar agenda de outro psicólogo? (0 = sim, 1 = não): "))
                        else:
                            print("esse dia não existe:")
                    else:
                        print("Esse dia não foi disponibilizado pelo profissional.")
                        print(dias_disponiveis)
                        dias_marcar = input("Escolha um dos dias acima para vizualizar os horários disponíveis: ")
                else:
                    repetir_mostra = int(input("Esse psicólogo não está disponível, ver os horários de outro profissional?: (0 = sim, 1 = não)"))
                    if repetir_mostra == 1:
                        repetir_tudo = int(input("marcar mais horários ou encerrar? (0 = marcar mais, 1 = encerrar) "))
                    elif repetir_tudo == 1:
                        nome_paciente = str(input("Nome do Paciente (caso não tenha marcado horário aperte espaço e enter): "))
                        pacientes.append(nome_paciente)
                        nome_paciente = []
                        nome_paciente.append(dias_marcados)
                        ver_pacientes_marcados = int(input("Vizualizar pacientes marcados? (0 = sim, 1 = não): "))
                        if ver_pacientes_marcados == 0:
                            print(pacientes)
                            sel_paciente = str(input("Selecione um paciente acima para ver seus horários: "))
                            if sel_paciente in pacientes:
                                print(dias_marcados)
                                dias_marcados_sel = str(input("Selecione um dos dias acima para ver os horários marcados: "))
                                if dias_marcados_sel in dias_marcados:
                                    if dias_marcados_sel == "seg":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", seg_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "dom":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", dom_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "ter":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", ter_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "qua":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", qua_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "qui":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", qui_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "sex":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", sex_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    elif dias_marcados_sel == "sab":
                                        print("os horários que", sel_paciente, "marcou esse dia são: ", sab_marc)
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                                    else:
                                        print("indisponíverl")
                                        ver_pacientes_marcados = int(input("Visualizar outro paciente ou encerrar? (0 = visualizar, 1 = encerrar): "))
                        elif ver_pacientes_marcados == 1:
                            break
        elif repetir_agenda == 0:
            repetir_operacao = 1