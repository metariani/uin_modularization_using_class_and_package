nama = 'meta riani ananda'
program = 'dinamika rotasi'

print(f'program {program} oleh {nama}')

def hitung_usaha(jarak, gaya):
    return jarak * gaya

jarak = 5
gaya = 20
usaha = hitung_usaha(jarak , gaya)

print(f'jarak = {jarak/5}m dengan gaya = {gaya/20}N')
print(f'sehingga usaha = {usaha} joule')