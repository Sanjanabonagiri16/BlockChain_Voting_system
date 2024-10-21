class Transaction:
    def __init__(self, voter_id, candidate_id):
        self.voter_id = voter_id
        self.candidate_id = candidate_id

    def to_dict(self):
        return {
            "voter_id": self.voter_id,
            "candidate_id": self.candidate_id
        }