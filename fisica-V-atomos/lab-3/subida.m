table_subida = readtable('subida.csv');


voltaje_subida = table_subida.V;
temperatura_subida = table_subida.TK;

ft = fittype( 'power2' );
opts = fitoptions( 'Method', 'NonlinearLeastSquares' );
opts.Algorithm = 'Levenberg-Marquardt';
opts.DiffMinChange = 1e-10;
opts.Display = 'Off';
opts.Lower = [-Inf 3 -Inf];
opts.MaxFunEvals = 1000;
opts.MaxIter = 2000;
opts.StartPoint = [1.09010609020783e-40 15.2862458371299 0];
opts.TolFun = 1e-09;
opts.TolX = 1e-09;
opts.Upper = [Inf 5 Inf];

[fit_subida, fit_subida_error] = fit( temperatura_subida, voltaje_subida, ft, opts );



% Crear una serie de valores para la temperatura para graficar la curva ajustada
temperatura_para_grafica = linspace(min(temperatura_subida), max(temperatura_subida), 100);

% Calcular los valores ajustados usando el modelo y los valores de temperatura generados
voltaje_ajustado = feval(fit_subida, temperatura_para_grafica);

% Graficar los valores experimentales
scatter(temperatura_subida, voltaje_subida, 'o', 'MarkerFaceColor', 'black', 'MarkerEdgeColor', 'black');
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





