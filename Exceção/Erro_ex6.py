class Leitor_de_arquivo:
    def __init__(self, caminho_arquivo):
        self.caminho_arquivo = caminho_arquivo

    def ler_arquivo(self):
        arquivo = None

        try:
            arquivo = open(self.caminho_arquivo, 'r', encoding='utf-8')
            conteudo = arquivo.read()
            print("Conteúdo do arquivo: ")
            print(conteudo)

        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.caminho_arquivo}' não foi encontrado.")

        except Exception as e:
            print(f"Ocorreu um erro ao ler o arquivo: {e}")

        finally:
            if arquivo:
                arquivo.close()
                print("Arquivo fechado com sucesso.")


if __name__ == "__main__":
    leitor = Leitor_de_arquivo("exemplo.txt")
    leitor.ler_arquivo()