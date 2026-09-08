from app.models.ticket import TicketAnalysis, TicketRequest

def analyze_ticket(ticket: TicketRequest) -> TicketAnalysis:
    return TicketAnalysis(
        category= "NETWORK",
        priority= "HIGH",
        summary= "Problème de connexion Wifi"
    )