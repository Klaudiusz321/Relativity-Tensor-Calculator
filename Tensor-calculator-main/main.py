from core.calculate_tensor import display
from core.core import compute
from core.load import load
from core.modules.plot import plot


def wyswietl_tensory(g, Gamma, R_abcd, Ricci, Scalar_Curvature, G_upper, G_lower, n):
    display.write_metric_components(g, n)
    display.write_christoffel_symbols(Gamma, n)
    display.write_full_riemann_components(R_abcd, n)
    display.write_ricci_components(Ricci, n)
    display.write_einstein_components(G_upper, G_lower, n)
    display.write_scalar_curvatre(Scalar_Curvature, n)

    print("")


if __name__ == "__main__":

    filename = r"C:\Users\sorak\Desktop\metric.txt.txt"

    wspolrzedne, parametry, metryka = load.wczytaj_metryke(filename)
    print("Coordinates:", wspolrzedne)
    print("Parameters:", parametry)
    print("Metric (non zero elements):", metryka)
    print("")

    if wspolrzedne and metryka:
        g, Gamma, R_abcd, Ricci, Scalar_Curvature = compute.oblicz_tensory(wspolrzedne, metryka)
        
  
        try:
            g_inv = g.inv()
        except Exception as e:
            print("Błąd przy obliczaniu odwrotnej metryki:", e)
            exit(1)
        
       
        G_upper, G_lower = compute.compute_einstein_tensor(Ricci, Scalar_Curvature, g, g_inv, len(wspolrzedne))
        
       
        wyswietl_tensory(g, Gamma, R_abcd, Ricci, Scalar_Curvature, G_upper, G_lower, len(wspolrzedne))
        
        # ========== AUTOMATYCZNE GENEROWANIE WYKRESÓW ==========
        print("\n" + "="*50)
        print("GENEROWANIE WYKRESÓW METRYKI")
        print("="*50 + "\n")
        
        try:
            # Automatyczne ustawienie wartości numerycznych dla parametrów
            # Dla każdego parametru użyj stałej wartości numerycznej
            parametry_wartosci = {}
            for param in parametry:
                param_str = str(param)
                # Przydziel wartości numeryczne na podstawie nazwy parametru
                if param_str in ['a', 'M', 'm']:
                    parametry_wartosci[param] = 1.0  # Masa/skala
                elif param_str in ['tau', 'T', 't']:
                    parametry_wartosci[param] = 0.5  # Czas
                elif param_str in ['psi', 'phi', 'F']:
                    parametry_wartosci[param] = 1.0  # Kąt/pole
                elif param_str in ['theta', 'G', 'g']:
                    parametry_wartosci[param] = 1.5708  # π/2
                else:
                    parametry_wartosci[param] = 1.0  # Domyślna wartość
            
            # Automatyczne ustawienie zakresów współrzędnych na podstawie nazwy
            coord_ranges = {}
            for coord in wspolrzedne:
                coord_str = str(coord)
                if coord_str in ['T', 'tau', 't']:
                    coord_ranges[coord] = (-2.0, 2.0, 50)  # Zakres czasu
                elif coord_str in ['G', 'theta', 'g']:
                    coord_ranges[coord] = (0, 3.14159, 50)  # Zakres kąta
                elif coord_str in ['F', 'phi', 'p']:
                    coord_ranges[coord] = (0, 6.28318, 50)  # Pełny obrót
                else:
                    coord_ranges[coord] = (0.1, 5.0, 50)  # Domyślny zakres
            
            # Rysuj metrykę
            print("Rysowanie komponentów metryki 3D...")
            plot.plot_metric_3d(g, wspolrzedne, parametry_wartosci, coord_ranges)
            
            print("\n✓ Wykresy zostały wygenerowane i zapisane!")
            
        except Exception as e:
            print(f"Błąd przy generowaniu wykresów: {e}")
            import traceback
            traceback.print_exc()