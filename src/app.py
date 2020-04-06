from src.arg_parser import ArgParser
from src.brute.brute_force import BruteForce
from src.brute.charset import *
import keyboard
import os


class App(object):
    
    """
    Classe principal
    """

    def __init__(self, attempt_function, err_callback, data_dir = "data", description = "", key_to_stop = "q"):
        
        """
        @param attempt_function: Função para receber uma senha e verificar se ela é válida.
        @param err_callback: Função para receber uma mensagem de erro.
        @param data_dir: Diretório onde os arquivos referentes a configurações e outros serão guardados.
        @param description: Descrição do programa.
        @param key_to_stop: Tecla para interromper a execução do BruteForce.
        """
        
        # Obtém os argumentos passados para o programa.
        parser = ArgParser(description, data_dir)
        self.__args = parser.parse_args()
        
        # Valida os argumentos.
        parser.validate_args(self.__args, err_callback)

        # Verifica se o diretório de data_dir existe. Se não existir, ele será criado.
        if not os.path.exists(data_dir):
            os.mkdir(data_dir)

        # Verifica se o arquivo charset existe. Se não existir, ele será criado.
        if not os.path.exists(self.__args.charset):
            self.create_charset_file()

        # Obtém o charset.
        self.__charset = get_charset_from_file(self.__args.charset, self.__args.excludes.split(","))

        # Interrompe a execução do Brute Force ao pressionar uma tecla.
        keyboard.on_press_key(key_to_stop, self.stop_brute_force)

        # Cria uma instância de BruteForce.
        self.__bruteForce = BruteForce(attempt_function, self.__charset)


    @property
    def args(self):
        return self.__args
    
    
    @property
    def bruteForce(self):
        return self.__bruteForce


    def create_charset_file(self):

        """
        Cria um arquivo charset.
        """

        range_ = Range(self.__args.range)
        chars = get_charset_from_range(range_)

        with open(self.__args.charset, "w") as file:
            file.write("".join(chars))


    def run_brute_force(self):

        """
        Inicializa o Brute Force.
        """

        self.__stop = False
        self.__bruteForce.run([self.__args.min, self.__args.max], stop_function = lambda *args: self.__stop)

    
    def stop_brute_force(self, *args):

        """
        Interrompe a execução do Brute Force.
        """

        self.__stop = True
