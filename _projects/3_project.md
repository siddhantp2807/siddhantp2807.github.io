---
layout: page
title: AMP/NAMP activity classifier
description: ProtBERT + XGBoost classifier for antimicrobial peptide activity (MCC 0.867)
importance: 3
category: work
---

Trained three classical classifier models (Logistic Regression, Random Forest and XGBoost) distinguishing antimicrobial peptides (AMPs) from non-antimicrobial peptides (NAMPs), using ProtBERT embeddings and biophysical properties as features.

**Result:** Matthews correlation coefficient (MCC) of **0.867** on held-out (test) sequences (XGBoost).

Code available on [GitHub](https://github.com/rikmicrobio/IIMT-WORKSHOP-).
