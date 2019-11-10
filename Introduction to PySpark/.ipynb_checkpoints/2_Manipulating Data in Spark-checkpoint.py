# 1. Creating columns
# Create the DataFrame flights
flights = spark.table('flights')

# Show the head
flights.show()

# Add a new column "duration_hrs" to existing table
flights = flights.withColumn('duration_hrs',flights.air_time/60)

# 2. Filtering Data
# Filter flights by passing a string
long_flights1 = flights.filter('distance >1000')

# Filter flights by passing a column of boolean values
long_flights2 = flights.filter(flights.distance > 1000)

# Print the data to check they're equal
long_flights1.show()
long_flights2.show()

# 3. Selecting
# Select the first set of columns
selected1 = flights.select('tailnum','origin','dest')

# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)

# Define first filter
filterA = flights.origin == "SEA"

# Define second filter
filterB = flights.dest == "PDX"

# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")

# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)

# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")