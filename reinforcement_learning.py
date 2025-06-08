class ReinforcementLearningAgent:
    """Simple agent to prioritize payloads based on past success."""

    def __init__(self):
        self.payload_stats = {}

    def learn(self, url, param, payload, method, success):
        stats = self.payload_stats.setdefault(payload, {"success": 0, "attempts": 0})
        stats["attempts"] += 1
        if success:
            stats["success"] += 1

    def rank_payloads(self, payloads):
        def score(p):
            data = self.payload_stats.get(p, {"success": 0, "attempts": 1})
            return data["success"] / data["attempts"]

        return sorted(payloads, key=score, reverse=True)

    def select_payload(self, payloads):
        ranked = self.rank_payloads(payloads)
        return ranked[0] if ranked else None
