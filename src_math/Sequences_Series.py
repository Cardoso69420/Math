import sympy as sp


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
def first_n_terms(Un, var, k):
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
def infinite_sum(Un, var):
    sum_infinite = sp.summation(Un, (var, 1, sp.oo))
    return sum_infinite


#Representação da série numa forma simbólica
def symbolic_serie(Un, var):
    sum_serie = sp.Sum(Un, (var, 1, sp.oo))
    return sum_serie









def sequences_series():
    print()


if __name__ == "__main__":
    sequences_series()
