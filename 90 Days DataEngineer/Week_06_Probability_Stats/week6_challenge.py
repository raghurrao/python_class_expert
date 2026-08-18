import numpy as np

def naive_bayes_predict(word_probs: dict, prior_spam: float, email_words: list) -> bool:
    """
    Compute spam vs ham posterior ratio and return True if email is spam.
    word_probs format: {word: (p_word_given_spam, p_word_given_ham)}
    """
    log_spam = np.log(prior_spam)
    log_ham = np.log(1.0 - prior_spam)
    
    for word in email_words:
        if word in word_probs:
            p_ws, p_wh = word_probs[word]
            log_spam += np.log(p_ws)
            log_ham += np.log(p_wh)
            
    return log_spam > log_ham