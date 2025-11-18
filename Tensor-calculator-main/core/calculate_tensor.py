import sympy as sp
from core.modules.simplify import Simple
from core.modules.index import index



class display():
    def write_scalar_curvatre(scalar_curvature, n):
        print("Curvature sclar R:")
        sp.pprint(scalar_curvature)
        print("")

    def write_einstein_components(G_upper, G_lower, n):
        print("Non zero Einstein tensor (G^i_j):")
        for i in range(n):
            for j in range(n):
                val = Simple.custom_simplify(G_upper[i, j])
                if val != 0:
                
                    print(f"G^{{{i}}}_{{{j}}} = {val}")
        print("")
        
        print("Non zero Einstein tensor (G_ij):")
        for i in range(n):
            for j in range(n):
                val = Simple.custom_simplify(G_lower[i, j])
                if val != 0:
                
                    print(f"G_{{{i}{j}}} = {val}")
        print("")

    def write_metric_components(g, n):
        print("Metric tensor (g_{ij}):")
        for i in range(n):
            for j in range(i, n):
                val = Simple.custom_simplify(g[i, j])
                if val != 0:
                    print(f"g_{i}{j} = {val}")
        print("")

    def write_christoffel_symbols(Gamma, n):
        print("Non zero Christoffel symbols (Γ^a_{bc}):")
        ch_index = index.generate_index_christoffel(n)
        for (a, b, c) in ch_index:
            val = Gamma[a][b][c]
            if Simple.custom_simplify(val) != 0:
            
                print(f"\\Gamma^{{{a}}}_{{{b}{c}}} = {val}")
        print("")

    def write_full_riemann_components(R_abcd, n):
        print("Non zero components Riemann tensor (R_{abcd}):")
        riemann_index = index.generate_index_riemann(n)
        for (a, b, c, d) in riemann_index:
            val = R_abcd[a][b][c][d]
            if val != 0:
            
                print(f"R_{{{a}{b}{c}{d}}} = {val}")
        print("")

    def write_ricci_components(Ricci, n):
        print("Non zero components Ricci tensor (R_{ij}):")
        ricci_index = index.generate_index_ricci(n)
        for (i, j) in ricci_index:
            val = Ricci[i, j]
            if val != 0:
                
                print(f"R_{{{i}{j}}} = {val}")
        print("")

