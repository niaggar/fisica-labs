
table_bajada = readtable('bajada.csv');
voltaje_bajada = table_bajada.V;
temperatura_bajada = table_bajada.TK;


filtro = temperatura_bajada > 520;
voltaje_bajada_filtrado = voltaje_bajada(~filtro);
temperatura_bajada_filtrada = temperatura_bajada(~filtro);

ft = fittype( 'power2' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Algorithm = 'Levenberg-Marquardt';
opts.Display = 'Off';
opts.Lower = [-Inf 1 -Inf];
opts.Robust = 'LAR';
opts.StartPoint = [3.32594964201511e-12 4.60644364247517 -0.00460929816404687];

[fit_bajada, fit_bajada_error] = fit(temperatura_bajada_filtrada, voltaje_bajada_filtrado, ft, opts);


% Crear una serie de valores para la temperatura para graficar la curva ajustada
temperatura_para_grafica = linspace(min(temperatura_bajada_filtrada), max(temperatura_bajada_filtrada), 100);

% Calcular los valores ajustados usando el modelo y los valores de temperatura generados
voltaje_ajustado = feval(fit_bajada, temperatura_para_grafica);

% Graficar los valores experimentales
scatter(temperatura_bajada_filtrada, voltaje_bajada_filtrado, 'o', 'MarkerFaceColor', 'black', 'MarkerEdgeColor', 'black');
hold on; % Mantener la gráfica actual

% Graficar la curva ajustada
plot(temperatura_para_grafica, voltaje_ajustado, 'r', 'LineWidth', 2);

% Etiquetas y título del gráfico
xlabel('Temperatura [K]');
ylabel('Voltaje [V]');

% Leyenda
legend('Valores Experimentales', 'Curva Ajustada');

% Mostrar la cuadrícula
grid on;

% Liberar el modo "hold"
hold off;