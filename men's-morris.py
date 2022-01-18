#99087 Joao Barbosa


def cria_posicao(c, l):
    """
    recebe a coluna e linha e devolve uma posicao criada
    """
    if not c == 'a' and not c == 'b' and not c == 'c' or not l == '1' and not l == '2' and not l == '3':
        raise ValueError('cria_posicao: argumentos invalidos')
    return [c, l]


def cria_copia_posicao(p):
    """
    recebe uma posicao e cria uma copia da mesma
    """
    x = p
    return x


def obter_pos_c(p):
    """
    recebe uma posicao e devolve a sua coluna
    """
    return str(p[0])


def obter_pos_l(p):
    """
    recebe uma posicao e devolve a sua linha
    """
    return str(p[1])


def eh_posicao(arg):
    """
    recebe uma posicao e verifica a sua validade
    """
    return isinstance(arg, list) and len(arg) == 2 and (arg[0] == 'a' or arg[0] == 'b' or arg[0] == 'c')\
            and (arg[1] == '1' or arg[1] == '2' or arg[1] == '3')


def posicoes_iguais(p1, p2):
    """
    recebe duas posicoes e verifica se sao iguais
    """
    return eh_posicao(p1) and eh_posicao(p2) and p1 == p2


def posicao_para_str(p):
    """
    recebe uma posicao e devolve a mesma em string
    """
    return str(obter_pos_c(p)) + str(obter_pos_l(p))


def ordena_posicoes(t):
    """
    recebe um tuplo de posicoes e devolve o tuplo ordenado
    """
    res = ()
    for i in ('a1', 'b1', 'c1', 'a2', 'b2', 'c2', 'a3', 'b3', 'c3'):
        if i in t:
            res += i,
    return res


def obter_posicoes_adjacentes(p):
    """
    recebe uma posicao e devolve um tuplo com as posicoes adjacentes
    """
    if obter_pos_c(p) == 'a' or obter_pos_c(p) == 'c':
        if obter_pos_l(p) == '1':
            return ordena_posicoes((posicao_para_str(cria_posicao('b', obter_pos_l(p))),
                                    posicao_para_str(cria_posicao(obter_pos_c(p), '2')), 'b2'))
        if obter_pos_l(p) == '2':
            return (posicao_para_str(cria_posicao(obter_pos_c(p), '1')),
                    posicao_para_str(cria_posicao('b', obter_pos_l(p))),
                    posicao_para_str(cria_posicao(obter_pos_c(p), '3')))
        if obter_pos_l(p) == '3':
            return ordena_posicoes((posicao_para_str(cria_posicao(obter_pos_c(p), '2')),
                                   posicao_para_str(cria_posicao('b', obter_pos_l(p))), 'b2'))
    else:
        if obter_pos_l(p) == '1':
            return (posicao_para_str(cria_posicao('a', obter_pos_l(p))),
                    posicao_para_str(cria_posicao('c', obter_pos_l(p))),
                    posicao_para_str(cria_posicao(obter_pos_c(p), '2')))
        if obter_pos_l(p) == '2':
            return 'a1', 'b1', 'c1', 'a2', 'c2', 'a3', 'b3', 'c3'
        if obter_pos_l(p) == '3':
            return (posicao_para_str(cria_posicao(obter_pos_c(p), '2')),
                    posicao_para_str(cria_posicao('a', obter_pos_l(p))),
                    posicao_para_str(cria_posicao('c', obter_pos_l(p))))


def cria_peca(s):
    """
    recebe uma peca e devolve numa lista
    """
    if not s == 'X' and not s == ' ' and not s == 'O':
        raise ValueError('cria_peca: argumento invalido')
    return [s]


def cria_copia_peca(j):
    """
    recebe uma peca e devolve uma copia
    """
    x = j
    return x


def eh_peca(arg):
    """
    recebe uma peca e verifica a sua validade
    """
    return isinstance(arg, list) and (arg[0] == 'X' or arg[0] == 'O' or arg[0] == ' ')


def pecas_iguais(j1, j2):
    """
    recebe duas pecas e verifica se sao iguais
    """
    return eh_peca(j1) and eh_peca(j2) and j1 == j2


def peca_para_str(j):
    """
    recebe uma peca e devolve em string
    """
    return '[' + j[0] + ']'


def peca_para_inteiro(j):
    """
    recebe uma peca e devolve a mesma representada em inteiro
    """
    if j[0] == 'X':
        return 1
    if j[0] == 'O':
        return -1
    if j[0] == ' ':
        return 0


def cria_tabuleiro():
    """
    cria um tabuleiro de posicoes livre
    """
    return [[cria_peca(' '), cria_peca(' '), cria_peca(' ')], [cria_peca(' '),
            cria_peca(' '), cria_peca(' ')], [cria_peca(' '), cria_peca(' '),
            cria_peca(' ')]]


