from Geometry_and_trigonometry import geometry_trigonometry as gt
from Probability_and_Combinatorics import probability_and_combinatorics as pc
from Sequences_Series import sequences_series as s
from Calculus import calculus as calc
from ComplexNumbers import complex_numbers as cn


YELLOW = "\033[93m"
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"





#Aqui irá ser feito o método para escolher que tipo de matéria queremos estudar
def math():
    Files = {
        "1": ("Geometria e Trigonometria", gt),
        "2": ("Probabilidades e Combinatória", pc),
        "3": ("Sucessões e Séries", s),
        "4": ("Calculus", calc ),
        "5": ("Números Complexos", cn ),

    }

    while True:
        print(f"{YELLOW}Escolhe um dos métodos seguintes:{RESET}")

        for key, (name, _) in Files.items():
            print(f"{GREEN}{key} - {name}{RESET}")

        option = input(f"{GREEN}Opção: {RESET}\n")

        if option not in Files:
            print(f"{RED}Opção inválida.{RESET}\n")
            continue

        name, files_math = Files[option]
        files_math()

        
if __name__ == "__main__":
    math()



