# Fluency and minimal-edit annotations

These are the annotations that we collected for the sentence in the NUCLE test set
(download)[http://www.comp.nus.edu.sg/~nlp/conll14st.html]. There are 1313 sentences in
the original data, however the expert annotators identified 34 sentences that should have
been merged together. The line numbers of these sentences are included in the `merged_ids`
file (1-indexed). For our analysis, we skipped these sentences in all annotation sets.

## Data

    .
    ├── README.md
    ├── expert_annotations	# expert fluency and minimal edits
    │   ├── expert_fluency
    │   └── expert_minimal
    ├── extra_fluency		# 10 more non-expert minimal edits for 20 sentences
    ├── merged_ids		# list of sentences that need to be merged
    └── turker_annotations	# non-expert fluency and minimal edits      
	├── raw			# non-expert annotations, pre-tokenization
	├── turkers_fluency	
	└── turkers_minimal
