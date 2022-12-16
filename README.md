# Climate Analysis 

### Part 1: Climate Analysis and Exploration

In this project, I used Python and SQLAlchemy to perform basic climate analysis and data exploration of the climate database. 

First, I found the most recent date in the dataset and used it to retrieve the previous 12 months of precipitation data by querying the 12 previous months of data. I loaded the query results into a Pandas DataFrame and plotted the results using the Dataframe plot method. 

Then I designed a query to calculate the total number of stations in the dataset, and a query to find the most active stations. Using the most active station id, I calculated the lowest, highest, and average temperatures.

Finally, I designed a query to retrieve the previous 12 months of temperature observation data (TOBS). I filtered the data by the station with the highest number of observations, and queried the previous 12 months of temperature observation data for this station. Then, I plotted the results as a histogram. 

### Part 2: Designing the Climate App

After completing my initial analysis, I designed a Flask API based on the queries that I developed. 

I used Flask to create the following routes: 

* `/`

    * Homepage that lists all available routes.

* `/api/v1.0/precipitation`

    * Returns a list of the prior year's precipitation data for all stations in a dictionary. 

* `/api/v1.0/stations`

    * Returns a JSON list of all station numbers and names.

* `/api/v1.0/tobs`

    * Returns a JSON list of the prior year's min, max and avg temperatures from all stations.

* `/api/v1.0/<start>`

    * Returns a calculated min, max and avg temperature for all dates greater than or equal to an inputted start date (YYYY-MM-DD).

* `/api/v1.0/<start>/<end>`

    * Returns a calculated min, max and avg temperature for all dates between an inputted start and end date (YYYY-MM-DD).
