import itertools
import pandas as pd
from typing import List

def calculate_sequence_score(sequence: List[str]) -> float:
    """
    Calculate a simple language model score for a sequence of words.
    This is a basic implementation - in practice you'd want to use
    the actual Gemma 2 9B model for scoring.
    """
    # Simple bigram-based scoring
    score = 0
    for i in range(len(sequence) - 1):
        word1, word2 = sequence[i], sequence[i + 1]
        # Add basic scoring logic here
        if word1.lower() in ['the', 'a', 'an'] and word2.lower() in ['and', 'or', 'but']:
            score -= 1  # Penalize article followed by conjunction
        if word1.lower() in ['and', 'or', 'but'] and word2.lower() in ['the', 'a', 'an']:
            score += 1  # Reward conjunction followed by article
    return score

def optimize_sequence(words: List[str], max_permutations: int = 1000) -> List[str]:
    """
    Optimize a sequence of words to minimize perplexity.
    Uses a simplified scoring approach for demonstration.
    """
    if len(words) <= 1:
        return words
    
    best_score = float('inf')
    best_sequence = words
    
    # For very long sequences, we'll use a sliding window approach
    if len(words) > 10:
        # Break into smaller chunks and optimize each
        window_size = 5
        optimized_words = []
        for i in range(0, len(words), window_size):
            chunk = words[i:i + window_size]
            optimized_chunk = optimize_sequence(chunk, max_permutations)
            optimized_words.extend(optimized_chunk)
        return optimized_words
    
    # For shorter sequences, try permutations
    for perm in itertools.islice(itertools.permutations(words), max_permutations):
        score = calculate_sequence_score(perm)
        if score < best_score:
            best_score = score
            best_sequence = perm
    
    return list(best_sequence)

def main():
    # Read input data
    df = pd.read_csv('sample_submission.csv')
    
    # Process each sequence
    results = []
    for _, row in df.iterrows():
        words = row['text'].split()
        optimized_words = optimize_sequence(words)
        results.append({
            'id': row['id'],
            'text': ' '.join(optimized_words)
        })
    
    # Create submission file
    submission_df = pd.DataFrame(results)
    submission_df.to_csv('submission.csv', index=False)
    print("Submission file created successfully!")

if __name__ == "__main__":
    main()