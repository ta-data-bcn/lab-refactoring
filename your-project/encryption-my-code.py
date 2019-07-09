import functionsenc as fe
import dicts_func as df

choice = input('Type 0 to encrypt or 1 to decrypt: ')
text = fe.intext(fe.enc_or_dec(choice))

if choice == '0':
    df.encrypt(text)
else:
    df.decrypt(text)
