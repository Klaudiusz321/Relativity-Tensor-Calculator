

def process_latex(latex_str):
   
    def remove_function_argument(latex):
        result = ""
        i = 0
        while i < len(latex):
            if latex[i].isalpha():
                start = i
                while i < len(latex) and latex[i].isalpha():
                    i += 1
                func_name = latex[start:i]
                
                if i < len(latex) and latex[i] == '(':
                    i += 1  
                    arg_start = i
                    paren_count = 1
                    while i < len(latex) and paren_count > 0:
                        if latex[i] == '(':
                            paren_count += 1
                        elif latex[i] == ')':
                            paren_count -= 1
                        i += 1
                    arg = latex[arg_start:i-1].strip()
                    if arg in ['\\chi', 'chi']:
                       
                        result += func_name
                    else:
                        
                        result += f"{func_name}({arg})"
                else:
                   
                    result += func_name
            else:
                
                result += latex[i]
                i += 1
        return result

 
    def replace_derivative(latex):
        search_str = "\\frac{d}{d \\chi}"
        while search_str in latex:
            index = latex.find(search_str)
            
            after = latex[index + len(search_str):]
           
            var_end = index + len(search_str)
            while var_end < len(latex) and (latex[var_end].isalpha() or latex[var_end] == '\\'):
                var_end += 1
            var = latex[index + len(search_str):var_end].strip()
            
            if var.startswith('\\'):
                var_name = ""
                j = 0
                while j < len(var) and (var[j].isalpha() or var[j] == '\\'):
                    var_name += var[j]
                    j += 1
                var_replaced = f"{var_name}'"
            else:
                var_replaced = f"{var}'"
          
            latex = latex[:index] + var_replaced + latex[var_end:]
        return latex

    
    latex_str = remove_function_argument(latex_str)
   
    latex_str = replace_derivative(latex_str)

    return latex_str