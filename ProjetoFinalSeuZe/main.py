import requests
from time import sleep
from loguru import logger
from deep_translator import GoogleTranslator

URL = "https://api.adviceslip.com/advice"

n_conselhos = int(input('Digite a quantidade de conselhos: '))

try:
    for i in range(n_conselhos):
        logger.info(f'Ciclo {i+1} de chamada de API iniciado.')
        result = requests.get(URL)

        logger.success('Chamada de API realizada com sucesso.')

        id = result.json()['slip']['id']
        advice = result.json()['slip']['advice']

        traducao = GoogleTranslator(source='english', target='portuguese').translate(advice)

        print(f'Conselho:{id} {advice} - Tradução: {traducao}.')
        print('Deseja Salvar ou Excluir? \nTecle (S) para salvar ou tecle (X) para excluir.')

        sx_conselho = input('Digite aqui o que deseja: ').upper()



        if sx_conselho == 'S':
            with open('arquivo.txt', 'a', encoding='UTF-8') as arquivo:
                arquivo.write(f'{id} - {advice} - {traducao} \n')
            logger.success('Registro no banco de dados(txt) realizado com sucesso.')
        else:
            logger.info('Conselho Excluido')
        sleep(1)

        print('Gostaria de ver todos os conselhos presente no banco de dados?')
        ver_conselhos = input('Digite (V) para ver e (N) para encerrar o programa: ').upper()

        if ver_conselhos == 'V':
            with open('arquivo.txt', 'r', encoding='UTF-8') as arquivo:
                arquivos_banco = arquivo.read()
            print(arquivos_banco)
            logger.info('Programa Encerrado')

        else:
            logger.info('Programa Encerrado')

        logger.info(f'Fim do ciclo {i + 1}.')
except Exception as e:
    logger.exception(e)