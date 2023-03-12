# external counts
cant_convert_count = 0
blacklist_count = 0

# ["flagged", "date", "description", "name', "from", "to", "cc", "subject", "time (minutes)"]
def apply_rules(date, sent_name, sent_from, sent_to, cc, subject, contents, owners, blacklist_domains):
    return [
        date,
        "",
	sent_name,
        ", ".join(sent_from),
        ", ".join(sent_to),
        ", ".join(cc),
        subject,
        "0"
    ]
