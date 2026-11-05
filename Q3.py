akumulasi_berat = 0

while True:
    akumulasi_berat += 5
    print(f"Total berat saat ini: {akumulasi_berat} kg")

    if akumulasi_berat >= 25:
        break

print("-" * 40)