from itertools import product
import subprocess


class BruteForce(object):

    def __init__(self, callback, charset):

        self.__charset = charset
        self.__callback = callback
        self.__attempts = 0
        self.__found_password = ""


    @property
    def attempts(self):
        return self.__attempts
    

    @property
    def found_password(self):
        return self.__found_password


    def run(self, size = [1, 5], stop_function = None):

        """
        Inicializa a execução do Brute Force.

        @param size: Lista com o tamanho mínimo e máximo da senha.
        @param stop_function: Função para interromper a execução do Brute Force.
        """

        self.__attempts = 0

        for length in range(size[0], size[1] + 1):

            # Obtém todas as combinações possíveis.
            password_list = product(self.__charset, repeat = length)

            # Percorre as combinações.
            for password in password_list:

                self.__attempts += 1
                password = "".join(password)

                # Verifica se a senha está correta.
                if self.__callback(password):
                    self.__found_password = password
                    return True

                # Verifica se o usuário pediu para parar.
                if callable(stop_function) and stop_function(password):
                    return False
                    
        return False



