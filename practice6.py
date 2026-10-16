def bayes(prior, p_o, p_c):
    so = prior * p_o
    sc = (1 - prior) * p_c
    return so / (so + sc)

# A бөлімі: бір хабар
print(round(bayes(0.30, 0.80, 0.20), 4))  # BLOCKED -> 0.6316
print(round(bayes(0.30, 0.20, 0.80), 4))  # CLEAR   -> 0.0968

# C бөлімі: HMM
obs = ["BLOCKED", "CLEAR", "BLOCKED", "BLOCKED"]
emit = {"BLOCKED": (0.8, 0.2), "CLEAR": (0.2, 0.8)}
p = 0.30
for t, r in enumerate(obs, 1):
    pred = p if t == 1 else 0.7 * p + 0.2 * (1 - p)
    p = bayes(pred, *emit[r])
    print(t, r, round(pred, 4), round(p, 4))
