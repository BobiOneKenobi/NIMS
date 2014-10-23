%% Copyright 2014 MERCIER David
function A_thin_films_properties_GUI
%% Function used to create buttons in the GUI in function of the number of thin films
gui = guidata(gcf);

%% Film 0
% Thickness of the thin film
gui.handles.title_thinfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.05 0.05 0.22 0.7],...
    'String', 'Thickness film 0 :',...
    'HorizontalAlignment', 'left'); 

gui.handles.value_thinfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.27 0.05 0.1 0.9],...
    'String', 500,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_thickfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.37 0.05 0.06 0.7],...
    'String', 'nm',...
    'HorizontalAlignment', 'center');

% Young's modulus of the thin film
gui.handles.title_youngfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.43 0.05 0.1 0.7],...
    'String', ' /  YM :',...
    'HorizontalAlignment', 'left');

gui.handles.value_youngfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.53 0.05 0.1 0.9],...
    'String', 100,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_youngfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.63 0.05 0.08 0.7],...
    'String', 'GPa',...
    'HorizontalAlignment', 'center');

% Poisson's ratio of the thin film
gui.handles.title_poissfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.71 0.05 0.1 0.7],...
    'String', ' /  PR :',...
    'HorizontalAlignment', 'left');

gui.handles.value_poissfilm0_GUI = uicontrol('Parent', gui.handles.bg_film0_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.81 0.05 0.1 0.9],...
    'String', 0.3,...
    'Callback', 'A_get_and_plot');

%% Film 1
% Thickness of the thin film
gui.handles.title_thinfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.05 0.05 0.22 0.7],...
    'String', 'Thickness film 1 :',...
    'HorizontalAlignment', 'left');

gui.handles.value_thinfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.27 0.05 0.1 0.9],...
    'String', 500,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_thickfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.37 0.05 0.06 0.7],...
    'String', 'nm',...
    'HorizontalAlignment', 'center');

% Young's modulus of the thin film
gui.handles.title_youngfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.43 0.05 0.1 0.7],...
    'String', ' /  YM :',...
    'HorizontalAlignment', 'left');

gui.handles.value_youngfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.53 0.05 0.1 0.9],...
    'String', 100,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_youngfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.63 0.05 0.08 0.7],...
    'String', 'GPa',...
    'HorizontalAlignment', 'center');

% Poisson's ratio of the thin film
gui.handles.title_poissfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.71 0.05 0.1 0.7],...
    'String', ' /  PR :',...
    'HorizontalAlignment', 'left');

gui.handles.value_poissfilm1_GUI = uicontrol('Parent', gui.handles.bg_film1_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.81 0.05 0.1 0.9],...
    'String', 0.3,...
    'Callback', 'A_get_and_plot');

%% Film 2
% Thickness of the thin film
gui.handles.title_thinfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.05 0.05 0.22 0.7],...
    'String', 'Thickness film 2 :',...
    'HorizontalAlignment', 'left');

gui.handles.value_thinfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.27 0.05 0.1 0.9],...
    'String', 500,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_thickfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.37 0.05 0.06 0.7],...
    'String', 'nm',...
    'HorizontalAlignment', 'center');

% Young's modulus of the thin film
gui.handles.title_youngfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.43 0.05 0.1 0.7],...
    'String', ' /  YM :',...
    'HorizontalAlignment', 'left');

gui.handles.value_youngfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.53 0.05 0.1 0.9],...
    'String', 100,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_youngfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.63 0.05 0.08 0.7],...
    'String', 'GPa',...
    'HorizontalAlignment', 'center');

% Poisson's ratio of the thin film
gui.handles.title_poissfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.71 0.05 0.1 0.7],...
    'String', ' /  PR :',...
    'HorizontalAlignment', 'left');

gui.handles.value_poissfilm2_GUI = uicontrol('Parent', gui.handles.bg_film2_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.81 0.05 0.1 0.9],...
    'String', 0.3,...
    'Callback', 'A_get_and_plot');

%% Properties of the substrate
% Young's modulus of the substrate
gui.handles.title_youngsub_GUI = uicontrol('Parent', gui.handles.bg_substrat_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.05 0.05 0.3 0.9],...
    'String', 'Young''s modulus of the substrate :',...
    'HorizontalAlignment', 'left');

gui.handles.value_youngsub_GUI = uicontrol('Parent', gui.handles.bg_substrat_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.35 0.05 0.1 0.9],...
    'String', 165,...
    'Callback', 'A_get_and_plot');

gui.handles.unit_youngsub_GUI = uicontrol('Parent', gui.handles.bg_substrat_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.45 0.05 0.08 0.7],...
    'String', 'GPa',...
    'HorizontalAlignment', 'center');

% Poisson's ratio of the substrate
gui.handles.title_poisssub_GUI = uicontrol('Parent', gui.handles.bg_substrat_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'text',...
    'Position', [0.55 0.05 0.3 0.9],...
    'String', 'Poisson''s ratio of the substrate :',...
    'HorizontalAlignment', 'left');

gui.handles.value_poisssub_GUI = uicontrol('Parent', gui.handles.bg_substrat_properties_GUI,...
    'Units', 'normalized',...
    'Style', 'edit',...
    'Position', [0.85 0.05 0.1 0.9],...
    'String', 0.28,...
    'Callback', 'A_get_and_plot');

guidata(gcf, gui);

end