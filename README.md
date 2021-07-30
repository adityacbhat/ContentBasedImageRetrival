# ContentBasedImageRetrival
CBIR using histogram as image discriptors
Index the dataset using:
python index.py --dataset dataset --index index.csv

Search using query image using:
python search.py --index index.csv --query dataset/201100.jpg --result-path dataset
