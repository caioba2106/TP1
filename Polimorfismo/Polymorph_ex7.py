class Arquivo:

    def abrir(self):
        raise NotImplementedError("Este método deve ser implementado pelas subclasses.")
    
class ArquivoTexto(Arquivo):

    def abrir(self):
        print("Abrindo arquivo de texto no editor padrão... ")

class ArquivoImagem(Arquivo):

    def abrir(self):
        print("Exibindo imagem na galeria de fotos... ")

class ArquivoVideo(Arquivo):

    def abrir(self):
        print("Reproduzindo vídeo no player de mídia... ")


arquivos = [ArquivoTexto(), ArquivoImagem(), ArquivoVideo()]

for arquivo in arquivos:
    arquivo.abrir()