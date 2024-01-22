
# funkcijas argumenti - ieejas
# funkcijas rezultāts - izeja
def summa(a, b):
    # parbauda vai argumenti ir skaitliskas vertibas:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    else:
        return "Saskaitāmie argumenti nav skaitliskas vērtības"