def cria_copia_tabuleiro(t):
    """
    recebe um tabuleiro e devolve uma copia
    """
    new_t = []
    for i in t:
        for x in i:
            new_t += cria_copia_peca(x),
    return [new_t[0:3], new_t[3:6], new_t[6:9]]


def letra_para_int(s):
    """
    recebe um uma coluna (letra) e devolve em inteiro
    """
    if s == 'a':
        return 1
    if s == 'b':
        return 2
    if s == 'c':
        return 3


def obter_peca(t, p):
    """
    recebe um tabuleiro e uma posicao e devolve a peca em causa
    """
    if p[1] == '1':
        return t[0][letra_para_int(p[0]) - 1]
    if p[1] == '2':
        return t[1][letra_para_int(p[0]) - 1]
    if p[1] == '3':
        return t[2][letra_para_int(p[0]) - 1]


def obter_vetor(t, s):
    """
    recebe um tabuleiro e uma coluna ou linha, e devolve um tuplo da mesm ou mesma
    """
    if s == 'a' or s == 'b' or s == 'c':
        return t[0][letra_para_int(s) - 1], t[1][letra_para_int(s) - 1], t[2][letra_para_int(s) - 1]
    if s == '1':
        return tuple(t[0])
    if s == '2':
        return tuple(t[1])
    if s == '3':
        return tuple(t[2])


def coloca_peca(t, j, p):
    """
    recebe um tabuleiro, uma peca e uma posicao e devolve o tabuleiro com a peca colocada
    """
    t[int(p[1]) - 1][letra_para_int(p[0]) - 1] = j
    return t


def remove_peca(t, p):
    """
    recebe um tabuleiro e uma posicao e devolve um tabuleiro com a peca dessa posicao removida
    """
    return coloca_peca(t, [' '], p)


def move_peca(t, p1, p2):
    """
    recebe um tabuleiro e duas posicoes e devolve um tabuleiro com a peca movida de p1 para p2
    """
    coloca_peca(t, obter_peca(t, p1), p2)
    remove_peca(t, p1)
    return t


def eh_tabuleiro(arg):
    """
    recebe um tabuleiro e verifica a sua validade
    """
    res1, res2 = 0, 0
    if not isinstance(arg, list) or not len(arg) == 3:
        return False
    for i in arg:
        if not isinstance(i, list) or not len(i) == 3:
            return False
        for x in i:
            if not eh_peca(x):
                return False
            if x[0] == 'X':
                res1 += 1
            if x[0] == 'O':
                res2 += 1
    if res1 > 3 or res2 > 3 or res1 > res2 + 1 or  res2 > res1 + 1:
        return False
    if res1 == res2 == 3:
        for i in 'abc':
            for x in 'abc':
                if obter_vetor(arg, x) == (['X'], ['X'], ['X']):
                    if obter_vetor(arg, i) == (['O'], ['O'], ['O']):
                        return False
                if obter_vetor(arg, str(letra_para_int(x))) == (['X'], ['X'], ['X']):
                    if obter_vetor(arg, str(letra_para_int(i))) == (['O'], ['O'], ['O']):
                        return False
    return True


def eh_posicao_livre(t, p):
    """
    recebe um tabuleiro e uma posicao e verifica se e livre
    """
    if obter_peca(t, p)[0] != ' ':
        return False
    return True


