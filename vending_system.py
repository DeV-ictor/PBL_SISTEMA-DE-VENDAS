#Autor: Adson Victor de Souza Alves
#Componente Curricular: Algoritmos e Programação I
#Concluido em: 18/04/2024

#Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
#trecho de código de outro colega ou de outro autor, tais como provindos de livros e
#apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
#de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
#do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

#CONFIGURAÇÃO INICIAL DO SISTEMA E INICIALIZAÇÃO DAS VARIÁVEIS

#Disponibilização de ingressos
num_total_tickets = 2000
num_tickets_vip = 0

#Precificação
price_tickets_with_discount = 10.00           
price_tickets_full = 30.00
price_tickets_half = price_tickets_full / 2

#Tipos de ingressos
num_tickets_full = 0
num_tickets_half_student = 0
num_tickets_half_old = 0
num_promotional_tickets = 0

total_num_tickets_half = num_tickets_half_student + num_tickets_half_old

total_age = 0

#Vendedores comissionados

num_tickets_sold_by_1 = 0
num_tickets_sold_by_2 = 0
num_tickets_sold_by_3 = 0

num_tickets_courtesy_1 = 0
num_tickets_courtesy_2 = 0
num_tickets_courtesy_3 = 0

#INICIALIZAÇÃO DAS SENHAS

manager_password = 'y'
vendor_password = 'x'
vip_password = 'vip@pass2024'
promotional_password = 'ecomp20241'

#Variáveis de inicialização

option = '0'
age = 0
minimun_age = 16
sold_tickets = 0

#Variáveis de resultados

collection_full = 0
collection_half_old = 0
collection_half_student = 0
collection_promotional = 0

#INICIALIZAÇÃO DO SISTEMA

print('Sistema iniciando...\n')

