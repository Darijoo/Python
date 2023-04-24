rente_per_jaar = 0.0012
beginbedrag = float(input("Hoeveel is het bedrag datje bij het begin van het jaar op je rekening hebt gezet?"))
bedrag_jaar_1 = round((beginbedrag + beginbedrag * rente_per_jaar), 2)
bedrag_jaar_2 = round((bedrag_jaar_1 + bedrag_jaar_1 * rente_per_jaar),2)
bedrag_jaar_3 = round((bedrag_jaar_2 + bedrag_jaar_2 * rente_per_jaar),2)
print(f"Na 1 jaar: {bedrag_jaar_1}\nNa 2 jaar: {bedrag_jaar_2}\nNa 3 jaar: {bedrag_jaar_3}\n")