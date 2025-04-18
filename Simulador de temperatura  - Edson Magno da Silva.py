coeficiente_de_emissao = [['1 - Negro fumo',1]]
coeficiente_de_conducao = [#Metal
['1 - Alumínio seco - massa especifica 2800 kilogramas por metro cubico',204],
['2 - Alumínio molhado - massa especifica 2800 kilogramas por metro cubico',204],
['3 - Cobre seco - massa especifica 9000 kilogramas por metro cubico',372],
['4 - Cobre molhado - massa especifica 9000 kilogramas por metro cubico',372],
['5 - Ligas seco - massa especifica 12250 kilogramas por metro cubico',35],
['6 - Liga molhada - massa especifica 12250 kilogramas por metro cubico',35],
['7 - Aço, ferro seco - massa especifica 7800 kilogramas por metro cubico',52],
['8 - Aço, ferro molhado - massa especifica 7800 kilogramas por metro cubico',52],
['9 - Zinco seco - massa especifica 7200 kilogramas por metro cubico',110],
['10 - Zinco molhado - massa especifica 7200 kilogramas por metro cubico',110],
#Pedra Natural
['11 - Basalto, granito seco- massa especifica 3000 kilogramas por metro cubico',3.5],
['12 - Basalto, granito molhado- massa especifica 3000 kilogramas por metro cubico',3.5],
['13 - Calcario, marmore seco- massa especifica 2700 kilogramas por metro cubico',2.5],
['14 - Calcario, marmore molhado- massa especifica 2700 kilogramas por metro cubico',2.5],
['15 - Arenito seco- massa especifica 2600 kilogramas por metro cubico',1.6],
['16 - Arenito molhado- massa especifica 2600 kilogramas por metro cubico',1.6],
#Alvenaria
['17 - Tijolo seco- massa especifica 1600-1900 kilogramas por metro cubico',0.65],
['18 - Tijolo molhado- massa especifica 1600-1900 kilogramas por metro cubico',1.05],
['19 - Tijolo de Areia Cal seco- massa especifica 1900 kilogramas por metro cubico',0.9],
['20 - Tijolo de Areia Cal molhado- massa especifica 1900 kilogramas por metro cubico',1.4],
['21 - Tijolo de Areia Cal seco- massa especifica 1000-1400 kilogramas por metro cubico',0.6],
#Concreto
['22 - Concreto de cascalho seco - massa especifica 2300-2500 kilogramas por metro cubico',2],
['23 - Concreto de cascalho molhado - massa especifica 2300-2500 kilogramas por metro cubico',2],
['24 - Concreto leve seco - massa especifica 1600-1900 kilogramas por metro cubico',0.8],
['25 - Concreto leve molhado - massa especifica 1600-1900 kilogramas por metro cubico',1.3],
['26 - Concreto leve seco - massa especifica 1000-1300 kilogramas por metro cubico',0.425],
['27 - Concreto leve molhado - massa especifica 1000-1300 kilogramas por metro cubico',0.65],
['28 - Concreto leve seco - massa especifica 300-700 kilogramas por metro cubico',0.175],
['29 - Concreto de pó de polimento seco - massa especifica 1000-1400 kilogramas por metro cubico',0.425],
['30 - Concreto de pó de polimento molhado - massa especifica 1000-1400 kilogramas por metro cubico',0.725],
['31 - Concreto de pó de polimento seco - massa especifica 700-1000 kilogramas por metro cubico',0.29],
['32 - Concreto de isolação seco - massa especifica 300-700 kilogramas por metro cubico',0.175],
['33 - Concreto celular seco - massa especifica 1000-1300 kilogramas por metro cubico',0.425],
['34 - Concreto celular molhado - massa especifica 1000-1300 kilogramas por metro cubico',0.95],
['35 - Concreto celular seco - massa especifica 400-700 kilogramas por metro cubico',0.2],
['36 - Concreto de Escória seco - massa especifica 1600-1900 kilogramas por metro cubico',0.575],
['37 - Concreto de Escória molhado - massa especifica 1600-1900 kilogramas por metro cubico',0.85],
['38 - Concreto de Escória seco - massa especifica 1000-1300 kilogramas por metro cubico',0.265],
['39 - Concreto de Escória molhado - massa especifica 1000-1300 kilogramas por metro cubico',0.425],
#Inorgânico
['40 - Cimento de asbesto seco - massa especifica 1600-1900 kilogramas por metro cubico',0.525],
['41 - Cimento de asbesto molhado - massa especifica 1600-1900 kilogramas por metro cubico',1.05],
['42 - Placa de Gipsita - massa especifica 800-1400',0.34],
['43 - Cartão gipsita - massa especifica 900 kilogramas por metro cubico',0.2],
['44 - Vidro seco - massa especifica 2500 kilogramas por metro cubico',0.8],
['45 - Vidro molhado - massa especifica 2500 kilogramas por metro cubico',0.8],
['46 - Lã de vidro - massa especifica 150 kilogramas por metro cubico',0.04],
['47 - Lã de rocha - massa especifica 35-200 kilogramas por metro cubico',0.04],
['48 - Telhas secas - massa especifica 2000 kilogramas por metro cubico',1.2],
['49 - Telhas molhadas - massa especifica 2000 kilogramas por metro cubico',1.2],
#Emplastros
['50 - Cimento seco - massa especifica 1900 kilogramas por metro cubico',0.9],
['51 - Cimento molhado - massa especifica 1900 kilogramas por metro cubico',1.5]]

