# Title
Healthy food: from packaging to consumption

# Abstract
One of the highest stake of the century is to limit the damages made on natural resources. Understanding where the food is produced, packaged and consumed can show insights about the current issues in the food industry. In some countries, there is a tendency to favor local products, we want to see if this is really the case and see how the food travels. Moreover, we would like to estimate the impact of those travels on the carbon footprint index.

In a later part, we will try to see if there is any correlation between the packaging of a product (color, shape, material) and its quality in terms of nutritious facts. Are there dominant colors in the packaging that could describe the overall quality of the food?

Our project is motivated by the idea of understanding these tendencies in the marketing behind the food industry, to have a good way to visualize those results and to see whether the use of machine learning for computer vision can bring some interesting insights. 

# Research questions
* How does food products travel before being sold (distance, countries visited)?
* Which countries consume the best food in terms of nutritious facts?
* Which brands produce healthier and more environmental friendly food?
* Does packaging allows consumers to have a good idea of a product quality?

# Dataset
* Open Food Facts database: this database is organized in a csv file, we will probably consider columns such as 'nutrition_grade_fr' or 'carbon-footprint_100g'. The fields 'origins', 'manufacturing_places', 'cities' and 'countries' will be useful to better understand how the food travels around the world.

There is also a 'image_url' field which can be used to retrieve an image of the packaging, so that we can describe it, find patterns, with some image processing or machine learning techniques. Also, the 'packaging' field contains information about the material and shape of the packaging.

# A list of internal milestones up until project milestone 2
* Technical preparation: setup the repository with proper .gitignore file, branches and file hierarchy. Download the datasets
* Get a more precise idea on which visualizations we want for our results, and thus which libraries we should use
* Exploratory data analysis: explore the dataset, understand the data we are working on and document it. Understand the correlations, the potential redundancies and the outliers. Refresh on relational models and think about applying them to the datasets to make them easier to use
* Transform the datasets according to our needs, discarding what we will not use and isolating what will interest us the most (when possible)
* Make statistical models for the quantities that we want to count, and make sure that our research is unbiased, or quantify the bias and keep it minimal.
* Update our project's direction with respect to our better knowledge of the datasets


# Questions for TAs
