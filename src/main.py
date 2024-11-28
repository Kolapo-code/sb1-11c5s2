from models.sequence_scorer import SequenceScorer
from optimizers.sequence_optimizer import SequenceOptimizer
from data.data_handler import DataHandler

def main():
    # Initialize components
    scorer = SequenceScorer()
    optimizer = SequenceOptimizer(scorer)
    data_handler = DataHandler()
    
    # Read input data
    df = data_handler.read_input('sample_submission.csv')
    
    # Process sequences
    results = []
    for _, row in df.iterrows():
        words = row['text'].split()
        optimized_words = optimizer.optimize(words)
        results.append({
            'id': row['id'],
            'text': ' '.join(optimized_words)
        })
    
    # Save results
    data_handler.save_submission(results, 'submission.csv')

if __name__ == "__main__":
    main()