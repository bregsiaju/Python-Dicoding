import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-n', '--nama', required=True, help="Masukkan nama Anda")
args = parser.parse_args()

print("Terima kasih telah menggunakan panggildicoding.py, "+args.nama)