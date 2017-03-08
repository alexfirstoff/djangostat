import re
import pandas as pd
import pymorphy2


def req_voc (set_keys):
    word ={}
    set_keys1 = set_keys.splitlines()
    for t in set_keys1:
        k = t.split()
        for key in k:
            if key in word:
                value = word[key][0]
                word[key][0] = value + 1
            else:
                word[key] = [1]
    db = pd.DataFrame(word)
    db = db.T
    db = db.sort_values(0, ascending=False)
    line = ''
    for i in range (len(db)):
        t = db.iloc[i]
        line += str(t.name) + '-' + str(t[0]) + '\n'
    set_keys1 = line.splitlines()
    return '\n'.join(set_keys1)


def set_group (set_keys,keys_keys ,nclick):
    word = {}
    set_keys1 = set_keys.splitlines()
    what_keys = keys_keys.splitlines()
    nclick1 = nclick.splitlines()
    i = 0
    done_keys = ''
    for p in set_keys1:
        claster = ''
        for t in what_keys:
            if p.find(t) != -1:
                claster += t
                claster += '|'
        if claster == '':
            claster ='-'

        done_keys += claster

        if claster in word:
            value = word[claster][0]
            word[claster][0] = int(value) + int(nclick1[i])
            word[claster][1] += 1
        else:
            word[claster]=[int(nclick1[i]),1]
        i += 1
        done_keys += '\n'
    set_keys1 = done_keys.splitlines()
    done_keys = ''
    done = ''
    for r in set_keys1:
        done = r + " ; " + str(word[r][0]) + "/" + str(str(word[r][1]))
        done_keys += done
        done_keys += '\n'


    db = pd.DataFrame(word)
    db = db.T
    db = db.sort_values(0, ascending=False)
    line = ''
    for i in range(len(db)):
        t = db.iloc[i]
        line += str(t.name) + '-' + str(t[0]) + '-'+ str(t[1]) +'\n'


    set_keys2 = line.splitlines()




    set_keys1 = done_keys.splitlines()
    return ['\n'.join(set_keys1),'\n'.join(set_keys2)]



def b_replacer (where, what, onwhat):
    set_keys1 = where.splitlines()
    what_keys = what.splitlines()
    onwhat = onwhat.splitlines()
    done_keys_keys=''
    i = 0
    for t in what_keys:
        done_keys_keys = ''
        for p in set_keys1:
            try:
                if onwhat[i] == '-':
                    onwt = ''
                else:
                    onwt = onwhat[i]
                p = p.replace(t, onwt)
            except:
                p = p

            done_keys_keys += p
            done_keys_keys += '\n'
        set_keys1 = done_keys_keys.splitlines()
        i += 1

    return '\n'.join(set_keys1)

def keys_33 (where, n):
    set_keys1 = where.splitlines()
    final = ''
    for t in set_keys1:
        if len(t) > n:
            final += t
            final += '\n'

    return final

def b_replacer_33 (where, what, onwhat):
    set_keys1 = where.splitlines()
    what_keys = what.splitlines()
    onwhat = onwhat.splitlines()

    i = 0
    for t in what_keys:
        done_keys_keys = ''
        for p in set_keys1:
            if len(p) > 33:
                if onwhat[i] == '-':
                    onwt = ''
                else:
                    onwt = onwhat[i]
                try:
                    p = p.replace(t, onwt)
                except:
                    p = p
            else:
                p = p
            done_keys_keys += p
            done_keys_keys += '\n'

        set_keys1 = done_keys_keys.splitlines()

        i += 1
    return '\n'.join(set_keys1)

def eng_capitalize (where):

    set_keys1 = where.splitlines()
    final = ''
    for t in set_keys1:
        if re.search(r'[A-Za-z]',t):
            ss = t.split()
            final_line = ''
            for p in ss:
                if re.search(r'[A-Za-z]',p):
                    p = p[0].upper() + p[1:]
                final_line += p
                final_line += ' '
            t = final_line

        final += t
        final += '\n'

    return final

def first_capitalize(where):
    set_keys1 = where.splitlines()
    final = ''
    for t in set_keys1:
        t = t[0].upper() + t[1:]
        t = t.replace('  ',' ')
        final += t.strip()
        final += '\n'

    return final