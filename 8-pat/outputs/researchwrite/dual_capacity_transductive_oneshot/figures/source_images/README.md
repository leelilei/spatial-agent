# Training-image provenance

The manuscript image plate contains six real images from the official training
partitions. No generated or official-test image is included.

## CUB-200-2011

The three CUB images were retrieved from the public training-only mirror
`anjunhu/naively_captioned_CUB2002011_train`, which contains 5,994 examples,
matching the official CUB training partition:

- row 3: Nashville warbler;
- row 5: Tennessee warbler;
- row 3002: Myrtle warbler.

The local image bytes were checked against the current dataset-server assets;
all SHA256 digests matched. The official dataset record is:

`https://data.caltech.edu/records/65de6-vp158`

## Stanford Dogs

The three Dogs files were checked against the `train_list.mat` distributed in
the official Stanford Dogs `lists.tar` archive:

- `n02094114-Norfolk_terrier/n02094114_2923.jpg`;
- `n02094258-Norwich_terrier/n02094258_3435.jpg`;
- `n02096177-cairn/n02096177_164.jpg`.

All three occur in the 12,000-file training list and none occurs in the
8,580-file test list. The official dataset page is:

`http://vision.stanford.edu/aditya86/ImageNetDogs/`

The image bytes were retrieved from the public `ksaml/Stanford_dogs` mirror.

## Processing and audit

`generate_figures.py` applies only a centered 4:3 crop for consistent display.
It does not adjust brightness, contrast, color, gamma, or local content. The
generated `source_data/fig_training_examples_provenance.csv` records the panel,
class, source locator, split evidence, processing, and SHA256 digest for every
displayed image.

The source datasets remain subject to their original terms and citations.
