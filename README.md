# Virtual World User Engagement Pipeline Analytics

## Project Overview
This project simulates and analyzes user engagement data from a virtual world environment. It models activities like movement, interaction, and purchases to build a real-time data pipeline for processing, storing, and visualizing user behaviors.

## Key Features:
- **Real-time Data Ingestion** using Apache Kafka to stream user events.
- **Real-time Data Processing** with Apache Spark Streaming for processing events.
- **Data Storage** in Google BigQuery (or AWS Redshift) for scalable querying and storage.
- **Data Transformation** using dbt (Data Build Tool) for creating key metrics.
- **Data Visualization** with Google Data Studio or Tableau Public for dashboards.

## Technologies Used:
- Apache Kafka (Confluent Cloud)
- Apache Spark (Databricks)
- Google BigQuery / AWS Redshift
- dbt (Data Build Tool)
- Google Data Studio / Tableau Public

## Project Architecture:
Here’s a high-level overview of the data pipeline architecture:

1. **Data Ingestion**: Kafka receives events such as user movements, purchases, and interactions from the virtual world.
2. **Real-time Processing**: Spark Streaming processes these events and aggregates them in real-time.
3. **Data Storage**: Processed events are stored in Google BigQuery or AWS Redshift, partitioned by activity type.
4. **Data Transformation**: dbt models the data to create key metrics such as Daily Active Users (DAU), Monthly Active Users (MAU), and transaction trends.
5. **Data Visualization**: Google Data Studio or Tableau Public is used to visualize user behaviors, engagement metrics, and trends.

## How to Run the Project:

### 1. Kafka Setup
- Sign up for **Confluent Cloud** and create a free Kafka cluster.
- Create a Kafka topic named `user_engagement_events`.

### 2. Data Simulation
- Run the Python script `kafka_producer_consumer.py` to generate simulated user events and send them to the Kafka topic.

### 3. Real-Time Processing with Spark
- Create a Spark Streaming job in **Databricks** to process real-time events from Kafka and store the results in BigQuery.

### 4. Data Transformation
- Use `dbt` to run SQL transformations on the data stored in BigQuery to create engagement metrics (e.g., DAU, MAU).

### 5. Visualization
- Use **Google Data Studio** or **Tableau Public** to visualize the processed data with dashboards.

## License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
