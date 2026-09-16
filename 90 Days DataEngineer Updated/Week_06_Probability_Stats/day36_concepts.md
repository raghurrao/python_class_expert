# Day 36: Conditional Probability & Bayes' Theorem

Probability is the mathematical language of uncertainty. In data science, we rarely know things with 100% certainty; instead, we deal with probabilities.

---

## 1. Conditional Probability
Conditional probability is the probability of an event occurring *given* that another event has already occurred.
* Notation: $P(A|B)$ (Probability of A given B)
* Formula: $P(A|B) = \frac{P(A \cap B)}{P(B)}$

**Example:** What is the probability that someone buys a phone case ($A$) *given* that they just bought a new phone ($B$)? It is much higher than the probability of someone randomly buying a phone case on a Tuesday.

---

## 2. Bayes' Theorem
Bayes' Theorem provides a principled way to update our beliefs (probabilities) when we receive new evidence.

**Formula:**
$$P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$$

* **$P(A)$ (Prior):** Our initial belief in event A before seeing any evidence.
* **$P(B|A)$ (Likelihood):** The probability of seeing the evidence B if A is true.
* **$P(B)$ (Marginal Likelihood):** The total probability of seeing the evidence B under all possible circumstances.
* **$P(A|B)$ (Posterior):** Our updated belief in A *after* seeing the evidence B.

### Medical Testing Example
Imagine a rare disease affects 1% of the population ($P(\text{Disease}) = 0.01$).
A test for this disease is 90% accurate ($P(\text{Positive}|\text{Disease}) = 0.90$).
The test has a 5% false-positive rate ($P(\text{Positive}|\text{No Disease}) = 0.05$).

If you test positive, what is the actual probability you have the disease?

```python
# P(Disease) - Prior
p_disease = 0.01

# P(Positive | Disease) - Likelihood
p_pos_given_disease = 0.90

# P(Positive | No Disease) - False Positive
p_pos_given_no_disease = 0.05
p_no_disease = 1 - p_disease

# P(Positive) - Total probability of testing positive
p_pos = (p_pos_given_disease * p_disease) + (p_pos_given_no_disease * p_no_disease)

# P(Disease | Positive) - Bayes' Theorem
p_disease_given_pos = (p_pos_given_disease * p_disease) / p_pos

print(f"Probability of having the disease given a positive test: {p_disease_given_pos:.2%}")
# Output: ~15.38%
# Wait, only 15%?! Yes! Because the disease is so rare, most positive tests are actually false positives!
```

---

## 3. Reference Documentation
* [Bayes' theorem (Wikipedia)](https://en.wikipedia.org/wiki/Bayes'_theorem)