#CONFIGURAÇÃO INICIAL DO SISTEMA E INICIALIZAÇÃO DAS VARIÁVEIS

num_total_tickets = 2000
num_tickets_vip = 0

price_tickets_with_discount = 10.00
            
price_tickets_full = 30.00

num_tickets_reserved = 0

price_tickets_half = price_tickets_full / 2

num_tickets_half_student = 0
num_tickets_half_old = 0

total_num_tickets_half = num_tickets_half_student + num_tickets_half_old

num_tickets_full = 0

num_promotional_tickets = 0

num_disponible_tickets = num_total_tickets - num_tickets_vip

total_age = 0

num_tickets_sold_by_1 = 0
num_tickets_sold_by_2 = 0
num_tickets_sold_by_3 = 0

#INICIALIZAÇÃO DAS SENHAS

manager_password = 'y'
vendor_password = 'x'
vip_password = 'vip@pass2024'
promotional_password = 'ecomp20241'

option = '0'

age = 0

#INICIALIZAÇÃO DO SISTEMA


print('Sistema iniciando...\n')

while option != '4':

    print('\n===== SELECIONE O TIPO DE ACESSO =====\n')
    print('[1] - Gerenciador')
    print('[2] - Vendedor')
    print('[3] - Comprador')
    print('[4] - Encerrar\n')

    option = str(input('Insira uma opção: '))

    if option == '1':

        manager_password_confirm = str(input('\nInsira a senha para continuar: '))

        if manager_password_confirm == manager_password:

            print('\n===== SELECIONE UMA OPÇÃO =====\n')
            print('[1] - Configurar o sistema')
            print('[2] - Visualizar informações')
            print('[3] - Alterar senhas')
            print('[4] - Voltar\n')

            manager_option = str(input('Insira uma opção: '))

            if manager_option == '1':

                num_total_tickets = int(input('\nDefina a quantidade de ingressos totais: '))

                num_tickets_reserved = int(input('\nDefina a quantidade de ingressos reservados: '))

                price_tickets_with_discount = float(input('\nDigite o preço dos ingressos promocionais: '))
                
                price_tickets_full = float(input('\nDigite o valor dos ingressos na modalidade Inteira: '))

                price_tickets_half = price_tickets_full / 2

            elif manager_option == '2':

                #ATUALIZAÇÃO DOS DADOS

                sold_tickets = num_total_tickets - num_disponible_tickets
                unsold_tickets = num_disponible_tickets

                num_tickets_courtesy_1 = num_tickets_sold_by_1 // 10 #Cortesias para Tipo 1 (Biologia)
                num_tickets_courtesy_2 = num_tickets_sold_by_2 // 10 #Cortesias para Tipo 2 (Enfermagem)
                num_tickets_courtesy_3 = num_tickets_sold_by_3 // 10 #Cortesias para Tipo 3 (não definido)

                collection_full = price_tickets_full * num_tickets_full
                collection_half_student = price_tickets_half * num_tickets_half_student
                collection_half_old = price_tickets_half * num_tickets_half_old
                collection_promotional = price_tickets_with_discount * num_promotional_tickets
                 
                print(f'\n[Ingressos emitidos - {sold_tickets}]')
                print(f'[Ingressos não emitidos] - {unsold_tickets}\n')

                print('=' * 40, '\n')

                print(f'[Ingressos Inteira vendidos] - {num_tickets_full}')
                print(f'[Ingressos Estudante vendidos] - {num_tickets_half_student}')
                print(f'[Ingressos Idoso vendidos] - {num_tickets_half_old}')
                print(f'[Ingressos Promocionais vendidos] - {num_promotional_tickets}')
                print(f'[Ingressos VIP emitidos] - {num_tickets_vip}\n')

                print('=' * 40, '\n')

                print(f'[Ingressos vendidos por Tipo 1] - {num_tickets_sold_by_1}')
                print(f'[Ingressos vendidos por Tipo 2] - {num_tickets_sold_by_2}')
                print(f'[Ingressos vendidos por Tipo 3] - {num_tickets_sold_by_3}\n')

                print('=' * 40, '\n')

                print(f'[Cortesias para Tipo 1] - {num_tickets_courtesy_1}')
                print(f'[Cortesias para Tipo 2] - {num_tickets_courtesy_2}')
                print(f'[Cortesias para Tipo 3] - {num_tickets_courtesy_3}\n')

                print('=' * 40, '\n')

                print(f'[Arrecadação do tipo Inteira] - R${collection_full:.2f}')
                print(f'[Arrecadação do tipo Estudante] - R${collection_half_student:.2f}')
                print(f'[Arrecadação do tipo Idoso] - R${collection_half_old:.2f}')
                print(f'[Arrecadação do tipo Promocional] - R${collection_promotional:.2f}\n')

                print(f'[Arrecadação Total] - R${(price_tickets_full * num_tickets_full) + (price_tickets_half * num_tickets_half_old) + (price_tickets_half * num_tickets_half_student) + (price_tickets_with_discount * num_promotional_tickets):.2f}\n')

                print('=' * 40, '\n')

                print(f'O ingresso Inteira foi vendido {num_tickets_full} vezes. O ingresso Estudante {num_tickets_half_student} vezes. O ingresso Idoso {num_tickets_half_old} vezes. O ingresso Promocional {num_promotional_tickets} vezes. E o ingresso {num_tickets_vip}')

                if sold_tickets > 0:

                    print(f'[Idade média do evento] - {total_age / sold_tickets}\n')

                else:
                    print('\nA média de idade não foi possível de ser calculada.\n')

            elif manager_option == '3':
                print('\n[1] - Alterar senha de Gerenciador')
                print('[2] - Alterar senha de Vendedor')
                print('[3] - Alterar código VIP')
                print('[4] - Alterar código promocional')
                print('[5] - Voltar\n')

                password_change = str(input('\nInsira uma opção: '))

                if password_change == '1':
                    manager_password = str(input('\nInsira a nova senha para Gerenciador: '))
                    print('\n===== Senha alterada! =====')
                    breakpoint

                elif password_change == '2':
                    vendor_password = str(input('\nInsira a nova senha para Vendedor: '))
                    print('\n===== Senha alterada! =====')
                    breakpoint

                elif password_change == '3':
                    vip_password = str(input('\nInsira o novo código para ingressos VIP: '))
                    print('\n===== Código alterado! =====')
                    breakpoint

                elif password_change == '4':
                    promotional_password = str(input('\nInsira o novo código para ingressos promocionais: '))
                    print('\n===== Código alterado! =====')
                    breakpoint

                elif password_change == '5':
                     breakpoint

                else:
                     breakpoint

            elif manager_option == '4':
                 breakpoint
            
            else:
                 print('\nOpção inválida!')
                 breakpoint
            
            

        else:
            print('\nA senha está incorreta!')
            breakpoint

    elif option == '2' and num_disponible_tickets > 0: 

        vendor_password_confirm = str(input('\nInsira a senha para continuar: '))

        while num_disponible_tickets != 0:
            if vendor_password_confirm == vendor_password:
                
                print('\n===== TIPO DE COMISSÃO =====')
                print('\n[1] - Comissão Biologia')
                print('[2] - Comissão Enfermagem')
                print('[3] - Voltar\n')

                option_vendor_type = str(input('Insira uma das opções: '))

                if option_vendor_type == '1':

                    print('\n===== TIPO DE INGRESSO =====\n')

                    print(f'[1] - Ingresso Inteira - R${price_tickets_full:.2f}')
                    print(f'[2] - Ingresso Estudante - R${price_tickets_half:.2f}')
                    print(f'[3] - Ingresso Idoso - R${price_tickets_half:.2f}')
                    print(f'[4] - Ingresso Promocional - R${price_tickets_with_discount:.2f}')
                    print('[5] - Ingresso VIP')
                    print('[6] - Voltar a tela anterior\n')

                    option_vendor_ticket_type = str(input('Selecione o tipo de ingresso: '))
            
                    if option_vendor_ticket_type == '1':
                        
                        print('\nIngresso Inteira selecionado. Para continuar confirme os dados solicitados!')
                        age = int(input('\nInsira a idade do comprador: '))

                        if age < 16:
                             print('\nCompra não autorizada. Idade mínima de 16 anos.')
                             breakpoint

                        else:     
                            print('\nIngresso adquirido!')
                            total_age += age
                            num_disponible_tickets -= 1
                            num_tickets_full += 1
                            num_tickets_sold_by_1 += 1
                            break

                    elif option_vendor_ticket_type == '2':

                        print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')
                        age = int(input('\nInsira a idade do comprador: '))
                        doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

                        if age < 16 or len(doc) < 9 or len(doc) > 9:
                                print('\nCompra não autorizada! A idade mínima permitida é de 16 anos ou seu documento estava incorreto.')
                                breakpoint

                        else:
                            print('\nIngresso adquirido!')
                            total_age += age
                            num_disponible_tickets -= 1
                            num_tickets_half_student += 1
                            num_tickets_sold_by_1 += 1
                            break  

                    elif option_vendor_ticket_type == '3':
                            print('\n===== Ingresso Idoso selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                            
                            if age >= 60:
                                print('Ingresso adquirido!')
                                total_age += age
                                num_disponible_tickets -= 1
                                num_tickets_half_old += 1
                                num_tickets_sold_by_1 += 1
                                break

                            else:
                                    print('\nA idade mínima para este tipo de ingresso é de 60 anos.')
                                    breakpoint

                    elif option_vendor_ticket_type == '4':
                            print('\n===== Ingresso Promocional selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                                breakpoint

                            if age < 16:
                                 print('\nA idade minima é de 16 anos.')
                            promotional_password_confirm = str(input('Insira o código promocional: '))

                            if promotional_password_confirm == promotional_password:
                                print('Ingresso adquirido!')
                                total_age += age
                                num_disponible_tickets -= 1
                                num_promotional_tickets += 1
                                num_tickets_sold_by_1 += 1
                                break
                            
                            else:
                                 print('\nCódigo inválido.')
                                 breakpoint

                    elif option_vendor_ticket_type == '5':
                            print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                                breakpoint

                            vip_password_confirm = str(input('\nInsira o código VIP: '))

                            if vip_password_confirm == vip_password:
                                 print('\nIngresso adquirido!')
                                 total_age += age
                                 num_disponible_tickets -= 1
                                 num_tickets_vip += 1
                                 num_tickets_sold_by_1 += 1

                    elif option_vendor_ticket_type == '6':
                        breakpoint

                elif option_vendor_type == '2':

                    print('\n===== TIPO DE INGRESSO =====\n')

                    print(f'[1] - Ingresso Inteira - R${price_tickets_full:.2f}')
                    print(f'[2] - Ingresso Estudante - R${price_tickets_half:.2f}')
                    print(f'[3] - Ingresso Idoso - R${price_tickets_half:.2f}')
                    print(f'[4] - Ingresso Promocional - R${price_tickets_with_discount:.2f}')
                    print('[5] - Ingresso VIP')
                    print('[6] - Voltar a tela anterior\n')

                    option_vendor_ticket_type = str(input('Selecione o tipo de ingresso: '))
            
                    if option_vendor_ticket_type == '1':
                        
                        print('\nIngresso Inteira selecionado. Para continuar confirme os dados solicitados!')

                        try:
                            age = int(input('\nInsira a idade do comprador: '))
                
                        except ValueError:
                            print('\nInsira apenas números!\n')

                        if age < 16:
                             print('Compra não autorizada. Idade mínima de 16 anos.')
                             breakpoint

                        else:     
                            print('\nIngresso adquirido!')
                            total_age += age
                            num_disponible_tickets -= 1
                            num_tickets_full += 1
                            num_tickets_sold_by_2 += 1
                            break

                    elif option_vendor_ticket_type == '2':

                        print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')

                        try:
                            age = int(input('\nInsira a idade do comprador: '))
                
                        except ValueError:
                            print('\nInsira apenas números!\n')
                            breakpoint

                        doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

                        if age < 16 or len(doc) < 9 or len(doc) > 9:
                                print('\nCompra não autorizada! A idade mínima permitida é de 16 anos ou seu documento estava incorreto.')
                                breakpoint

                        else:
                            print('\nIngresso adquirido!')
                            total_age += age
                            num_disponible_tickets -= 1
                            num_tickets_half_student += 1
                            num_tickets_sold_by_2 += 1
                            break  

                    elif option_vendor_ticket_type == '3':
                            print('\n===== Ingresso Idoso selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                            
                            if age >= 60:
                                print('\nIngresso adquirido!')
                                total_age += age
                                num_disponible_tickets -= 1
                                num_tickets_half_old += 1
                                num_tickets_sold_by_2 += 1
                                break

                            else:
                                    print('\nA idade mínima para este tipo de ingresso é de 60 anos.')
                                    breakpoint

                    elif option_vendor_ticket_type == '4':
                            print('\n===== Ingresso Promocional selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')

                            promotional_password_confirm = str(input('Insira o código promocional: '))

                            if age < 16:
                                 print('\nA idade mínima é de 16 anos.')

                            if promotional_password_confirm == promotional_password:
                                print('\nIngresso adquirido!')
                                total_age += age
                                num_disponible_tickets -= 1
                                num_promotional_tickets += 1
                                num_tickets_sold_by_2 += 1
                                breakpoint
                            
                            else:
                                 print('\nCódigo inválido.')
                                 breakpoint

                    elif option_vendor_ticket_type == '5':
                            print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')

                            vip_password_confirm = str(input('\nInsira o código VIP: '))

                            if vip_password_confirm == vip_password:
                                 print('\nIngresso adquirido!\n')
                                 total_age += age
                                 num_disponible_tickets -= 1
                                 num_tickets_vip += 1
                                 num_tickets_sold_by_2 += 1
                                 breakpoint
                            
                            else:
                                print('\nCódigo inválido!')
                                break

                    elif option_vendor_ticket_type == '6':
                        breakpoint

                elif option_vendor_type == '3':
                    break

                else:
                    print('\nOpção inválida!')
                    break

            else:
                print('\nA senha está incorreta!')
                break

    elif option == '3' and num_disponible_tickets > 0:

        print('\n===== TIPO DE INGRESSO =====\n')

        print(f'[1] - Ingresso Inteira - R${price_tickets_full:.2f}')
        print(f'[2] - Ingresso Estudante - R${price_tickets_half:.2f}')
        print(f'[3] - Ingresso Idoso - R${price_tickets_half:.2f}')
        print(f'[4] - Ingresso Promocional - R${price_tickets_with_discount:.2f}')
        print('[5] - Ingresso VIP')
        print('[6] - Voltar a tela anterior\n')

        option_buyer_ticket_type = str(input('Selecione o tipo de ingresso: '))

        if option_buyer_ticket_type == '1':
            
            print('\nIngresso Inteira selecionado. Para continuar confirme os dados solicitados!')

            try:
                age = int(input('\nInsira a idade do comprador: '))
                
            except ValueError:
                print('\nInsira apenas números!\n')

            if age < 16:
                    print('===== Compra não autorizada! Idade mínima de 16 anos ou valor inserido inválido. =====')
                    breakpoint

            else:     
                print('\n===== Ingresso adquirido! =====')
                total_age += age
                num_disponible_tickets -= 1
                num_tickets_full += 1
                breakpoint

        elif option_buyer_ticket_type == '2':

            print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')
            age = int(input('\nInsira a idade do comprador: '))
            doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

            if age < 16 or len(doc) < 9 or len(doc) > 9:
                    print('\nCompra não autorizada! A idade mínima permitida é de 16 anos ou seu documento estava incorreto.')
                    breakpoint

            else:
                print('\n===== Ingresso adquirido! =====')
                total_age += age
                num_disponible_tickets -= 1
                num_tickets_half_student += 1
                breakpoint

        elif option_buyer_ticket_type == '3':
                print('\n===== Ingresso Idoso selecionado. Para continuar confirme os dados solicitados! =====')

                try:
                    age = int(input('\nInsira a idade do comprador: '))
                
                except ValueError:
                    print('\nInsira apenas números!\n')
                
                if age >= 60:
                    print('\n===== Ingresso adquirido! =====')
                    total_age += age
                    num_disponible_tickets -= 1
                    num_tickets_half_old += 1
                    breakpoint

                else:
                        print('\n===== A idade mínima para este tipo de ingresso é de 60 anos ou o valor inserido é inválido. =====')
                        breakpoint

        elif option_buyer_ticket_type == '4':
                print('\n===== Ingresso Promocional selecionado. Para continuar confirme os dados solicitados! =====')

                try:
                    age = int(input('\nInsira a idade do comprador: '))
                
                except ValueError:
                    print('\nInsira apenas números!\n')

                promotional_password_confirm = str(input('Insira o código promocional: '))

                if promotional_password_confirm == promotional_password and age >= 16:
                    print('\n===== Ingresso adquirido! =====')
                    total_age += age
                    num_disponible_tickets -= 1
                    num_promotional_tickets += 1
                    breakpoint
                
                else:
                        print('\n===== Código inválido. Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                        breakpoint

        elif option_buyer_ticket_type == '5':
                print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                try:
                    age = int(input('\nInsira a idade do comprador: '))
                
                except ValueError:
                    print('\nInsira apenas números!\n')

                vip_password_confirm = str(input('\nInsira o código VIP: '))

                if vip_password_confirm == vip_password and age >= 16:
                        print('\n===== Ingresso adquirido! =====')
                        total_age += age
                        num_disponible_tickets -= 1
                        num_tickets_vip += 1
                        breakpoint


        elif option_buyer_ticket_type == '6':
            breakpoint

    elif option == '4':
         print('\n--- Sistema desligado! ---')
         break

    else:
        print('\n--- A opção selecionada não existe ou os ingressos estão esgotados. ---')
        breakpoint