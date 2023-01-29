print("Hva er ditt navn?") #spør om navnet
navn = input() #input for svar
print("Hva er din adresse?") #spør om gateadresse
gate = input() #input for svar
print("Hva er ditt postnummer og poststed?") #spør om postkode og sted
post = input() #input for svar

#sjekker lengden av input
navn_len = len(navn)
gate_len = len(gate)
post_len = len(post)

#skriver ut den lengste av input
print(max(int(navn_len),int(gate_len),int(post_len)))