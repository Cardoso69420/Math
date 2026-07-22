import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


x = sp.symbols('x')


YELLOW = "\033[93m"
RED = "\033[31m"
BLUE = "\033[94m"
GREEN = "\033[32m"
RESET = "\033[0m"




#Calculo da imagem da função f(x)
def image(func, var, point):
    image = func.subs(var, point)
    return image


#Calculo dos zeros da função f(x)
def zero(func, var):
        zero = sp.solve(func, var)
        return zero


#Limite da função f(x) num ponto
def limit(func, var, point):
    lim = sp.limit(func, var, point)
    return lim


#Limite da função f(x) num ponto para a direita e para a esquerda
def limits_sides(func, var, point):
    lim_right = sp.limit(func, var, point, dir = '+')
    lim_left = sp.limit(func, var, point, dir ='-')
    print(f"{BLUE}O limite à esquerda em {point}(-) é{RESET} {YELLOW}{lim_left}{RESET}")
    print(f"{BLUE}O limite à direita em {point}(+) é{RESET} {YELLOW}{lim_right}{RESET}")


#Continuidade de uma função num ponto
def continuity(func, var, point):
    lim_right = sp.limit(func, var, point, dir = '+')
    lim_left = sp.limit(func, var, point, dir ='-')
    print(f"{BLUE}O limite à esquerda em {point}(-) é{RESET} {YELLOW}{lim_left}{RESET}")
    print(f"{BLUE}O limite à direita em {point}(+) é{RESET} {YELLOW}{lim_right}{RESET}")

    try:
        value = image(func, var, point)

    except Exception:
        None

    if lim_right == lim_left and lim_left == value and lim_right == value:
        print(f"{BLUE}Continuidade:{RESET} {YELLOW}Esta função é continua{RESET}\n")
        
    else:
        print(f"{BLUE}Continuidade:{RESET} {YELLOW}Esta função não é continua{RESET}\n")


#Reta tangente através da formúla da derivada num ponto (m = declive)
def lim_tangent_line(func, var, point):
    f_point = image(func, var, point)
    m = limit((func - f_point) / (var - point), var, point)
    tangent_line = m * (var - point) + f_point
    return tangent_line


#Derivada da função f(x) = f'(x)
def derivative(func, var):
    df = sp.diff(func, var)
    return df


#Reta tangente através das regras da derivação
def derivative_tangent_line(func, var, point):
    f_point = image(func, var, point)
    func_derivative = derivative(func, var)
    m = image(func_derivative, var, point)
    tangent_line = m * (var - point) + f_point
    return tangent_line


#Encontra os extremos e pontos de inflexão:
def extreme_inflection_points(func, var):
    func_first_derivative = derivative(func, var)
    func_first_derivative_zeros = zero(func_first_derivative, var)

    print(f"{BLUE}O(s) extremo(s) da função é(são):{RESET} {YELLOW}{func_first_derivative_zeros}{RESET}\n")

    func_second_derivative = derivative(func_first_derivative, var)

    for point in func_first_derivative_zeros:
        func_second_derivative_image = image(func_second_derivative, var, point)
        func_image_y = image(func, var, point)

        if func_second_derivative_image > 0:
            print(f"{BLUE}O ponto ({point}, {func_image_y} ) é:{RESET} {YELLOW}MÍNIMO da função f(x){RESET}\n")

        elif func_second_derivative_image < 0:
            print(f"{BLUE}O ponto ({point}, {func_image_y} ) é:{RESET} {YELLOW}MÁXIMO da função f(x){RESET}\n")

        else:
            print(f"{BLUE}O ponto ({point}, {func_image_y} ) é:{RESET} {YELLOW}ponto de inflexão da função f(x){RESET}\n")



#Primitiva da função f(x) = F(x) + C
def primitive(func, var):
    C = sp.symbols('C')
    integral = sp.integrate(func, var) + C
    return integral


#Calcula a constante C da primitiva da função f(x)
def calculate_c(func, var, point, value):
    C = sp.symbols('C')
    integral = sp.integrate(func, var) + C
    c_value = sp.solve(integral.subs(var, point) - value, C) # C = f(point) - value
    return c_value[0]


#Integral da função f(x)
def integral(func, var, a, b):
    integral = sp.integrate(func, (var, a, b))
    return integral


#Função em  Série de Taylor em redor de x0 até à ordem n
def taylor_series(func, var, n, x0=1):
    serie = func.series(var, x0, n)
    return serie


