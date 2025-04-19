class ProdutoNaoEncontradoError(Exception):
    def __init__(self, produto):
        super().__init__(f"O produto '{produto}' não foi encontrado na loja.")

class Loja:
    def __init__(self, nome:str):
        self.nome = nome
        self.produtos = []

    def adicionar_produto(self, produto:str):
        self.produtos.append(produto)
        print(f"Produto '{produto}' adicionado com sucesso.")

    def remover_produto(self, produto:str):
        try:
            self.produtos.remove(produto)
            print(f"Produto '{produto}' removido com sucesso.")

        except ValueError:
            raise ProdutoNaoEncontradoError(produto)
        
    def listar_produtos(self):
        if not self.produtos:
            print("A loja está sem produtos no momento.")

        else:
            print(f"Produtos disponíveis na loja '{self.nome}':")
            for i, produto in enumerate(self.produtos, start=1):
                print(f"{i}. {produto}")


if __name__ == "__main__":
    minha_loja = Loja("Carrefour")

    try:
        minha_loja.adicionar_produto("Picanha")
        minha_loja.adicionar_produto("Azeite de Oliva")
        minha_loja.listar_produtos()

        minha_loja.remover_produto("Picanha")
        minha_loja.remover_produto("Filé de Tilápia")

    except ProdutoNaoEncontradoError as e:
        print(f"Erro: {e}")

    finally:
        minha_loja.listar_produtos()