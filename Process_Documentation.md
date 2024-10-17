# Process Documentation: Virtual World User Engagement Pipeline Analytics

## Project Setup Steps and Overview

This document outlines the key steps taken to build the real-time analytics pipeline for processing and analyzing user engagement data in a virtual world.

### 1. Setting up Apache Kafka (Confluent Cloud)
**Goal**: To create a real-time data ingestion layer where events from a virtual world (e.g., user movement, interactions, purchases) are streamed.

- **Action**: Created a free **Confluent Cloud** account and spun up a Kafka cluster.
- **Topic Created**: `user_engagement_events`.
- **Reason**: Kafka allows decoupled, scalable event streaming, which is ideal for capturing real-time user activity.

### 2. Writing the Data Simulator
**Goal**: To simulate user events such as movements and interactions in a virtual world.

- **Python Script**: Wrote `kafka_producer_consumer.py` to simulate user activity and send events to the Kafka topic.
- **Details**:
  - Events include: user movement, item purchases, and user interactions.
  - Data is sent to the `user_engagement_events` topic in real time.

### 3. Real-Time Processing with Apache Spark (Databricks)
**Goal**: To process the streamed Kafka events in real-time, aggregate them, and store the results for analysis.

- **Action**: Used **Databricks Community Edition** to set up a Spark Streaming job.
- **Spark Job**:
  - Consumed data from the Kafka topic.
  - Cleaned and aggregated events (e.g., counting interactions, calculating transaction totals).
- **Reason**: Spark Streaming is optimized for processing data in real time, enabling real-time metric calculation.

### 4. Data Storage in Google BigQuery
**Goal**: To store the processed data for further analysis and transformation.

- **Action**: Set up **Google BigQuery** (using the free tier) to store processed Kafka events from Spark.
- **Details**:
  - Partitioned the data by event type (e.g., movement, interaction, purchase).
  - Enabled querying of stored data for later transformation.

### 5. Data Transformation with dbt
**Goal**: To transform raw event data into meaningful business metrics like DAU and MAU.

- **Action**: Wrote SQL models in **dbt** to transform the raw data stored in BigQuery.
- **Metrics Calculated**:
  - Daily Active Users (DAU).
  - Monthly Active Users (MAU).
  - Transaction trends by item type and user location.

### 6. Visualization with Google Data Studio
**Goal**: To create dashboards that visualize user engagement metrics in real-time.

- **Action**: Connected **Google Data Studio** to BigQuery to visualize the processed metrics.
- **Dashboards Created**:
  - User activity trends (movements, interactions).
  - Purchase patterns by item type.
  - Active users by day, week, and month.

## Conclusion

By integrating **Kafka**, **Spark**, **BigQuery**, and **dbt**, this project successfully demonstrates a full real-time analytics pipeline that can ingest, process, store, transform, and visualize large-scale data. Future improvements include enhancing the data visualization layer and extending the pipeline to support more data types.
