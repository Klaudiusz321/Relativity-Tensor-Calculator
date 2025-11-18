# Relativity Tensor Calculator

Calculate and visualize tensors for arbitrary metrics in General Relativity.

## Features

- Parse metric from text file (format: `coords; params` and `i j expression`)
- Compute Christoffel symbols, Riemann tensor, Ricci tensor, Ricci scalar
- Calculate Einstein tensor
- Generate 3D visualizations of metric components

## Installation

```bash
pip install sympy matplotlib numpy
```

## Usage

1. Create metric file (e.g., `metric.txt`):
```
T, G, F; a
0 0 -a**2
1 1 a**2 * cosh(T)**2
2 2 a**2 * sin(G)**2 * cosh(T)**2
```

2. Run:
```bash
python main.py
```

Output includes:
- Tensor components (console)
- 3D metric plots (`metric_3d_plot.png`)

## Structure

```
core/
  core.py          - Tensor computations
  load.py          - Metric parser
  calculate_tensor.py - Display functions
  modules/
    simplify.py    - Symbolic simplification
    index.py       - Index generation
    plot.py        - 3D visualization
main.py            - Entry point
```

## Metric File Format

```
coordinate1, coordinate2, ...; parameter1, parameter2, ...
i j metric_component_expression
```

Expressions support sympy syntax.
