class Donor:
    def __init__(self, donor_id, name, blood_type, organs):
        self.donor_id = donor_id
        self.name = name
        self.blood_type = blood_type
        self.organs = organs

class Recipient:
    def __init__(self, recipient_id, name, blood_type, organ_needed):
        self.recipient_id = recipient_id
        self.name = name
        self.blood_type = blood_type
        self.organ_needed = organ_needed

class OrganDonationSystem:
    def __init__(self):
        self.donors = {}
        self.recipients = {}
        self.matches = []
        self.next_donor_id = 1
        self.next_recipient_id = 1

    def add_donor(self, name, blood_type, organs):
        donor_id = self.next_donor_id
        self.donors[donor_id] = Donor(donor_id, name, blood_type, organs)
        self.next_donor_id += 1
        print(f"Donor added: {name}, Blood Type: {blood_type}, Organs: {organs}")

    def add_recipient(self, name, blood_type, organ_needed):
        recipient_id = self.next_recipient_id
        self.recipients[recipient_id] = Recipient(recipient_id, name, blood_type, organ_needed)
        self.next_recipient_id += 1
        print(f"Recipient added: {name}, Blood Type: {blood_type}, Organ Needed: {organ_needed}")

    def match_donors_recipients(self):
        for donor_id, donor in self.donors.items():
            for recipient_id, recipient in self.recipients.items():
                if donor.blood_type == recipient.blood_type and recipient.organ_needed in donor.organs:
                    match = {
                        'donor_id': donor_id,
                        'recipient_id': recipient_id,
                        'organ': recipient.organ_needed
                    }
                    self.matches.append(match)
                    donor.organs.remove(recipient.organ_needed)
                    print(f"Match found: Donor {donor.name} -> Recipient {recipient.name} for Organ: {recipient.organ_needed}")

    def view_matches(self):
        if not self.matches:
            print("No matches found.")
            return

        for match in self.matches:
            donor = self.donors[match['donor_id']]
            recipient = self.recipients[match['recipient_id']]
            print(f"Match: Donor {donor.name} -> Recipient {recipient.name} for Organ: {match['organ']}")

# Example usage
if __name__ == "__main__":
    system = OrganDonationSystem()
    
    # Add donors
    system.add_donor("John Doe", "O+", ["Kidney", "Liver"])
    system.add_donor("Jane Smith", "A+", ["Heart", "Lung"])
    
    # Add recipients
    system.add_recipient("Alice Johnson", "O+", "Kidney")
    system.add_recipient("Bob Brown", "A+", "Heart")
    
    # Match donors with recipients
    system.match_donors_recipients()
    
    # View matches
    system.view_matches()

