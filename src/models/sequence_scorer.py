from typing import List

class SequenceScorer:
    @staticmethod
    def calculate_score(sequence: List[str]) -> float:
        """
        Calculate a simple language model score for a sequence of words.
        """
        score = 0
        for i in range(len(sequence) - 1):
            word1, word2 = sequence[i], sequence[i + 1]
            
            # Basic linguistic pattern scoring
            if word1.lower() in ['the', 'a', 'an'] and word2.lower() in ['and', 'or', 'but']:
                score -= 1  # Penalize article followed by conjunction
            if word1.lower() in ['and', 'or', 'but'] and word2.lower() in ['the', 'a', 'an']:
                score += 1  # Reward conjunction followed by article
                
        return score