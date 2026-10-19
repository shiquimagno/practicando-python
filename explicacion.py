nombre_vendedor = input("Nombre del vendedor: ")
meta_semanal = 8000
contador_metas_cumplidas = 0 # contador
total_ventas = 0 # acumulador
comision = 0 # 0 = 0%
bono = 0
pago_total = 0

for semana in range(1,5):
    ventas_semana = float(input(f"Ventas de la semana {semana} (S/.): "))
    total_ventas += ventas_semana 
    if ventas_semana >= meta_semanal: 
        print("   -> Meta semanal cumplida!")
        contador_metas_cumplidas += 1 # metas_cumplidas = metas_cumplidas + 1
    else:
        print(f"   -> Faltaron para la meta S/. {meta_semanal - ventas_semana}") 

if total_ventas <= 20000: # Si
    comision = 2.0
elif total_ventas <= 35000: # Sino Si
    comision = 3.5
else: # Sino, ya qué
    comision = 5.0


if contador_metas_cumplidas == 4:
    bono = 500
elif contador_metas_cumplidas == 3:
    bono = 200
else:
    bono = 0

pago_total = (comision/100)*total_ventas + bono 
promedio_semanal = total_ventas / 4 
# Mostrar
print()
print("====================================")
print("Vendedor\t\t:", nombre_vendedor)
print("Total de ventas\t\t:", total_ventas)
print("Promedio semanal\t:", promedio_semanal)
print("Semanas con meta\t:", contador_metas_cumplidas,"de 4")
print("Tasa de comisión\t:", comision, " %")
print("Comisión\t\t:", (comision/100)*total_ventas)
print("Bono por constancia\t:", bono)
print("Pago total\t\t:", "S/.",pago_total)