def tabuleiros_iguais(t1, t2):
    """
    recebe dois tabuleiros e verifica se sao iguais
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and t1 == t2


def tabuleiro_para_str(t):
    """
    recebe um tabuleiro e devolve a sua representacao em string
    """
    return '   a   b   c\n1 ' + peca_para_str(t[0][0]) + '-' + peca_para_str(t[0][1]) + '-' + peca_para_str(t[0][2])\
        + '\n   | \ | / |\n2 ' + peca_para_str(t[1][0]) + '-' + peca_para_str(t[1][1]) + '-' + peca_para_str(t[1][2])\
        + '\n   | / | \ |\n3 ' + peca_para_str(t[2][0]) + '-' + peca_para_str(t[2][1]) + '-' + peca_para_str(t[2][2])


def inteiro_para_peca(i):
    """
    recebe um inteiro e devolve a peca que o representa
    """
    if i == 1:
        return ['X']
    if i == -1:
        return ['O']
    if i == 0:
        return [' ']


def tuplo_para_tabuleiro(t):
    """
    recebe um tuplo e devolve um tabuleiro
    """
    res = list(t[0]) + list(t[1]) + list(t[2])
    res1 = []
    for i in res:
        res1 += inteiro_para_peca(i),
    return [list(res1[0:3]), list(res1[3:6]), list(res1[6:9])]


def obter_ganhador(t):
    """
    recebe um tabuleiro e devolve, se houver, a peca do ganhador
    """
    for i in 'abc':
        if obter_vetor(t, i) == (['X'], ['X'], ['X']):
            return ['X']
        if obter_vetor(t, str(letra_para_int(i))) == (['X'], ['X'], ['X']):
            return ['X']
        if obter_vetor(t, i) == (['O'], ['O'], ['O']):
            return ['O']
        if obter_vetor(t, str(letra_para_int(i))) == (['O'], ['O'], ['O']):
            return ['O']
    else:
        return [' ']


def obter_posicoes_livres(t):
    """
    recebe um tabuleiro e devolve um tuplo com as posicoes livres
    """
    res = ()
    for i in 'abc':
        for x in range(1, 4):
            if eh_posicao_livre(t, i + str(x)):
                res += (i + str(x),)
    return ordena_posicoes(res)


def obter_posicoes_jogador(t, j):
    """
    recebe um tabuleiro e devolve um tuplo com as posicoes do jogador
    """
    res = ()
    for i in 'abc':
        for x in range(1, 4):
            if obter_peca(t, i + str(x)) == j:
                res += (i + str(x),)
    return ordena_posicoes(res)


def obter_movimento_manual(t, j):
    """
    recebe um tabuleiro e a peca do jogador, devolve a posicao ou movimento inserido pelo jogador
    """
    res = ()
    res1 = ()
    if not eh_tabuleiro(t) or not eh_peca(j):
        raise ValueError('obter_movimento_manual: escolha invalida')
    for x in t:
        for i in x:
            if i == j:
                res += i,
    if len(res) < 3:
        p = str(input('Turno do jogador. Escolha uma posicao: '))
        if not len(p) == 2 or not eh_tabuleiro(t) or not eh_peca(j) or not p[0] in 'abc' or not p[1] in '123'\
                or not eh_posicao_livre(t, p):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return p,
    if len(res) == 3:
        p = str(input('Turno do jogador. Escolha um movimento: '))
        for e in obter_posicoes_jogador(t, j):
            for z in obter_posicoes_adjacentes(e):
                if eh_posicao_livre(t, z):
                    res1 += z,
        if len(res1) == 0:
            if not len(p) == 4 or not p[0] in 'abc' or not p[1] in '123' or not p[0:2] == p[2:4]:
                raise ValueError('obter_movimento_manual: escolha invalida')
            return p[0:2], p[2:4]
        if not len(p) == 4 or not p[0] in 'abc' or not p[1] in '123' or not p[2] in 'abc' or not p[3] in '123' or not eh_posicao(cria_posicao(p[2], p[3]))\
                or not eh_posicao_livre(t, p[2:4]) or not obter_peca(t, p[0:2]) == j\
                or not p[2:4] in obter_posicoes_adjacentes(p[0:2]):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return p[0:2], p[2:4]


def vitoria(t, j):
    """
    recebe um tabuleiro e uma peca e devolve a posicao, se houver, para dar vitoria ao jogador
    """
    for i in 'abc':
        if obter_vetor(t, i) == (j, j, cria_peca(' ')):
            return i + '3'
        if obter_vetor(t, i) == (j, cria_peca(' '), j):
            return i + '2'
        if obter_vetor(t, i) == (cria_peca(' '), j, j):
            return i + '1'
        if obter_vetor(t, str(letra_para_int(i))) == (j, j, cria_peca(' ')):
            return 'c' + str(letra_para_int(i))
        if obter_vetor(t, str(letra_para_int(i))) == (j, cria_peca(' '), j):
            return 'b' + str(letra_para_int(i))
        if obter_vetor(t, str(letra_para_int(i))) == (cria_peca(' '), j, j):
            return 'a' + str(letra_para_int(i))
    return False


def bloqueio(t, j):
    """
    recebe um tabuleiro e uma peca e devolve uma posicao, se houver, para bloquear a vitoria do adversario
    """
    if j[0] == 'X':
        return vitoria(t, cria_peca('O'))
    if j[0] == 'O':
        return vitoria(t, cria_peca('X'))


def centro(t):
    """
    recebe um tabuleiro e devolve a posicao central caso livre
    """
    if eh_posicao_livre(t, 'b2'):
        return 'b2'
    return False


def canto_vazio(t):
    """
    recebe um tabuleiro e devolve a posicao de um dos cantos, caso livre
    """
    for p in ('a1', 'c1', 'a3', 'c3'):
        if eh_posicao_livre(t, p):
            return p
    return False


def lateral_vazio(t):
    """
    recebe um tabuleiro e devolve a posicao das laterais, caso livres
    """
    for p in ('b1', 'a2', 'c2', 'b3'):
        if eh_posicao_livre(t, p):
            return p
    return False


def estrategia(nivel):
    """
    recebe  um nivel e verifica a sua validade
    """
    if nivel != 'facil' and nivel != 'normal' and nivel != 'dificil':
        return False
    return True


def minimax(t, j, p, s):
    """
    recebe um tabuleiro, uma peca, uma profundidade e uma sequencia de movimentos e devolve um tuplo com a ou as
    melhores sequencias de movimentos a fazer
    """
    if pecas_iguais(obter_ganhador(t), cria_peca('X')) or pecas_iguais(obter_ganhador(t), cria_peca('O')) or p == 0:
        return peca_para_inteiro(obter_ganhador(t)), s
    else:
        best_res = -1 * peca_para_inteiro(j)
        best_s = ()
        for i in obter_posicoes_jogador(t, j):
            for x in obter_posicoes_adjacentes(i):
                if eh_posicao_livre(t, x):
                    new_t = cria_copia_tabuleiro(t)
                    move_peca(new_t, i, x)
                    new_s = (i, x)
                    new_best_res, new_s_res = minimax(new_t, inteiro_para_peca(-1 * peca_para_inteiro(j)),
                                                      p - 1, s + (new_s,))
                    if not len(best_s) or (pecas_iguais(j, cria_peca('X')) and new_best_res > best_res)\
                            or (pecas_iguais(j, cria_peca('O')) and new_best_res < best_res):
                        best_res, best_s = new_best_res, new_s_res
        return best_res, best_s


def obter_movimento_auto(t, j, nivel):
    """
    recebe um tabuleiro uma peca e um nivel e devolve a posicao ou movimento a usar de acordo com a situacao de jogo
    """
    if not eh_peca(j) or not eh_tabuleiro(t) or not estrategia(nivel):
        raise ValueError('escolher_posicao_auto: algum dos argumentos e invalido')
    res = ()
    for x in t:
        for i in x:
            if i == cria_peca(j[0]):
                res += i,
    if len(res) < 3:
        if vitoria(t, j):
            return vitoria(t, j),
        if bloqueio(t, j):
            return bloqueio(t, j),
        if centro(t):
            return centro(t),
        if canto_vazio(t):
            return canto_vazio(t),
        if lateral_vazio(t):
            return lateral_vazio(t),
    if len(res) == 3:
        if nivel == 'facil':
            for i in obter_posicoes_jogador(t, j):
                for x in obter_posicoes_adjacentes(i):
                    if eh_posicao_livre(t, x):
                        return i, x
            return i, i
        if nivel == 'normal':
            return minimax(t, j, 1, ())[1][0]
        if nivel == 'dificil':
            return minimax(t, j, 5, ())[1][0]


def moinho(j, nivel):
    """
    recebe uma peca e um nivel e devolve o jogo completo
    """
    if not estrategia(nivel) or not j == '[X]' and not j == '[O]':
        raise ValueError('moinho: argumentos invalidos')
    t = cria_tabuleiro()
    print("Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade " + nivel + ".")
    print(tabuleiro_para_str(t))
    while obter_ganhador(t) == [' ']:
        res = ()
        for x in t:
            for i in x:
                if i == cria_peca(j[1]):
                    res += i,
        if len(res) < 3:
            t = coloca_peca(t, cria_peca(j[1]), obter_movimento_manual(t, cria_peca(j[1]))[0])
            print(tabuleiro_para_str(t))
        if len(res) == 3:
            m = obter_movimento_manual(t, cria_peca(j[1]))
            if m[0] != m[1]:
                t = move_peca(t, m[0], m[1])
            print(tabuleiro_para_str(t))
        if obter_ganhador(t) == [j[1]]:
            return j
        print('Turno do computador (' + nivel + '):')
        if len(res) < 3:
            t = coloca_peca(t, inteiro_para_peca(-1 * peca_para_inteiro(cria_peca(j[1]))),
                            obter_movimento_auto(t, inteiro_para_peca(-1 * peca_para_inteiro(cria_peca(j[1]))),
                                                 nivel)[0])
            print(tabuleiro_para_str(t))
        if len(res) == 3:
            n = obter_movimento_auto(t, inteiro_para_peca(-1 * peca_para_inteiro(cria_peca(j[1]))), nivel)
            if n[0] != n[1]:
                t = move_peca(t, n[0], n[1])
            print(tabuleiro_para_str(t))
        if obter_ganhador(t) == inteiro_para_peca(-1 * peca_para_inteiro(cria_peca(j[1]))):
            return peca_para_str(inteiro_para_peca(-1 * peca_para_inteiro(cria_peca(j[1]))))
