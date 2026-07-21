import sympy as sp


x = sp.symbols('x')


YELLOW = "\033[93m"
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[94m"
RESET = "\033[0m"




#Esta função vai calcular areas de figuras geométricas (b = base, h = altura)
def area(figure, b, h):
    if figure == 'quadrado':
        area = b**2

    elif figure == 'retangulo':
        area = b * h

    elif figure == 'triangulo':
        area = (b * h) / 2

    elif figure == 'circulo':
        area = sp.pi * (b**2)

    else:
        area = None

    return area


#Esta função vai fazer o teorema te pitagoras para calcular a hipotenusa de um triângulo retângulo
def pitagoras(a, b):
    c = sp.sqrt(a**2 + b**2)
    return c


#Esta função vai calcular o seno, cosseno e a tangente através do SOHCAHTOA
def sohcahtoa(adjacent, opposite, hipotenuse):
    sin = opposite / hipotenuse
    cos = adjacent / hipotenuse
    tan = opposite / adjacent
    print(f"{BLUE}Seno{RESET} {GREEN}={RESET} {YELLOW}{sin}{RESET}, {BLUE}Cosseno{RESET} {GREEN}={RESET} {YELLOW}{cos}{RESET}, {BLUE}Tangente{RESET} {GREEN}={RESET} {YELLOW}{tan}{RESET}\n")


#Esta função vai mostrar a Formúla Fundamental da Trigonometria (FFT): sin²(x) + cos²(x) = 1
def fft(var):
    fft = sp.sin(var)**2 + sp.cos(var)**2
    return fft


#Esta função vai calcular o seno através da FFT usando a tangente ou o cosseno
def sin(method, var):
    if method == 'tan':
        sin = sp.sqrt(sp.tan(var)**2 / (1 + sp.tan(var)**2))

    else:
        sin = 1 - sp.cos(var)**2
    return sin


#Esta função vai calcular o cosseno através da FFT usando a tangente ou o cosseno
def cos(method, var):
    if method == 'tan':
        cos = sp.sqrt(1 / (1 + sp.tan(var)**2))

    else:
        cos = 1 - sp.sin(var)**2
    return cos


#Esta função vai calcular a tangente
def tan(var):
    tan = sp.sin(var) / sp.cos(var)
    return tan


#Função para validações
def valid_answer(message, valid_options = None, numeric = False):
    while True:
        entry = input(f"{GREEN}{message}{RESET}").lower()

        if entry.strip() == "":
            print(f"{RED}Valor inválido, Introduza um valor válido{RESET}\n")
            continue

        if valid_options is not None:

            if entry.strip() in valid_options:
                return entry.strip()
            
            else:
                print(f"{RED}Valor inválido. Escolhe entre: {', '.join(valid_options)}{RESET}\n")
                continue

        try:
            value = sp.sympify(entry)

            if numeric and not value.is_number:
                print(f"{RED}Valor inválido, Introduza um número{RESET}\n")
                continue

            return value
        
        except (sp.SympifyError, TypeError):
            print(f"{RED}Valor inválido, Introduza um valor válido{RESET}\n")




#Função principal que vai correr todas as operações
def geometry_trigonometry():
    Operations = {
        "1": ("area", area ),
        "2": ("Teorema de Pitágoras", pitagoras ),
        "3": ("SOHCAHTOA", sohcahtoa ),
        "4": ("Formúla Fundamental da Trigonoteria (FFT)", fft  ),
        "5": ("Calculo do Seno através da FFT", sin ),
        "6": ("Calculo do Cosseno através da FFT", cos ),
        "7": ("Calculo da Tangente", tan )
    }

    while True:
        print(f"{YELLOW}Escolhe uma operação das seguintes:{RESET}")

        for key, (name, _) in Operations.items():
            print(f"{GREEN}{key} - {name}{RESET}")

        option = input(f"{GREEN}Opção: {RESET}")

        if option not in Operations:
            print(f"{RED}Opção inválida.{RESET}\n")
            continue

        name, operation_angles = Operations[option]

        if option == "1":
            geometric_figure = valid_answer("Introduza figura geometrica que quer calcular (quadrado, retangulo, triangulo, circulo): ",
                                            ["quadrado", "retangulo", "triangulo", "circulo"], False)
            base = valid_answer("Introduza o valor da base (b): ", None, True)
            height = valid_answer("Introduza o valor da altura (h), pode não ser usada: ", None, True)
            print(f"{BLUE}{name}:{RESET} {YELLOW}{area(geometric_figure, base, height)}{RESET}\n")

        elif option == "2":
            a_value = valid_answer("Introduza o valor de um cateto: ", None, True)
            b_value = valid_answer("Introduza o valor de outro cateto: ", None, True)
            print(f"{BLUE}{name}:{RESET} {YELLOW}{pitagoras(a_value, b_value)}{RESET}\n")
        
        elif option == "3":
            adjacent_value = valid_answer("Introduza o valor do cateto adjacente: ", None, True)
            opposite_value = valid_answer("Introduza o valor do cateto oposto: ", None, True)
            hipotenuse_value = valid_answer("Introduza o valor da hipotenusa: ", None, True)
            sohcahtoa(adjacent_value, opposite_value, hipotenuse_value)

        elif option == "5":
            sin_method = valid_answer("Escolha o método que quer utilizar para calcular o Seno (pela tangente ou diretamente da FFT): ", 
                                  ["tan", "fft"], False)
            print(f"{BLUE}{name}:{RESET} {YELLOW}{sin(sin_method, x)}{RESET}\n")

        elif option == "6":
            cos_method = valid_answer("Escolha o método que quer utilizar para calcular o Cosseno (pela tangente ou diretamente da FFT): ", 
                                  ["tan", "fft"], False)
            print(f"{BLUE}{name}:{RESET} {YELLOW}{cos(cos_method, x)}{RESET}\n")

        else:
            print(f"{BLUE}{name}:{RESET} {YELLOW}{operation_angles(x)}{RESET}\n")  

        new_operation = input(f"{GREEN}Clique 'Enter' para fazer outra operação: {RESET}")

        while new_operation != "":
            new_operation = input(f"{GREEN}Clique 'Enter' para fazer outra operação: {RESET}")     
            

if __name__ == '__main__':
    geometry_trigonometry()