while option != '4':

    num_disponible_tickets = num_total_tickets - (sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3)

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
            
                try:
                    num_total_tickets = int(input('\nDefina a quantidade de ingressos totais: '))

                    num_tickets_reserved = int(input('\nDefina a quantidade de ingressos reservados: '))

                    price_tickets_with_discount = float(input('\nDigite o preço dos ingressos promocionais: '))
                    
                    price_tickets_full = float(input('\nDigite o valor dos ingressos na modalidade Inteira: '))

                    minimun_age = int(input('\nDefina a idade mínima do evento: '))

                except ValueError:
                    print('\nValores inseridos incorretos!')
                    breakpoint

                price_tickets_half = price_tickets_full / 2

            elif manager_option == '2':

                #ATUALIZAÇÃO DOS DADOS

                #Ingressos emitidos e não emitidos

                num_disponible_tickets = num_total_tickets - (sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3)
                unsold_tickets = num_disponible_tickets

                num_tickets_courtesy_1 = num_tickets_sold_by_1 // 10 #Cortesias para Tipo 1 (Biologia)
                num_tickets_courtesy_2 = num_tickets_sold_by_2 // 10 #Cortesias para Tipo 2 (Enfermagem)
                num_tickets_courtesy_3 = num_tickets_sold_by_3 // 10 #Cortesias para Tipo 3 (não definido)

                #Arrecadação por tipo de ingressos

                collection_full = price_tickets_full * num_tickets_full
                collection_half_student = price_tickets_half * num_tickets_half_student
                collection_half_old = price_tickets_half * num_tickets_half_old
                collection_promotional = price_tickets_with_discount * num_promotional_tickets

                #Tipo de ingresso mais vendido

                most_sold_ticket = max(num_tickets_full, num_tickets_half_student, num_tickets_half_old, num_promotional_tickets, num_tickets_vip)
                
                print(f'\n[Ingressos totais - {sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3 + unsold_tickets}]')
                print(f'[Ingressos emitidos - {sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3}]')
                print(f'[Ingressos não emitidos - {unsold_tickets}]\n')

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

                if most_sold_ticket == 0:
                    print('Nenhum ingresso foi vendido até o momento.')
                elif num_tickets_full == most_sold_ticket:
                    print(f'O ingresso Inteira foi o mais vendido, com {most_sold_ticket} vendas!\n')
                elif num_tickets_half_student == most_sold_ticket:
                    print(f'O ingresso Estudante foi o mais vendido, com {most_sold_ticket} vendas!\n')
                elif num_tickets_half_old == most_sold_ticket:
                    print(f'O ingresso Idoso foi o mais vendido, com {most_sold_ticket} vendas!\n')
                elif num_tickets_vip == most_sold_ticket:
                    print(f'O ingresso VIP foi o mais vendido, com {most_sold_ticket} vendas!\n')
                elif num_promotional_tickets == most_sold_ticket:
                    print(f'O ingresso Promocional foi o mais vendido, com {most_sold_ticket} vendas!\n')

                if sold_tickets > 0:

                    print(f'\n[Idade média do evento] - {total_age / sold_tickets}\n')

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

        while num_disponible_tickets > 0:

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

                        try:
                            age = int(input('\nInsira a idade do comprador: '))
                
                        except ValueError:
                            print('\nInsira apenas números!\n')

                        if age < minimun_age:
                            print(f'\nCompra não autorizada. Idade mínima de {minimun_age} anos ou o valor inserido é inválido.')
                            breakpoint

                        else:     
                            print('\nIngresso adquirido!')
                            total_age += age
                            sold_tickets += 1
                            num_tickets_full += 1
                            num_tickets_sold_by_1 += 1
                            breakpoint

                    elif option_vendor_ticket_type == '2':

                        print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')

                        try:
                            age = int(input('\nInsira a idade do comprador: '))
                
                        except ValueError:
                            print('\nInsira apenas números!\n')

                        doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

                        if age < minimun_age or len(doc) < 9 or len(doc) > 9 or doc.isnumeric() == False:
                            print(f'\nCompra não autorizada! A idade mínima permitida é de {minimun_age} anos, seu documento estava incorreto ou os dados inseridos são inválidos.')
                            breakpoint

                        else:
                            print('\nIngresso adquirido!')
                            total_age += age
                            sold_tickets += 1
                            num_tickets_half_student += 1
                            num_tickets_sold_by_1 += 1
                            breakpoint

                    elif option_vendor_ticket_type == '3':
                            print('\n===== Ingresso Idoso selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                            
                            if age >= 60:
                                print('Ingresso adquirido!')
                                total_age += age
                                sold_tickets += 1
                                num_tickets_half_old += 1
                                num_tickets_sold_by_1 += 1
                                breakpoint

                            else:
                                print('\nA idade mínima para este tipo de ingresso é de 60 anos.')
                                breakpoint

                    elif option_vendor_ticket_type == '4':
                            print('\n===== Ingresso Promocional selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')

                            if age < minimun_age:
                                print(f'\nA idade minima é de {minimun_age} anos.')
                                breakpoint

                            promotional_password_confirm = str(input('Insira o código promocional: '))

                            if promotional_password_confirm == promotional_password and age >= minimun_age:
                                print('Ingresso adquirido!')
                                total_age += age
                                sold_tickets += 1
                                num_promotional_tickets += 1
                                num_tickets_sold_by_1 += 1
                                breakpoint
                            
                            else:
                                print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                                breakpoint

                    elif option_vendor_ticket_type == '5':
                            print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                                breakpoint

                            if age < minimun_age:
                                print(f'\nCompra não autorizada. Idade mínima de {minimun_age} anos ou o valor inserido é inválido.')
                                breakpoint
                            
                            vip_password_confirm = str(input('\nInsira o código VIP: '))

                            if vip_password_confirm == vip_password and age >= minimun_age:
                                print('\nIngresso adquirido!')
                                total_age += age
                                sold_tickets += 1
                                num_tickets_vip += 1
                                num_tickets_sold_by_1 += 1

                            else:
                                print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                                breakpoint

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

                        if age < minimun_age:
                            print(f'\nCompra não autorizada. Idade mínima de {minimun_age} anos ou o valor inserido é inválido.')
                            breakpoint

                        else:     
                            print('\nIngresso adquirido!')
                            total_age += age
                            sold_tickets += 1
                            num_tickets_full += 1
                            num_tickets_sold_by_2 += 1
                            breakpoint

                    elif option_vendor_ticket_type == '2':

                        print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')

                        try:
                            age = int(input('\nInsira a idade do comprador: '))
                
                        except ValueError:
                            print('\nInsira apenas números!\n')

                        doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

                        if age < minimun_age or len(doc) < 9 or len(doc) > 9 or doc.isnumeric() == False:
                            print(f'\nCompra não autorizada! A idade mínima permitida é de {minimun_age} anos, seu documento estava incorreto ou os dados inseridos são inválidos.')
                            breakpoint

                        else:
                            print('\nIngresso adquirido!')
                            total_age += age
                            sold_tickets += 1
                            num_tickets_half_student += 1
                            num_tickets_sold_by_2 += 1
                            breakpoint

                    elif option_vendor_ticket_type == '3':
                            print('\n===== Ingresso Idoso selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')
                            
                            if age >= 60:
                                print('\nIngresso adquirido!')
                                total_age += age
                                sold_tickets += 1
                                num_tickets_half_old += 1
                                num_tickets_sold_by_2 += 1
                                breakpoint

                            else:
                                print('\nA idade mínima para este tipo de ingresso é de 60 anos.')
                                breakpoint

                    elif option_vendor_ticket_type == '4':
                            print('\n===== Ingresso Promocional selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')

                            if age < minimun_age:
                                print(f'\nA idade mínima é de {minimun_age} anos.')
                                breakpoint

                            promotional_password_confirm = str(input('Insira o código promocional: '))

                            if promotional_password_confirm == promotional_password and age >= minimun_age:
                                print('\nIngresso adquirido!')
                                total_age += age
                                sold_tickets += 1
                                num_promotional_tickets += 1
                                num_tickets_sold_by_2 += 1
                                breakpoint
                            
                            else:
                                print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                                breakpoint

                    elif option_vendor_ticket_type == '5':
                            print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                            try:
                                age = int(input('\nInsira a idade do comprador: '))
                
                            except ValueError:
                                print('\nInsira apenas números!\n')

                            if age < minimun_age:
                                print(f'\nA idade mínima é de {minimun_age} anos.')
                                breakpoint

                            vip_password_confirm = str(input('\nInsira o código VIP: '))

                            if vip_password_confirm == vip_password and age >= minimun_age:
                                print('\nIngresso adquirido!\n')
                                total_age += age
                                sold_tickets += 1
                                num_tickets_vip += 1
                                num_tickets_sold_by_2 += 1
                                breakpoint
                            
                            else:
                                print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                                breakpoint 

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

            if age < minimun_age:
                print(f'\n===== Compra não autorizada! Idade mínima de {minimun_age} anos ou valor inserido inválido. =====')
                breakpoint

            else:     
                print('\n===== Ingresso adquirido! =====')
                total_age += age
                sold_tickets += 1
                num_tickets_full += 1
                breakpoint

        elif option_buyer_ticket_type == '2':

            print('\n===== Ingresso Estudante selecionado. Para continuar confirme os dados solicitados! =====')

            try:
                age = int(input('\nInsira a idade do comprador: '))
                
            except ValueError:
                print('\nInsira apenas números!\n')

            doc = str(input('\nInsira o número do cartão de estudante (09 dígitos e sem caracteres): '))

            if age < minimun_age or len(doc) < 9 or len(doc) > 9 or doc.isnumeric() == False:
                print(f'\nCompra não autorizada! A idade mínima permitida é de {minimun_age} anos, seu documento estava incorreto ou os dados informados são inválidos.')
                breakpoint

            else:
                print('\n===== Ingresso adquirido! =====')
                total_age += age
                sold_tickets += 1
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
                    sold_tickets += 1
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

                if age < minimun_age:
                    print(f'\nA idade mínima é de {minimun_age} anos.')
                    breakpoint

                promotional_password_confirm = str(input('Insira o código promocional: '))

                if promotional_password_confirm == promotional_password and age >= minimun_age:
                    print('\nIngresso adquirido!')
                    total_age += age
                    sold_tickets += 1
                    num_promotional_tickets += 1
                    num_tickets_sold_by_2 += 1
                    breakpoint
                
                else:
                    print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                    breakpoint

        elif option_buyer_ticket_type == '5':
                print('\n===== Ingresso VIP selecionado. Para continuar confirme os dados solicitados! =====')

                try:
                    age = int(input('\nInsira a idade do comprador: '))
                
                except ValueError:
                    print('\nInsira apenas números!\n')

                if age < minimun_age:
                    print(f'\nA idade mínima é de {minimun_age} anos.')
                    breakpoint

                vip_password_confirm = str(input('\nInsira o código VIP: '))

                if vip_password_confirm == vip_password and age >= minimun_age:
                    print('\n===== Ingresso adquirido! =====')
                    total_age += age
                    sold_tickets += 1
                    num_tickets_vip += 1
                    breakpoint

                else:
                    print('\n===== Você não possui idade mínima, a idade inserida é inválida ou o código está expirado! =====')
                    breakpoint

                
        elif option_buyer_ticket_type == '6':
            breakpoint
        
    elif option == '4':
        pass

    else:
        print('\n--- A opção selecionada não existe ou os ingressos estão esgotados. ---')
        breakpoint

print('\nSistema encerrado. Gerando resultados...\n')

#ATUALIZAÇÃO DOS DADOS

#Ingressos emitidos e não emitidos

num_disponible_tickets = num_total_tickets - (sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3)
unsold_tickets = num_disponible_tickets

num_tickets_courtesy_1 = num_tickets_sold_by_1 // 10 #Cortesias para Tipo 1 (Biologia)
num_tickets_courtesy_2 = num_tickets_sold_by_2 // 10 #Cortesias para Tipo 2 (Enfermagem)
num_tickets_courtesy_3 = num_tickets_sold_by_3 // 10 #Cortesias para Tipo 3 (não definido)

#Arrecadação por tipo de ingressos

collection_full = price_tickets_full * num_tickets_full
collection_half_student = price_tickets_half * num_tickets_half_student
collection_half_old = price_tickets_half * num_tickets_half_old
collection_promotional = price_tickets_with_discount * num_promotional_tickets

#Tipo de ingresso mais vendido

most_sold_ticket = max(num_tickets_full, num_tickets_half_student, num_tickets_half_old, num_promotional_tickets, num_tickets_vip)

print(f'\n[Ingressos totais - {sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3 + unsold_tickets}]')
print(f'[Ingressos emitidos - {sold_tickets + num_tickets_courtesy_1 + num_tickets_courtesy_2 + num_tickets_courtesy_3}]')
print(f'[Ingressos não emitidos - {unsold_tickets}]\n')

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

if most_sold_ticket == 0:
    print('Nenhum ingresso foi vendido até o momento.')
elif num_tickets_full == most_sold_ticket:
    print(f'O ingresso Inteira foi o mais vendido, com {most_sold_ticket} vendas!\n')
elif num_tickets_half_student == most_sold_ticket:
    print(f'O ingresso Estudante foi o mais vendido, com {most_sold_ticket} vendas!\n')
elif num_tickets_half_old == most_sold_ticket:
    print(f'O ingresso Idoso foi o mais vendido, com {most_sold_ticket} vendas!\n')
elif num_tickets_vip == most_sold_ticket:
    print(f'O ingresso VIP foi o mais vendido, com {most_sold_ticket} vendas!\n')
elif num_promotional_tickets == most_sold_ticket:
    print(f'O ingresso Promocional foi o mais vendido, com {most_sold_ticket} vendas!\n')

if sold_tickets > 0:

    print(f'\n[Idade média do evento] - {total_age / sold_tickets}\n')

else:
    print('\nA média de idade não foi possível de ser calculada.\n')