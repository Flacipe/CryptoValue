#!/usr/bin/env python3.5
#-*-coding utf-8 -*-

import sys
import requests

try :
	quit = 'off'
	while quit != 'on':
		print('Pour avoir la liste des crypto-monnaies, entrez le mot clé \'list\'')
		print('Sinon, entrez le code de la crypto-monnaie dont vous voules savoir le prix')
		print('Si par hasard un jour vous voulez quitter le script, entrez le mot clé \'quit\'')
		entree = input('Entrez un mot clé ou le code d\'une crypto-monnaie :')
		if entree == 'quit':
			quit = 'on'
		else :
			if entree == 'list':
				response = requests.get('https://www.cryptocompare.com/api/data/coinlist').json()['Data']
				print(list(response.keys()))
			else :
				response = requests.get('https://min-api.cryptocompare.com/data/pricemulti?fsyms='+entree+'&tsyms=USD,EUR').json()
				print (response)
except KeyboardInterrupt:
	print('\n Merci d\'avoir utilisé CryptoValue, à la prochaine')
	sys.exit(0)