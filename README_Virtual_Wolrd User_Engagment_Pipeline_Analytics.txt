
# Virtual World User Engagement Pipeline Analytics Pipeline

## Project Overview
This project simulates and analyzes user engagement data from a Virtual World User Engagement Pipeline environment. We simulate activities like movement, interaction, and purchases to build a real-time data pipeline that processes, stores, and visualizes user behaviors.

## Key Features:
- **Real-time Data Ingestion** using Apache Kafka for streaming user events.
- **Real-time Data Processing** with Apache Spark Streaming.
- **Data Storage** in Google BigQuery (or AWS Redshift) for scalable querying and storage.
- **Data Transformation** using dbt for metrics calculation and data modeling.
- **Data Visualization** with Google Data Studio or Tableau Public.

## Technologies Used:
- Apache Kafka
- Apache Spark Streaming
- Google BigQuery / AWS Redshift
- dbt (Data Build Tool)
- Google Data Studio / Tableau Public

## Project Steps:

1. **Data Ingestion**:
   - Simulated user activity data from a Virtual World User Engagement Pipeline environment (movement, interactions, purchases) is ingested into Kafka.

2. **Data Processing**:
   - Kafka streams are processed in real time using Spark Streaming, where activities are parsed, cleaned, and aggregated.

3. **Data Storage**:
   - Processed data is stored in Google BigQuery or AWS Redshift, partitioned by activity type.

4. **Data Transformation**:
   - dbt is used to model the data and create key engagement metrics (e.g., DAU, MAU, transaction trends).

5. **Data Visualization**:
   - Dashboards in Google Data Studio / Tableau Public visualize user behavior trends, engagement metrics, and more.

## How to Run the Project:

1. **Kafka Setup**:
   - Install and configure Kafka on your local machine or cloud provider.
   - Create the necessary Kafka topics (e.g., `Virtual World User Engagement Pipeline-events`).

2. **Simulating Data**:
   - Use the Python script `Virtual World User Engagement Pipeline_data_simulator.py` to generate user event data and send it to Kafka.

3. **Spark Streaming**:
   - Run `spark_streaming_job.py` to process the real-time data and store it in BigQuery/Redshift.

4. **Data Transformation**:
   - Run `dbt` transformations to create key metrics.

5. **Visualize Data**:
   - Connect BigQuery/Redshift to Google Data Studio or Tableau Public and create interactive dashboards.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
