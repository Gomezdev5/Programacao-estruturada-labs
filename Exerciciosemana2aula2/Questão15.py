ano_epoch = 1970

ano = 2024

quant_anos  = ano - ano_epoch

meses = quant_anos * 12

dias = meses * 3.44

horas = dias * 24

minutos = horas * 60

segundo = minutos * 60

mili_seg = segundo * 1000

print(ano_epoch, ano, quant_anos, meses, dias, horas, minutos, segundo, mili_seg)