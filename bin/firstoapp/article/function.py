import re

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