def menor_e_maior(seq):
    if len(seq) == 1:
        return seq[0], seq[0]
    else:
        meio = len(seq) // 2
        menor_esq, maior_esq = menor_e_maior(seq[:meio])
        menor_dir, maior_dir = menor_e_maior(seq[meio:])
        return min(menor_esq, menor_dir), max(maior_esq, maior_dir)

sequencia = [1, 12, 34, 8, 313, 64]

menor, maior = menor_e_maior(sequencia)
print(f"O menor valor é {menor} e o maior valor é {maior}.")
