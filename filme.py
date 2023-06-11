from time import sleep

class Filme:
    def __init__(self, titulo, diretor, genero, ano_lancamento):
        self.titulo = titulo
        self.diretor = diretor
        self.genero = genero
        self.ano_lancamento = ano_lancamento

    def imprimirNomeFilme(self):
        return self.titulo

catalogoDeFilmes = { 
    
    #chave    classe e informações dos filmes       
    'filme1': Filme('Rocky', 'John G. Avildsen', 'Drama', 1976),
    'filme2': Filme('Rocky II', 'Sylvester Stallone', 'Drama', 1979),
    'filme3': Filme('Rocky III', 'Sylvester Stallone', 'Drama', 1982),
    'filme4': Filme('Rocky IV', 'Sylvester Stallone', 'Drama', 1985),
    'filme5': Filme('Rocky V', 'John G. Avildsen', 'Drama', 1990),
    'filme6': Filme('Rocky Balboa', 'Sylvester Stallone', 'Drama', 2006),
    'filme7': Filme('Creed', 'Ryan Coogler', 'Drama', 2015),
    'filme8': Filme('Creed II', 'Steven Caple Jr.', 'Drama', 2018),
}
for chave in catalogoDeFilmes:
    filme = catalogoDeFilmes[chave]
    sleep(0.4)
    print(filme.titulo)
sleep(1.5)
print('Fim do programa!!')


def editarFilmes(catalogo, titulo):
    if:
    else:
        