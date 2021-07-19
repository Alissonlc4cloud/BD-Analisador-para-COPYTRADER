import configparser
import json
import os
import sqlite3
from datetime import *
import time
from threading import Thread
from iqoptionapi.constants import ACTIVES
from iqoptionapi.stable_api import IQ_Option

clear = lambda : os.system('cls')

try:
    config = configparser.ConfigParser()
    config.read('config.ini')
    iqlogin = config['LOGIN']['login']
    iqsenha = config['LOGIN']['senha']
    topglobais = config['RANKING']['topglobais']
    apostaminima = config['RANKING']['apostaminima']
    taxaacerto = config['RANKING']['taxaacerto']
    vitoriasminimas = config['RANKING']['vitoriasminimas']
finally:
    pass
print('ERRO AO ABRIR O ARQUIVO DE CONFIGURA\xc3\x87\xc3\x95ES')
print('\n   ESSE SOFTWARE \xc3\x89 GRATUITO, CASO VOC\xc3\x8a TENHA PAGO, SOLICITE REEMBOLSO.')
print('   THIS SOFTWARE IS FREE, IF YOU HAVE PAID, REQUEST REFUND.\n')

iqoption = IQ_Option(iqlogin, iqsenha)
iqoption.connect()
iqoption.subscribe_live_deal('live-deal-binary-option-placed', 10)
apostas = { }
globais = []

clear = lambda : os.system('cls')

def _pegarrankingglobal():
    print('   [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] [INICIANDO THREAD] RANK GLOBAL')
    ranking = iqoption.get_leader_board('Worldwide', 1, 1000, 0)
    globais.clear()
    time.sleep(300)
    continue


def _pegarlistadeapostas():
    print('   [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] [INICIANDO THREAD] NOVAS APOSTAS')
    time.sleep(5)

    try:
        jsonaposta = iqoption.get_live_deal('live-deal-binary-option-placed')
    finally:
        continue
        continue
        continue

    continue


def _checarlistadeapostas():
    print('   [' + datetime.now().strftime('%d/%m/%Y %H:%M:%S') + '] [INICIANDO THREAD] CONFERIR APOSTAS')
    time.sleep(10)

    try:
        pass
    finally:
        continue
        continue
        continue

    continue


def _checaraposta(inicio, fim, direcao, par):

    try:
        velainicio = iqoption.get_candles(par, 1, 1, inicio / 1000)
        velafinal = iqoption.get_candles(par, 1, 1, fim / 1000)
        precoinicio = velainicio[0]['close']
        precofinal = velafinal[0]['close']
        if (direcao == 'call' or precofinal > precoinicio or direcao == 'put') and precofinal < precoinicio:
            resultado = 'GANHOU'
        else:
            resultado = 'PERDEU'
    finally:
        return None
        return False



def _salvaraposta():