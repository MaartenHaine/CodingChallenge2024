"""
Tijdens de opkomst van industriële revoluties en wereldwijde conflicten, proberen spionnen gecodeerde berichten
te infiltreren in de geheime netwerken van naties. Om deze dreiging tegen te gaan, moet je om berichten te valideren
voordat ze worden verzonden.

Jij bent verantwoordelijk voor het schrijven van een één-regelige inputvalidatie die elk bericht controleert.
Deze validatie moet ervoor zorgen dat er geen geheime of gecodeerde informatie in vijandige handen valt.

Vereisten:
    Het bericht mag niet langer zijn dan 256 tekens.
    Alleen alfanumerieke tekens en de volgende leestekens zijn toegestaan: . , ! ? ; :.
    Het bericht mag geen lange numerieke reeksen (meer dan 10 cijfers) bevatten.
"""

def validate(message: str) -> bool:
    return False