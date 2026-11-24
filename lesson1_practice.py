raw_ticket = "  TICKET-409 | P1 | Redis cache memory at 98%  "

# TODO 1: Clean raw_ticket using .strip() and split it by " | " into a list called `fields`
fields=raw_ticket.strip().split("|")
print(fields)




# TODO 2: Create a dictionary called `ticket_data` with keys:
# "ticket_id", "priority", and "issue" using items from `fields`
ticket_data = {
    "ticket_id": fields[0].strip(),
    "priority": fields[1].strip(),
    "issue": fields[2].strip()

}
print(ticket_data)

# TODO 3: Print an f-string alert like:
# "Urgent P1 Ticket TICKET-409: Redis cache memory at 98%"
print(f"Urgent {ticket_data['priority']} Ticket {ticket_data['ticket_id']} {ticket_data['issue']})")