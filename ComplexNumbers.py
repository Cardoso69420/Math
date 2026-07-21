import sympy as sp

i = sp.I
e = sp.exp
theta = sp.Symbol('theta', real=True)
euler_form = sp.exp(i * theta)


YELLOW = "\033[93m"
RED = "\033[31m"
BLUE = "\033[94m"
GREEN = "\033[32m"
RESET = "\033[0m"


#Vamos analisar a parte Real e Imaginária de um número complexo
def complex_number_z(z):
    real_part = sp.re(z)
    complex_part = sp.im(z)
    print(f"{BLUE}Parte Real ={RESET} {YELLOW}{real_part}{RESET}, {BLUE}Parte imaginária ={RESET} {YELLOW}{complex_part}{RESET}")


#Calcular a distância do ponto ao centro do gráfico (Módulo)
def complex_point_distance(z):
    abs_z = sp.Abs(z)
    return abs_z


#Calcula o ângulo, em radianos, que o número faz com o eixo horizontal positivo no gráfico
def complex_angle(z):
    angle_z = sp.arg(z)
    return angle_z


#Inversão do sinal da parte Imaginária (Conjugado)
def reverse(z):
    reverse_z = sp.conjugate(z)
    return reverse_z


#Devolve o número complexo em forma de coordenada
def complex_coordenates(z):
    coordenate_z = z.as_real_imag()
    return coordenate_z


#Esta função existe unicamente para facilitar o calculo de número complexos mais dificeis
def advanced_complex_calcule(z):
    number_z = sp.expand_complex(z)
    return number_z

#Reescreve a formúla trigonométrica de e^i*theta
def trigonometric_form(euler):
    trig_form = advanced_complex_calcule(euler)
    return trig_form


#Vamos escrever o Seno usando euler, theta e i
def complex_sin(angle):
    sin = sp.sin(angle)
    sin_with_euler = sin.rewrite(e)
    return sin_with_euler


#Vamos escrever o Cosseno usando euler, theta e i
def complex_cos(angle):
    cos = sp.cos(angle)
    cos_with_euler = cos.rewrite(e)
    return cos_with_euler


#Vamos escrever a tangente usando euler, theta e i
def complex_tan(angle):
    tan = sp.tan(angle)
    tan_with_euler = tan.rewrite(e)
    return tan_with_euler

#Função para validações
def valid_answer(message):
    while True:
        try:
            user_input = input(f"{GREEN}{message}{RESET}").strip()
            
            value = sp.sympify(user_input)
            
            if value is not None:
                return value
            
            else:
                print(f"{RED}Ângulo inválido. Tenta novamente.{RESET}\n")

        except (sp.SympifyError, TypeError, ValueError):
            print(f"{RED}.{RESET}\n")




#Função principal que vai correr todas as operações
def complex_numbers():
    Operations = {
        "1": ("Número complexo", complex_number_z),
        "2": ("Distância de um número complexo", complex_point_distance),
        "3": ("Ângulo de um número complexo", complex_angle),
        "4": ("Inverso de um número complexo", reverse), 
        "5": ("Coordenadas de um número complexo", complex_coordenates),
        "6": ("Cálculo de números complexos mais dificeis", advanced_complex_calcule),
        "7": ("Forma trigonométrica de um número complexo", trigonometric_form),     
        "8": ("Seno usando o número de Euler", complex_sin),        
        "9": ("Cosseno usando o número de Euler", complex_cos), 
        "10": ("Tangente usando o número de Euler", complex_tan)                    
    }

    while True:
        print(f"{YELLOW}Escolhe uma operação das seguintes:{RESET}")

        for key, (name, _) in Operations.items():
            print(f"{GREEN}{key} - {name}{RESET}")

        option = input(f"{GREEN}Opção: {RESET}")

        if option not in Operations:
            print(f"{RED}Opção inválida.{RESET}\n")
            continue

        name, operation_complex = Operations[option]

        if option == "8":
            angle_value_sin = valid_answer("Introduz o valor do ângulo Theta: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{complex_sin(angle_value_sin)}{RESET}\n")
        
        elif option == "9":
            angle_value_cos = valid_answer("Introduz o valor do ângulo Theta: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{complex_cos(angle_value_cos)}{RESET}\n")

        elif option == "10":
            angle_value_tan = valid_answer("Introduz o valor do ângulo Theta: ")
            print(f"{BLUE}{name}:{RESET} {YELLOW}{complex_tan(angle_value_tan)}{RESET}\n")

        else:
            while True:
                complex_number_value = input(f"{GREEN}Introduz um número complexo: {RESET}").strip()

                fixed_input = complex_number_value.replace('i', 'I')
                for d in '0123456789':
                    fixed_input = fixed_input.replace(f'{d}I', f'{d}*I')

                try:
                    z_value = sp.sympify(fixed_input)
                    if i not in z_value.free_symbols and not z_value.has(i):
                        continue
                    break

                except (sp.SympifyError, TypeError):
                    print(f"{RED}Número complexo inválido.{RESET}\n")
                    continue
            
            print(f"{BLUE}{name}:{RESET} {YELLOW}{operation_complex(z_value)}{RESET}\n")

        new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")

        while new_operation != "":
            new_operation = input(f"{YELLOW}Clique 'Enter' para fazer outra operação: {RESET}")


if __name__ == '__main__':
    complex_numbers()