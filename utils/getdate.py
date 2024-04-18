import datetime

def getdatesystem():
    actually_date = datetime.datetime.now()
    return actually_date.date()

def parse_data(string):
    meses = {
        'Janeiro': 1,
        'Fevereiro': 2,
        'Março': 3,
        'Abril': 4,
        'Maio': 5,
        'Junho': 6,
        'Julho': 7,
        'Agosto': 8,
        'Setembro': 9,
        'Outubro': 10,
        'Novembro': 11,
        'Dezembro': 12
    }
    data = string.split()
    new_mes = ''
    for chave, valor in meses.items():
        if data[2] == chave:
            new_mes = valor
    
    if len(str(new_mes)) < 2:
        new_mes = f'0{new_mes}'

    new_date = f'{data[4]}-{new_mes}-{data[0]}'

    return new_date

if __name__ == '__main__':
    print(parse_data('18 de Abril de 2024'))
