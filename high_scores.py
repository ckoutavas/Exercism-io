class HighScores(object):
    def __init__(self, scores):
        self.scores = scores
        
    def latest(self):
        return self.scores[-1]
    
    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        last = self.scores[-1]
        diff = abs(last - max(self.scores))
        
        if last >= max(self.scores):
            return f"Your latest score was {last}. That's your personal best!"
        else:
            return f"Your latest score was {last}. That's {diff} short of your personal best!"

    def personal_best(self):
        return max(self.scores)
