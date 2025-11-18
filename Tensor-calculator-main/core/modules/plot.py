import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp
from .simplify import Simple


class plot:
    """Moduł do generowania wykresów metryki i tensorów geometrycznych"""
    
    @staticmethod
    def plot_metric_3d(g, wspolrzedne, parametry_wartosci, coord_ranges):
        n = len(wspolrzedne)
        subs_dict = {param: val for param, val in parametry_wartosci.items()}
        
        nonzero_components = []
        for i in range(n):
            for j in range(i, n):
                component = Simple.custom_simplify(g[i, j])
                if component != 0:
                    nonzero_components.append((i, j, component))
        
        if not nonzero_components:
            return
        
        coords_to_plot = [coord for coord in wspolrzedne if coord in coord_ranges]
        
        if len(coords_to_plot) < 2:
            return
        
        coord1, coord2 = coords_to_plot[0], coords_to_plot[1]
        c1_min, c1_max, c1_steps = coord_ranges[coord1]
        c2_min, c2_max, c2_steps = coord_ranges[coord2]
        
        X = np.linspace(c1_min, c1_max, c1_steps)
        Y = np.linspace(c2_min, c2_max, c2_steps)
        X_mesh, Y_mesh = np.meshgrid(X, Y)
        
        fig = plt.figure(figsize=(12, 6*len(nonzero_components)))
        
        for idx, (i, j, component) in enumerate(nonzero_components):
            ax = fig.add_subplot(len(nonzero_components), 1, idx+1, projection='3d')
            
            expr = component.subs(subs_dict)
            f = sp.lambdify([coord1, coord2], expr, 'numpy')
            
            try:
                Z = f(X_mesh, Y_mesh)
                surf = ax.plot_surface(X_mesh, Y_mesh, Z, cmap='viridis', alpha=0.9, edgecolor='none')
                ax.set_xlabel(str(coord1), fontsize=10)
                ax.set_ylabel(str(coord2), fontsize=10)
                ax.set_zlabel(f'g_{i}{j}', fontsize=10)
                ax.set_title(f'g_{i}{j}', fontsize=12)
                fig.colorbar(surf, ax=ax, shrink=0.5, pad=0.1)
            except Exception as e:
                print(f"Błąd g_{i}{j}: {e}")
        
        plt.tight_layout()
        plt.savefig('metric_3d_plot.png', dpi=150, bbox_inches='tight')
        plt.show()
    
   