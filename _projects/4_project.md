---
layout: page
title: Protein-ligand binding affinity prediction
description: Structure-based screening for NS3 serine protease inhibitors
importance: 4
category: work
---

Implemented dockerised deep learning pipelines for protein-ligand binding affinity prediction,  screening for candidate small-molecule inhibitors of NS3 serine protease.

            |                 | 
Molecule -> |     FlowDock    | -> Score
            |                 |

            |                 | 
Molecule -> |   DynamicBind   | -> Score
            |                 |

            |                 | 
Molecule -> |     Equibind    | -> Score
            |                 |

