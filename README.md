# Healthy food: from packaging to consumption

## Running our notebook
In order to view everything, including the Folium maps, our notebook should be viewed as html. It is stored in docs/index.html. The html file should be accessed from https://mattbuot.github.io/Project/.

In case this does not work, you can still view the file ProjectADA-Final.ipynb in Github (everything is displayed except the maps), download our repository, go to the `maps` folder and manually open the maps that you want with Google Chrome.

You can also run our notebook, but for this you would need to download about 2 GB of csv data from https://static.openfoodfacts.org/data/en.openfoodfacts.org.products.csv, put that into the data folder, to install the libraries we use, and the version of Folium needs to be at least 0.7 (very recent). Also, our notebook can be quite long to run (5-30 mins depending on the computer) since we did not include any save of the cleaned data in the last version of the notebook (in order to make it a bit shorter).

## Abstract
One of the highest stake of the century is to limit the damage done to natural resources. Understanding where the food is produced, packaged and consumed can show insights about the current issues in the food industry. In some countries, there is a tendency to favor local products, we want to see if this is really the case and see which countries import-export where.

A second analysis will be made on the products designed as organic. What types of packaging are used for these products? Today, we use a lot of plastic, so it would be interesting to see if the organic products try to limit this tendency. Also, we will try to see if the organic products are local or imported. We surely hope that it is local, and using this dataset will certainly lead to useful insights.

In a later part, we will try to see if there is any correlation between the packaging of a product (color, shape, material) and its quality in terms of nutritious facts. Are there dominant colors in the packaging that could describe the overall quality of the food?

Our project is motivated by the idea of understanding these tendencies in the marketing behind the food industry, to have a good way to visualize those results and to see whether the use of machine learning for computer vision can bring some interesting insights. 

## Research questions
* How do food products are imported and exported?
* What proportion of products are imported and exported?
* Do organic products have a more environmental friendly packaging?
* Do organic products come from the country, or are they imported?
* Which countries produce healthier and more environmental friendly food?
* Does packaging allows consumers to have a good idea of a product quality?

## Dataset
***Open Food Facts database***: this database is organized in a csv file, we will probably consider columns such as `fat_100g`, `salt_100g`, or `sugars_100g`. The fields `origins` and `countries` will be useful to better understand how the food is imported and exported.

To filter and analyze the BIO products, we'll use the `labels` column since it tells us wether a product is BIO or not.

There is also an `image_url` field which can be used to retrieve an image of the packaging, so that we can describe it, find patterns, with some image processing or machine learning techniques. Also, the `packaging` field contains information about the material and shape of the packaging.

## A list of internal milestones up until project milestone 2
* Technical preparation: setup the repository with proper .gitignore file, branches and file hierarchy. Download the datasets.
* Get a more precise idea on which visualizations we want for our results, and thus which libraries we should use.
* Exploratory data analysis: explore the dataset, understand the data we are working on and document it. Understand the correlations, the potential redundancies and the outliers. Refresh on relational models and think about applying them to the datasets to make them easier to use.
* Transform the datasets according to our needs, discarding what we will not use and isolating what will interest us the most (when possible).
* Make statistical models for the quantities that we want to count, and make sure that our research is unbiased, or quantify the bias and keep it minimal.
* Update our project's direction with respect to our better knowledge of the datasets.

## A list of internal milestones up until the final submission

**We have chosen the pdf report for the final submission.**

For the 3rd milestone, we mainly plan to:

* Work on the formatting of packaging (in order to have everything in the same language, and matching precise names, like we did for the countries) → For the 2nd of December.

* Add visualization part (world map) For each country we plan to display some nutritional information about its products (from the columns of the form information_100g) → For the 2nd of December.

* Make some analysis on more labels (among vegan, gluten-free, halal and fair-trade) → For the 7th of December.

* Perform the machine learning part with the images for the organic products (to see if there are recurrent patterns or dominant colors) → For the 7th of December

**Note that we already created a script in order to download the images of products with the BIO label. It can be found in the file `images_download.py.`**

* Complete the report → For the 14th of December

* Review our report before the final submission and enhance it → For the 16th of December

## Plans for the presentation

For the presentation, we plan to:

* Give an introduction about the problem of how the food travels, packaging issues, organic products.

* Explain what our project was about (where the food comes from, organic products, packaging)

* Explain cleaning of the dataset shortly, and indicate the analyses we performed (import-export, packaging, images of packaging)

* Show the results on the poster, which will include: 
  * A map of Europe with countries from which France imports
  * A map of the world showing the proportion of plastic
  * Comparison of packaging for organic VS non-organic products
  * Explain the spectra obtained for the image processing part
  * Conclude with some explanations
  
## Plans for the design of the poster

For the poster, we plan to:
* Add the visualizations of the different results which includes:
  * One map of import export
  * Maps showing the packaging used around the world
  * Comparison of packaging organic VS non-organic products
  * Add the spectra for image processing part
  
* Explanations, which will include:
  * Introduction of our project & problematic
  * Cleaning of the data
  * Briefly explain import/export + packaging
  * More explanations for image processing
  * Comments on the results
  * Conclusion
 
## Contributions of group members
The workload was distributed in the following way:
 
**Valérian**: Cleaning of the dataset, analysis packaging & visualizations (maps)

**Matthieu**: Image processing of the packages
 
**Adrien**: Analysis of import-export & report
