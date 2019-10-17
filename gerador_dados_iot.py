# -*- coding: UTF-8 -*-
'''
Created on 16 de outubro de 2019

@author: luizfritsch
'''
from random import randint
import timeit
import os
import sys

def gera_dados(tamanho_dataset):
    temperaturas = gerar_dados_temperatura(tamanho_dataset)    
    latitudes = gerar_dados_posicionais(tamanho_dataset)

def gerar_dados_temperatura(tamanho_dataset):
    tamanho = 0
    temperaturas = []
    while (tamanho <= tamanho_dataset):
        tamanho = sys.getsizeof(temperaturas) 
        temperaturas.append(randint(0, 99))
    print (temperaturas)
    escreve_dataset_arquivo(temperaturas,"temperatura_escalar",tamanho_dataset)
    return temperaturas

def gerar_dados_posicionais(tamanho_dataset):
    tamanho = 0
    latitudes = []
    while (tamanho <= tamanho_dataset):
        tamanho = sys.getsizeof(latitudes) 
        latitudes.append( str(randint(1, 100)) + '° ' + str(randint(1, 100))+'´N')
    print (latitudes)
    escreve_dataset_arquivo(latitudes,"latitude",tamanho_dataset)
    return latitudes

def gerar_dado_multimidia(tamanho_dataset):


def escreve_dataset_arquivo(dataset,tipo,tamanho_dataset):
    try:
        f = open(tipo+"_"+str(tamanho_dataset)+"kb.txt","w+")
        for dado in dataset:
            f.write("%s\n" % dado)
    except Exception as e:
        print("Erro ao escrever dados de um dataset em um arquivo:"+e)
    finally:
        f.close()
gera_dados(1024)