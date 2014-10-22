%% Copyright 2014 MERCIER David
function model_perriot_barthel
%% Function used to calculate Young's modulus in bilayer system with the model of Perriot et al. (2003)
gui = guidata(gcf);

x = gui.results.t_corr./gui.results.ac;

% Coefficient 'n_perriot' between 1.06 and 1.32 function of the ratio Es/Ef !!!
bilayer_model = @(Ef_red_sol, x) (1e-9*((1e9*Ef_red_sol(1)) + ...
	((gui.data.Es_red-(1e9*Ef_red_sol(1)))./(1+(x.*(10.^(-0.093+0.792.*log10(gui.data.Es_red./(1e9*Ef_red_sol(1))) + ...
	0.05.*(log10(gui.data.Es_red./(1e9*Ef_red_sol(1))).^2))).^Ef_red_sol(2))))));

% Make a starting guess at the solution (Ef in GPa)
gui.results.Ef_red_sol0 = [str2double(get(gui.handles.value_youngfilm1_GUI, 'String')); 1.2];

OPTIONS = optimset('lsqcurvefit');
OPTIONS = optimset(OPTIONS, 'TolFun',  1e-20);
OPTIONS = optimset(OPTIONS, 'TolX',    1e-20);
OPTIONS = optimset(OPTIONS, 'MaxIter', 10000);
[gui.results.Ef_red_solfit, gui.results.resnorm, gui.results.residual, gui.results.exitflag, gui.results.output, gui.results.lambda, gui.results.jacobian] =...
    lsqcurvefit(bilayer_model, gui.results.Ef_red_sol0, x, gui.results.Esample_red, [0;1.06], [1000;1.32], OPTIONS);

gui.results.Ef_sol_fit(1) = gui.results.Ef_red_solfit(1) * (1-gui.data.nuf^2);

gui.results.Em_red = 1e-9*((1e9*gui.results.Ef_red_solfit(1))+...
    ((gui.data.Es_red-(1e9*gui.results.Ef_red_solfit(1))) ./ (1+(x.*(10.^(-0.093+0.792.*log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))) + ...
	0.05 .* (log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))).^2)))).^gui.results.Ef_red_solfit(2))));

gui.results.Ef_red = 1e-9*(((1e9.*gui.results.Esample_red)-...
    (gui.data.Es_red./(1+(x.*(10.^(-0.093+0.792.*log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))) + ...
	0.05 .* (log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))).^2)))).^gui.results.Ef_red_solfit(2)))) ./ (1-(1./(1+(x.*(10.^(-0.093+0.792.*log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))) + ...
	0.05 .* (log10(gui.data.Es_red./(1e9*gui.results.Ef_red_solfit(1))).^2)))).^gui.results.Ef_red_solfit(2)))));

guidata(gcf, gui);

end