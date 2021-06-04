import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama Anda")
parser.add_argument('-t', "--tahunlahir", required=True, help="Masukkan tahun tahir Anda (YYYY)")
args = parser.parse_args()

if args.tahunlahir <= '1990':
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2020, bapak "+args.nama)
else:
    print("Terima kasih telah menggunakan panggildicoding.py pada tahun 2020, kakak "+args.nama)