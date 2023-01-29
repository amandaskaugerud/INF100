# definerer en funksjon
def human_to_dog_years(humanYear):
    # gjør det mulig at den tar inn float slik at man kan skrive halve år
    humanYear = float(humanYear)
    # sjekker om årene som er oppgitt er mindre eller lik 2 pga krav om at 
    # de første to årene skal regnes som 10,5 hundeår
    if humanYear <= 2:
        return humanYear*10.5
    # beregner menneskeår til hundeår for mer enn 2
    else:
        # trekker fra marginen på 2 år som skulle regnes annerledes
        dogBeginning = 2 * 10.5
        # trekker fra marginen brukt de to første årene
        humanYear = humanYear-2
        # beregner de resterende menneskeårene til hundeår på vanlig måte
        # og legger på de to første annerledes årene
        dogYear = (humanYear*4) + dogBeginning
        return dogYear
