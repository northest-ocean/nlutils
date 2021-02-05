from Figure import Figure
from Visual import draw_single_figure,draw_multi_figures
from CommonDefine import FigureType

import numpy as np

if __name__ == '__main__':
    # Unit test for compare_visualization_polyline
    Xs = [[1, 2, 3, 4, 5, 6], [1, 2, 6, 8, 9, 11]]
    Xs = np.array(Xs)
    Ys = [[1, 2, 6, 7, 8, 9], [2, 5, 7, 8, 9, 11]]
    Ys = np.array(Ys)
    legends = ['x1', 'x2']
    XHs = [[1,1,1,2,4,5,1,2,3,3,2,1,2,2], [1,1,21,2,3,3,4,5,2,1,2,4,46,33,2,12,4,214,12,42,1,2,2]]
    XHs = np.array(XHs)
    XH2s = [1,1,21,2,3,3,4,5,2,1,2,4,46,33,2,12,4,11,12,42,1,2,2]
    XH2s = np.array(XH2s)
    YH2s = [1,1,21,2,3,3,4,5,2,1,2,4,46,33,2,12,4,11,12,42,1,2,2]
    YH2s = np.array(YH2s)
    # styles = [{'color':'yellow', 'alpha':0.5, 'edgecolor':'green'}, {'color':'blue', 'alpha':0.3,'edgecolor':'red'}]
    # print(Xs, Ys, type(XHs))
    fig1 = Figure(FigureType.BAR_PLOT, Xs, Ys, legends, title="Test Case", figure_size=(5, 10))
    fig2 = Figure(FigureType.POLYLINE_PLOT, Xs, Ys, legends, title="Test Case")
    fig3 = Figure(FigureType.SCATTER_PLOT, Xs, Ys, legends, title="Test Case")
    fig4 = Figure(FigureType.HISTOGRAM_PLOT, XHs, legends=legends, title="Test Case")
    fig5 = Figure(FigureType.HISTOGRAM_2D_PLOT, XH2s, YH2s, styles={'bins':50}, title="Test Case")
    # draw_single_figure(fig1)
    draw_multi_figures([fig1, fig2, fig3, fig4, fig5])