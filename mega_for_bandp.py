from TimeFrequencyRunIn import  dividir_em_bandas
from source.runInDB_utils import RunIn_File


def gera_data(path_in,n_bandas,f_max,var = "vibrationRAWLateral"):

    # como quer que estruture essa obtenção de dados? tudo em uma lista só? criar novos dicionários?...

    dataset_list = []
    with RunIn_File(path_in) as file:

        for unit in file:
             for test in unit:

                tempo = test.getMeasurements(varName=["time"], tStart = -float("inf"))
                tempo = [var["time"] for var in tempo]

                for momento in range (len(tempo)):
                    
                    dados = test.getMeasurements(varName=[var], indexes = momento)
                    valor = (dividir_em_bandas(f_max,n_bandas,dados)[1])
                    dataset_list.append(valor)

    return(dataset_list)


