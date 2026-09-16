def bayes_spam_probability(p_spam: float, p_word_given_spam: float, p_word_given_ham: float) -> float:
    """
    Calculate the posterior probability that an email is spam given that it contains a specific word.
    Formula:
    P(Spam|Word) = P(Word|Spam) * P(Spam) / P(Word)
    where P(Word) = P(Word|Spam)*P(Spam) + P(Word|Ham)*P(Ham)
    and P(Ham) = 1 - P(Spam)
    """
    p_ham = 1.0 - p_spam
    p_word = p_word_given_spam * p_spam + p_word_given_ham * p_ham
    return (p_word_given_spam * p_spam) / p_word