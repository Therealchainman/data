# Databricks notebook source
# MAGIC %md
# MAGIC # MAP MATCHING

# COMMAND ----------

# MAGIC %md
# MAGIC kalman filter, particle filter, hidden markov models
# MAGIC 
# MAGIC geometry, topology, probabilist, advanced
# MAGIC geometry: distance between trajectory elements and the road network
# MAGIC topology: considers connectivity and shape similarity
# MAGIC probabilistic: models uncertainty of trajectory, measurement error, unknown travel path between two samples.
# MAGIC advanced: kalman filter, particle filter, and fuzzy logic
# MAGIC 
# MAGIC navigation
# MAGIC tracking
# MAGIC mapping
# MAGIC incremental max-weight
# MAGIC global max-weight
# MAGIC global geometry
# MAGIC 
# MAGIC categories
# MAGIC similarity model, state-transition model, candidate-evolving model, and scoring model

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC ## SIMILARITY MODEL
# MAGIC 
# MAGIC vertices/edge closest to trajectory geometrically and/or topologically
# MAGIC 
# MAGIC closeness:  distance-based, pattern-based

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # STATE-TRANSITION MODEL
# MAGIC 
# MAGIC vertices (states), edges (transitions), weighted topological graph
# MAGIC 
# MAGIC 3 ways, hidden markov model (HMM), Conditional Random Field (CRF), Weighted Graph Technique (WGT)

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # CANDIDATE-EVOLVING MODEL
# MAGIC 
# MAGIC holds set of candidates (particles)
# MAGIC keeps set of candidates, and prunes old ones
# MAGIC 
# MAGIC particle filter, multiple hypothesis technique
# MAGIC 
# MAGIC particle filter combines monte carlo sampling methods with Bayesian Inference
# MAGIC 
# MAGIC recursively estimate the Probability Density Function (PDF)
# MAGIC 
# MAGIC N discrete particles

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # SCORING MODEL
# MAGIC 
# MAGIC naieve weighting:  lane-level map matching performance, road width information, partition into grids

# COMMAND ----------

# MAGIC %md
# MAGIC 
# MAGIC # DATASETs
# MAGIC 
# MAGIC https://sci-hub.ru/10.1109/ivs.2015.7225829SSSSSSSSSSSSSSSSSSSSSSSSSS

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------


