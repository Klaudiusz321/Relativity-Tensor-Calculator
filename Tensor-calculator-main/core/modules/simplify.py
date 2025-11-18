from sympy import simplify, factor, expand, trigsimp, cancel, ratsimp

class Simple():
    def custom_simplify(expr):
        expr_simpl = expand(expr)
        expr_simpl = trigsimp(expr_simpl)
        expr_simpl = factor(expr_simpl)
        expr_simpl = simplify(expr_simpl)
        expr_simpl = cancel(expr_simpl)
        expr_simpl = ratsimp(expr_simpl)
        
        return expr_simpl