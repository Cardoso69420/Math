import sympy as sp
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor


n = sp.Symbol('n', integer=True, positive=True)


YELLOW = "\033[93m"
RED = "\033[31m"
BLUE = "\033[94m"
GREEN = "\033[32m"
RESET = "\033[0m"


#Calculo de um termo à escolha
def calculate_term(Un, var, k):
    u_n = Un.subs(var, k)
    print(f"{BLUE}O {k} termo da sucessão {Un} é:{RESET} {YELLOW}{u_n}{RESET}")


#Primeiros k termos
def first_k_terms(Un, var, k):
    u_n = [Un.subs(var, i) for i in range(1, k + 1)]
    return u_n


#Limite da sucessão
def sequence_limit(Un, var):
    lim_u_n = sp.limit(Un, var, sp.oo)
    return lim_u_n


#Somatório dos primeiros k termos
def sum_first_k_terms(Un, var, k):
    sum_u_k = sp.summation(Un, (var, 1, k))
    return sum_u_k


#Somatório de uma série infinita
def infinite_sum(serie, var):
    sum_infinite = sp.summation(serie, (var, 1, sp.oo))
    return sum_infinite


#Representação da série numa forma simbólica
def symbolic_serie(serie, var):
    sum_serie = sp.Sum(serie, (var, 1, sp.oo))
    return sum_serie


#Verificar se a Sucessão é convergente ou divergente
def sequence_converge_diverge(Un, var):
    lim_u_n = sequence_limit(Un, var)

    if lim_u_n.is_number and lim_u_n not in (-sp.oo, sp.oo):
        print(f"{BLUE}A sucessão é convergente pois o limite tende para:{RESET} {YELLOW}{lim_u_n}{RESET}\n")

    else:
        print(f"{BLUE}A sucessão é divergente pois o limite tende para:{RESET} {YELLOW}{lim_u_n}{RESET}\n")


#Verificar se a Série é convergente ou divergente
def serie_converge_diverge(serie):
    try:
        evaluate = serie.is_convergent()

    except Exception:
        print(f"{RED}Não foi possível determinar a convergência{RESET}\n")
        return

    if evaluate == True:
        print(f"{BLUE}A Série é{RESET} {YELLOW}convergente{RESET}\n")

    elif evaluate == False:
        print(f"{BLUE}A Série é{RESET} {YELLOW}divergente{RESET}\n")

    else:
        print(f"{RED}Não é possível determinar{RESET}\n")


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
def sequences_series():
    Operations = {
        "1": ("Um termo", calculate_term),
        "2": ("Pirmeiros n termos de uma sucessão", first_k_terms),
        "3": ("Limite da sucessão", sequence_limit),
        "4": ("Somatório dos primeiros k termos de uma sucessão", sum_first_k_terms),
        "5": ("Somatório de uma série infinita", infinite_sum),
        "6": ("Representação simbólica do somatório de uma série infinita", symbolic_serie),
        "7": ("Convergência de uma sucessão", sequence_converge_diverge),
        "8": ("Convergência de uma série", serie_converge_diverge)
    }
    
    while True:
        print(f"{YELLOW}Escolhe uma operação das seguintes:{RESET}")

        for key, (name, _) in Operations.items():
            print(f"{GREEN}{key} - {name}{RESET}")

        option = input(f"{GREEN}Opção: {RESET}")

        if option not in Operations:
            print(f"{RED}Opção inválida.{RESET}\n")
            continue

        name, operation_series = Operations[option]

        while True:
            termo = input(f"{GREEN}Introduz o termo geral da sucessão/série (em função de n): {RESET}")

            try:
                transformations = standard_transformations + (implicit_multiplication_application, convert_xor)
                Un_serie = parse_expr(termo, transformations=transformations, local_dict={"n": n})

                if n not in Un_serie.free_symbols:
                    continue

                else:
                    break

            except (sp.SympifyError, TypeError, SyntaxError):
                print(f"{RED}Expressão inválida.{RESET}\n")

        if option == "1":
            term = valid_answer("Introduz um termo para calcular (k): ")
            calculate_term(Un_serie, n, term)

        elif option == "2":
            n_terms = valid_answer("Introduz quantos termos queres que apareçam (k): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{first_k_terms(Un_serie, n, n_terms)}{RESET}\n")

        elif option == "4":
            k_sum = valid_answer("Introduz quantos termos queres que sejam somados (k): ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{sum_first_k_terms(Un_serie, n, k_sum)}{RESET}\n")

        elif option == "7":
            sequence_converge_diverge(Un_serie, n)

        elif option == "8":
            serie = sp.Sum(Un_serie, (n, 1, sp.oo))
            serie_converge_diverge(serie)

        else:
            print(f"{BLUE}{name}:{RESET} {YELLOW}{operation_series(Un_serie, n)}{RESET}\n")

        new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")

        while new_operation != "":
            new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")


if __name__ == "__main__":
    sequences_series()
