%% Copyright 2014 MERCIER David
function get_and_plot
%% Function used to get and plot data
gui = guidata(gcf);

gui.handles.h_waitbar = waitbar(0, 'Calculations in progress...');
steps = 100;
for step = 1:steps
    waitbar(step / steps, gui.handles.h_waitbar);
end

%% Cleaning of data
gui.results = struct();
guidata(gcf, gui);

clean_data;
gui = guidata(gcf); guidata(gcf, gui);

%% Refreshing the GUI and getting parameters and
refresh_param_GUI;
get_param_GUI;

if ~gui.flag.wrong_inputs
    if gui.flag.flag_no_csm ~= 1
        CSM_correction;
    end
    
    %% Get parameters
    model_set_parameters;
    gui = guidata(gcf); guidata(gcf, gui);
    
    %% Load-Displacement curve analysis
    if gui.variables.y_axis == 1
        model_load_disp;
        gui = guidata(gcf); guidata(gcf, gui);
        gui.results.P_fit = gui.results.P_fit./gui.data.loadFact;
        guidata(gcf, gui);
    end
    
    %% Stiffness analysis
    if gui.variables.y_axis == 2
        model_stiffness;
        gui = guidata(gcf); guidata(gcf, gui);
        gui.results.S_fit = gui.results.S_fit./gui.data.stifFact;
        guidata(gcf, gui);
    end
    
    %% Load over stiffness squared analysis
    if gui.variables.y_axis == 3
        model_loadOverstiffnessSquared;
        gui = guidata(gcf); guidata(gcf, gui);
        gui.results.LS2_fit = gui.results.LS2_fit .* (gui.data.stifFact.^2) ./ ...
            gui.data.loadFact;
        gui.results.delta_LS2 = ...
            ls2_incertitude(gui.data.P, gui.data.S, gui.results.LS2,...
            gui.data.delta_P, gui.data.delta_S);
        guidata(gcf, gui);
    end
    
    %% Calculations of function area (for all cases, needed of contact radius estimation)
    model_function_area;
    gui = guidata(gcf); guidata(gcf, gui);
    
    %% Calculations of Young's modulus or Hardness
    if gui.variables.y_axis == 4 || gui.variables.y_axis == 5
        [gui.results.Eeff_red, gui.results.Esample_red, gui.results.Esample] = ...
            model_elastic(gui.data.S, gui.results.Ac, gui.data.nuf, gcf);
        gui.results.delta_E = ...
            elasticModulus_incertitude(gui.data.P, gui.data.h, gui.data.S, ...
            gui.results.hc, gui.results.Eeff_red, ...
            gui.data.delta_P, gui.data.delta_h, gui.data.delta_S);
        guidata(gcf, gui);
        %% Set model to use for calculations
        if get(gui.handles.value_numthinfilm_GUI, 'Value') == 2
            model_bilayer_elastic(gui.variables.val2);
        elseif get(gui.handles.value_numthinfilm_GUI, 'Value') > 2
            model_multilayer_elastic(gui.variables.val2);
        end
    elseif gui.variables.y_axis == 6
        gui.results.H = model_hardness(gui.data.P, gui.results.Ac);
        gui.results.delta_H = ...
            hardness_incertitude(gui.data.P, gui.data.h, gui.data.S, ...
            gui.results.hc, gui.results.H, ...
            gui.data.delta_P, gui.data.delta_h, gui.data.delta_S);
        guidata(gcf, gui);
        %% Set model to use for calculations
        if get(gui.handles.value_numthinfilm_GUI, 'Value') == 2
            model_bilayer_plastic(gui.variables.val2);
        elseif get(gui.handles.value_numthinfilm_GUI, 'Value') > 2
            model_multilayer_plastic(gui.variables.val2);
        end
        
    end
    
    if gui.variables.y_axis == 7 || gui.variables.y_axis == 8
        gui.data.hr = plasticDepth(gui.data.h, gui.data.P, gui.data.S);
        P = polyfit(gui.data.h,gui.data.hr,1);
        % y_linFit = P(1)*gui.data.h+P(2); % to plot the fit...
        gui.data.results.slopeDepth = P(1);
        [gui.results.Eeff_red, gui.results.Esample_red, gui.results.Esample] = ...
            model_elasticModulus_Guillonneau(gui.variables.val1, gui.data.P, ...
            gui.data.S, gui.data.results.slopeDepth, gui.data.indenter_tip_angle, ...
            1.5, gui.data.nuf, gcf, gui.config.numerics.alpha_Loubet);
        for ii = 1:1:length(gui.data.h)
            gui.results.Em_red(ii) = 0;
            gui.results.Hf(ii) = 0;
            gui.results.delta_E(ii) = 0;
            gui.results.delta_H(ii) = 0;
        end
    end
    
    if gui.variables.y_axis == 7
        guidata(gcf, gui);
    elseif gui.variables.y_axis == 8
        gui.results.H = model_hardness_Guillonneau(gui.data.P, gui.data.S, ...
            gui.results.Esample_red);
        guidata(gcf, gui);
    end
    
    % Be careful of the order of the 3 following lines, because gcf is
    % the waitbar during calculations !!!
    gui = guidata(gcf);
    delete(gui.handles.h_waitbar);
    guidata(gcf, gui);
    
    % Refactor data for plot
    gui.data.h = gui.data.h/gui.data.dispFact;
    gui.data.delta_h = gui.data.delta_h/gui.data.dispFact;
    gui.data.P = gui.data.P/gui.data.loadFact;
    gui.data.delta_P = gui.data.delta_P/gui.data.loadFact;
    gui.data.S = gui.data.S/gui.data.stifFact;
    gui.data.delta_S = gui.data.delta_S/gui.data.stifFact;
    
    guidata(gcf, gui);
    
    %% Plot data
    plot_exp_vs_mod_setvariables;
    gui = guidata(gcf); guidata(gcf, gui);
    
    plot_exp_vs_mod;
    if gui.variables.val2 > 1
        rSquare = r_square(gui.axis.y2plot, gui.axis.y2plot_2);
        xl = xlim;
        yl = ylim;
        text(xl(2)-0.1*xl(2), yl(2)-0.05*yl(2), ['R�=',num2str(rSquare)]);
    end
    gui = guidata(gcf);
else
    warndlg(gui.flag.warnText, 'Input Error');
    delete(gui.handles.h_waitbar);
end

% Update date and clock
set(gui.handles.date_GUI, ...
    'String', datestr(datenum(clock),'mmm.dd,yyyy HH:MM'));

guidata(gcf, gui);

end