#Função em  Série de Taylor em redor de x0 até à ordem n sem o x^n
def taylor_series_polynomial(func, var, n, x0=1):
    serie_polinominal = func.series(var, x0, n).removeO()
    return serie_polinominal



#Função para validações
def valid_answer(message):
    while True:
        try:
            value = sp.sympify(input(f"{GREEN}{message}{RESET}"))
            
            if value.is_number:
                return value
            
            else:
                print(f"{RED}Valor inválido, Introduza um número (ou 'oo' para infinito){RESET}\n")

        except (sp.SympifyError, TypeError):
            print(f"{RED}Valor inválido, Introduza um número (ou 'oo' para infinito){RESET}\n")




#Função principal que vai correr todas as operações
def calculus():
    Operations = {
        "1": ("Imagem", image),
        "2": ("Zero", zero),
        "3": ("Limite", limit),
        "4": ("Limites laterais", limits_sides),
        "5": ("Continuidade", continuity),
        "6": ("Reta tangente (limite)", lim_tangent_line),
        "7": ("Derivada", derivative),
        "8": ("Reta tangente (derivada)", derivative_tangent_line ),
        "9": ("Extremos e pontos de inflexão", extreme_inflection_points),
        "10": ("Primitiva", primitive),
        "11": ("Cálculo do C", calculate_c),
        "12": ("Integral", integral),
        "13": ("Séries de Taylor", taylor_series),
        "14": ("Polinomio de Taylor", taylor_series_polynomial)
    }
    
    while True:
        print(f"{YELLOW}Escolhe uma operação das seguintes:{RESET}")

        for key, (name, _) in Operations.items():
            print(f"{GREEN}{key} - {name}{RESET}")

        option = input(f"{GREEN}Opção: {RESET}")

        if option not in Operations:
            print(f"{RED}Opção inválida.{RESET}\n")
            continue
    
        name, operation_func = Operations[option]
        
        while True:
            function = input(f"{GREEN}Introduz uma função f(x): {RESET}")
 
            try:
                transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
                func = parse_expr(function, transformations = transformations)

                if x not in func.free_symbols:
                    continue
                break
            
            except (sp.SympifyError, TypeError, SyntaxError):
                print(f"{RED}Função inválida.{RESET}\n")
                continue
    
        if option == "1":
            object = valid_answer("Introduz o valor do objeto (x): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{image(func, x, object)}{RESET}")

        elif option == "3":
            point_x = valid_answer("Introduz o ponto para avaliar o limite: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{limit(func, x, point_x)}{RESET}\n")

        elif option == "4":
            point_x = valid_answer("Introduz o ponto para avaliar o limite à esquerda e à direita: ")
            limits_sides(func, x, point_x)

        elif option == "5":
            continuity_point = valid_answer("Introduz o ponto para avaliar a continuidade da função: ")
            continuity(func, x, continuity_point)

        elif option == "6":
            lim_tangent_point = valid_answer("Introduz o ponto de tangência da função (reta tangente): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{lim_tangent_line(func, x, lim_tangent_point)}{RESET}\n")

        elif option == "8":
            derivative_tangent_point = valid_answer("Introduz o ponto de tangência da função (reta tangente): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{derivative_tangent_line(func, x, derivative_tangent_point)}{RESET}\n")

        elif option == "9":
            extreme_inflection_points(func, x)

        elif option == "11":
            object_x = valid_answer("Introduz o ponto para calcular a constante C da primitiva: ")
            image_y = valid_answer("Introduz o valor da função nesse ponto: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{calculate_c(func, x, object_x, image_y)}{RESET}\n")

        elif option == "12":
            a = valid_answer("Introduz o limite inferior da integral: ")
            b = valid_answer("Introduz o limite superior da integral: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{integral(func, x, a, b)}{RESET}\n")
        
        elif option == "13":
            Order = valid_answer("Introduz a ordem (n): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{taylor_series(func, x, Order, 1)}{RESET}")

        elif option == "14":
            Order = valid_answer("Introduz a ordem (n): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{taylor_series_polynomial(func, x, Order, 1)}{RESET}")

        else:
            print(f"{BLUE}{name}:{RESET} {YELLOW}{operation_func(func, x)}{RESET}\n")

        new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")

        while new_operation != "":
            new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")


if __name__ == "__main__":
    calculus()