import itertools
from typing import List
from ..models.sequence_scorer import SequenceScorer

class SequenceOptimizer:
    def __init__(self, scorer: SequenceScorer):
        self.scorer = scorer
        
    def optimize(self, words: List[str], max_permutations: int = 1000) -> List[str]:
        """
        Optimize a sequence of words to minimize perplexity.
        """
        if len(words) <= 1:
            return words
        
        if len(words) > 10:
            return self._optimize_long_sequence(words, max_permutations)
        
        return self._optimize_short_sequence(words, max_permutations)
    
    def _optimize_short_sequence(self, words: List[str], max_permutations: int) -> List[str]:
        """
        Optimize shorter sequences using direct permutations.
        """
        best_score = float('inf')
        best_sequence = words
        
        for perm in itertools.islice(itertools.permutations(words), max_permutations):
            score = self.scorer.calculate_score(perm)
            if score < best_score:
                best_score = score
                best_sequence = perm
                
        return list(best_sequence)
    
    def _optimize_long_sequence(self, words: List[str], max_permutations: int) -> List[str]:
        """
        Optimize longer sequences using sliding window approach.
        """
        window_size = 5
        optimized_words = []
        
        for i in range(0, len(words), window_size):
            chunk = words[i:i + window_size]
            optimized_chunk = self._optimize_short_sequence(chunk, max_permutations)
            optimized_words.extend(optimized_chunk)
            
        return optimized_words