V = float(input('Volume da sala em metros cubico'))
armazenagem = []
armazenagememissivein = []
armazenagememissiveout = []
for j in range(100000):
   tempin = float(input('Temperatura interna do comodo: '))
   tempout = float(input('Temperatura face externa ao comodo: '))
   espessura = float(input('espessura da parede: '))
   area = float(input('area da superficie: '))
   for i in range(len(coeficiente_de_conducao)):
     print(coeficiente_de_conducao[i][0])
   
   coef = int(input('numero do material usado: '))
   armazenagem.append(coeficiente_de_conducao[coef - 1][1])
   TrueFalse = input('Há algum material que deja inserir a mais? 0 - Não ou 1 - Sim')
   if (TrueFalse == '0'):
     break
   else:
     continue

#tabela sendo construida

areain = []
for p in range(100000):
   tempin1 = float(input('Temperatura face interna do comodo: '))
   areainterna = float(input('area interna da sala em que estamos medindo a superficie em questão: '))
   areain.append(areainterna)
   #tabela sendo construida
   for v in range(len(coeficiente_de_emissao)):
     print(coeficiente_de_emissao[v][0])
   coef1 = int(input('numero do material usado: '))
   armazenagememissivein.append(coeficiente_de_emissao[coef1 - 1][1])
   TrueFalse1 = input('Há algum material que deseja inserir a mais? 0 - Não ou 1 - Sim')
   if (TrueFalse1 == '0'):
     break
   else:
     continue
areaout = []
for l in range(100000):
   tempout1 = float(input('Temperatura face externa ao comodo: '))
   areaexterna = float(input('area da superficie externa a sala: '))
   areaout.append(areaexterna)
   for c in range(len(coeficiente_de_emissao)):
     print(coeficiente_de_emissao[c][0])
   coef2 = int(input('numero do material usado: '))
   armazenagememissiveout.append(coeficiente_de_emissao[coef2-1][1])
   TrueFalse2 = input('Há algum material que deseja inserir a mais? 0 - Não ou 1 - Sim')
   if (TrueFalse2 == '0'):
     break
   else:
     continue


capterm = 1.29
Q_conduction = 0
Q_emissivity = 0

sigma = 0.0000000567

for d in range(10000000):
  for e in range(len(areain)):
    Q_emissivityin = sigma*armazenagememissivein[e]*(areain[e])*(tempin+273.15)**4
    
  for f in range(len(areaout)):
    Q_emissivityout = sigma*armazenagememissiveout[f]*(areaout[f])*(tempout+273.15)**4 
    
  
  for w in range(len(armazenagem)):
    Q_conduction = ((area*armazenagem[w]*(tempout-tempin))/espessura)*0.0001
    
    
  Q_emissivity = (Q_emissivityin - Q_emissivityout)*0.0001 
  tempin = (Q_conduction + Q_emissivity)/(capterm*1000*V) + tempin
    #print(Q_conduction)
  print(tempin,Q_conduction,Q_emissivity)