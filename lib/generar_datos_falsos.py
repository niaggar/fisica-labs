# Genera los datos falsos
def generar_datos_falsos(y, sigma_y):
    y_falso = np.random.normal(y, sigma_y)
    return y_falso

def obtener_dato_temperatura_real(tiempo_falso):
    for i in range(len(tiempo)):
        if tiempo[i] > tiempo_falso:
            return (temperatura[i] + temperatura[i - 1]) / 2
    

tiempo_maximo = np.max(tiempo)
t_de_medicion_inicial = 2 * 60 # 5 minutos
t_de_medicion = 6 * 60 # 10 minutos

numero_de_datos_falsos = tiempo_maximo 

# datos falsos para los primeros 25 minutos
dt = 2 * 60 # 1 minuto
tiempo_falso_25 = np.zeros(13)
temperatura_falso_25 = np.zeros(13)

for i in range(13):
    tiempo_falso_25[i] = i * dt

    temperatura_real = obtener_dato_temperatura_real(tiempo_falso_25[i])
    temperatura_falso_25[i] = int(generar_datos_falsos(temperatura_real, 0.2))


# datos para los 60 minutos restantes
dt = 4 * 60 # 1 minuto
tiempo_falso_60 = np.zeros(15)
temperatura_falso_60 = np.zeros(15)

for i in range(15):
    tiempo_falso_60[i] = i * dt + tiempo_falso_25[-1]

    temperatura_real = obtener_dato_temperatura_real(tiempo_falso_60[i])
    temperatura_falso_60[i] = int(generar_datos_falsos(temperatura_real, 0.2))


temperatura_falso = np.concatenate((temperatura_falso_25, temperatura_falso_60))
tiempo_falso = np.concatenate((tiempo_falso_25, tiempo_falso_60))

# Grafica los datos falsos
fig = plt.figure()
fig.set_figheight(10)
fig.set_figwidth(10)

plt.plot(tiempo_falso, temperatura_falso , '-o', color = 'black',  label='Datos manuales')
plt.plot(tiempo, temperatura, color = 'green')
plt.xlabel("Tiempo (s)", fontdict = font2)
plt.ylabel("ln[Temperatura] (ln[C°])", fontdict = font2)

legend = plt.legend(loc='upper right')
for text in legend.texts:
    text.set_fontsize(font3['size'])
    text.set_family(font3['family'])

plt.show()


# Guarda los datos en un archivo .csv
datos_falsos = pd.DataFrame({'Tiempo': tiempo_falso, 'Temperatura': temperatura_falso})
datos_falsos.to_csv('datos_manuales.csv', index=False)