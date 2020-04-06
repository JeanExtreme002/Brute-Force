import os


def main(command, password):

    """
    Função para verificar uma senha e retornar um código.

    OBS: Essa função pode ser escrita sem problema algum,
    contanto que retorne sempre um código (número inteiro).
    """

    cmd = command.format(password)
    code = os.system(cmd)
    return code
