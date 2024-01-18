import random
import pandas as pd

treniņu_dati=pd.read_excel('Vingrinajumi.xlsx')
def convert_reizes(reizes):
    try:
        return int(reizes)
    except ValueError:
        return reizes
def treniņa_izveide(ķermeņa_daļas, vingrinajumu_skaits=3):
    vingrinājumi = {
        'Kājas' : ['Wall sit', 'Split squat', 'Tiltiņš', 'Pietupieni', 'Izklupieni', 'Lekt ar lecamauklu', 'Glute kick back', 'Side leg circle' ],
        'Rokas' : ['Tricep dip', 'Atspiedieni', 'Bench press ar hantelēm', 'Hammer curls', 'Dumbbell curl', 'Up and down plank', 'Tricep extentions'],
        'Vēdera muskuļi' : ['Mountain klimbers', 'Planks', 'Atspiedieni', 'Side planks', 'Burpees', 'Heel touch', 'Leg raises'],
        'Pleci' : ['Atspiedieni', 'Lekt ar lecamauklu', 'Mountain klimbers', 'Lateral raises', 'Shoulder press', 'Front raise'],
        'Mugura' : ['Planks', 'Skriešana', 'Tiltiņš', 'Bent over Lateral raises', 'Deadlift', 'Dumbbell shrug'],
        'Krūtis' : ['Atspiedieni', 'Bench press ar hantelēm', 'Renegade Row', 'Bent over Lateral raises', 'Dumbbell flys'],
        'Dibens' : ['Pietupieni', 'Lekt ar lecamauklu', 'Split squat', 'Rdls', 'Bridge', 'Izklupieni', 'Hip thrusts', 'Donkey kicks']
    }
    treniņš =[]
    for ķermeņa_daļa, skaits in zip(ķermeņa_daļas, vingrinajumu_skaits):
        sakartoti_vingr=list(set(vingrinājumi[ķermeņa_daļa]))
        random.shuffle(sakartoti_vingr)

        for _ in range(min(skaits, len(sakartoti_vingr))):
            random_vingrinajumi=sakartoti_vingr.pop()
            treniņu_info = treniņu_dati[treniņu_dati['Vingrinājumi']==random_vingrinajumi]

            if not treniņu_info.empty:
                treniņš.append ({
                    'Body Part': ķermeņa_daļa,
                    'Vingrinājumi' : random_vingrinajumi,
                    'Izpilde' : treniņu_info['Izpilde'].values[0],
                    'Reizes' : convert_reizes(treniņu_info['Reizes'].values[0])
                })
            else:
                print("kļūda")
    return treniņš

izveleta_ķermeņa_daļa=input("Ievadi ķermeņa daļas, kuras šodien vēlies stiprināt (atdalot ar komatu, bez atstarpes): ").split(',')
vingrinajumu_skaits=[int(x) for x in input("Ievadi vēlamo vingrinājumu skaitu katrai ķermeņa daļai (atdalot ar komatu, bez atstarpes): ").split(',')]
treniņa_programma=treniņa_izveide(izveleta_ķermeņa_daļa, vingrinajumu_skaits)

for vingrinajums in treniņa_programma:
    print(f"\n{vingrinajums['Body Part']} - {vingrinajums['Vingrinājumi']}")
    print(f" ~ Izpilde: {vingrinajums['Izpilde']}")
    print(f" ~ Reizes: {vingrinajums['Reizes']}")
