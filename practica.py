otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

crudo_promedio = 5
crudo_dalto = 3.5


diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
print(f' el curso de dalto dura un {diferencia_con_min}% menos que el mas rapido')
print(f' el curso de dalto dura un {diferencia_con_max}% menos que el mas lento')
print(f' el curso de dalto dura un {diferencia_con_promedio}% menos que el mas promedio')


tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 -dalto_curso * 1000 // crudo_dalto / 10

print(f"Un curso promedio elimina un {tiempo_vacio_promedio}%")
print(f"Un curso dalto elimino {tiempo_vacio_dalto}%")


print(f"ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 1000 // dalto_curso / 10} horas de este curso")
print(f"ver 10 horas de este curso equivale a ver {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso")
