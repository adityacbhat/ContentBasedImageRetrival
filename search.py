from searcher import Searcher
from colordescriptor import ColorDescriptor
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
# initialize the image descriptor
cd = ColorDescriptor((8, 12, 3))


query = cv2.imread(args["query"])
features = cd.describe(query)
# perform the search
searcher = Searcher(args["index"])
results = searcher.search(features)
# display the query
cv2.imshow("Query", cv2.resize(query,(640,480)))
# loop over the results
for (score, resultID) in results:
	# load the result image and display it
    print("rsid: ",resultID," score: ",score)
    result = cv2.imread(resultID)
    try:
        cv2.imshow("Result", cv2.resize(result,(640,480)))
        cv2.waitKey(0)
    except:
        pass

cv2.destroyAllWindows()