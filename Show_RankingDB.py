import os, configparser, sqlite3, time
from datetime import datetime
conn = sqlite3.connect('ranking.db')
clear = lambda: os.system('cls')
os.system('mode con cols=70 lines=50')
try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    taxaacerto = config['RANKING']['taxaacerto']
    vitoriasminimas = config['RANKING']['vitoriasminimas']
except:
    print('ERRO AO ABRIR O ARQUIVO DE CONFIGURAÇÕES')
else:
    while True:
        c = conn.cursor()
        c.execute('SELECT * FROM ranking WHERE vitorias >= ' + str(vitoriasminimas) + ' AND taxavitorias >= ' + str(taxaacerto) + ' ORDER BY vitorias DESC, taxavitorias DESC LIMIT 45')
        ranking = c.fetchall()
        clear()
        print('\n  [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] RANKING MELHORES TRADES \n')
        print('{:<15s}{:<12s}{:<13s}{:<13s}{:<15s}'.format('  [USUARIO]', '[ID]', '[VITORIAS]', '[DERROTAS]', '[TAXA ACERTO]'))
        for trade in ranking:
            id_usuario = trade[0]
            nome_usuario = trade[1]
            vitorias = trade[2]
            derrotas = trade[3]
            winratio = trade[4]
            print('{:<15s}{:<12s}{:<13s}{:<13s}{:<15s}'.format('  ' + nome_usuario[:10], str(id_usuario), str(vitorias), str(derrotas), str(winratio) + '%'))
        else:
            time.sleep(60)