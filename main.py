import os


def main():

    os.chdir('./')
    name_file_accept = 'setenceaccepted.txt'
    name_file_reject = 'setencereject.txt'

    alphabet = input('Alfabeto (ex: x,y,z): ').split(',')
    prefix, sub_string, sufix = map(lambda x: tuple(x.split(',')),
                                    input('prefixo;subpalavra;sufixo (ex: 11,22;3,4;22,33): ').split(';'))

    lenght_str = int(input('Tamanho das sentença: '))

    combi = generate_combinations(alphabet, lenght_str)

    file_accept = open(name_file_accept, 'w+')
    file_rejec = open(name_file_reject, 'w+')

    for sentence in combi:
        rs = has_tokens(sentence, prefix, sub_string, sufix)
        if rs:
            file_accept.write(sentence + '\n')
        else:
            file_rejec.write(sentence + '\n')

    file_accept.close()
    file_rejec.close()

    print('Salvo!')


def generate_combinations(symbols, lenght):

    gen_arr, str_obj = [], [0] * lenght

    while str_obj[0] < len(symbols):
        gen_arr.append(''.join(list(map(lambda x: symbols[x], str_obj))))

        str_obj[lenght - 1] += 1
        if (str_obj[lenght - 1] >= len(symbols)):
            j = lenght - 2
            str_obj[lenght - 1], str_obj[j] = 0, str_obj[j] + 1

            while j > 0 and str_obj[j] >= len(symbols):
                str_obj[j] = 0
                str_obj[j - 1] += 1
                j -= 1

    return gen_arr


def has_tokens(sentence, prefixs, sub_strs, sufixs):

    if not(sentence.startswith(prefixs) and sentence.endswith(sufixs)):
        return False

    status, i = False, 0
    while i < len(sub_strs) and not(status):
        if sub_strs[i] in sentence:
            status = True
        i += 1

    return status


if __name__ == '__main__':
    main()
