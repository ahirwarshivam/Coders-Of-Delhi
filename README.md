# Coders Of Delhi

## Overview

Coders Of Delhi is a purely Python-based social networking recommendation system that analyzes user data stored in JSON format and generates intelligent friend and page recommendations.

The project simulates the recommendation mechanisms used by modern social networking platforms by leveraging mutual connections and shared interests.

---

## Problem Statement

Social networking platforms often struggle to help users discover relevant friends and communities.

This project aims to solve this problem by:

* Recommending new friends based on existing connections
* Recommending pages based on user interests
* Cleaning noisy and inconsistent user data before analysis

---

## Features

### Data Cleaning

* Removed duplicate users
* Removed duplicate pages
* Handled missing user information
* Validated friend relationships

### Friend Recommendation System

* Finds mutual connections
* Suggests relevant users who are not already friends

### Page Recommendation System

* Analyzes user interests
* Recommends pages liked by similar users

---

## Technologies Used

* Python
* JSON
* Data Structures
* Algorithms

---

## Project Workflow

Raw JSON Data

↓

Data Cleaning

↓

User Relationship Analysis

↓

Friend Recommendation

↓

Page Recommendation

---

## Dataset

The project contains:

* Raw Dataset
* Cleaned Dataset
* Large-scale Testing Dataset

---

## Learning Outcomes

Through this project, I gained practical experience in:

* JSON Processing
* Data Cleaning
* Recommendation Algorithms
* Python Data Structures
* Algorithm Design

---

## Future Improvements

* Recommendation Scoring System
* Network Graph Visualization
* Interactive Dashboard
* Machine Learning-based Recommendations

---
## Project Outputs

### Data Cleaning Result
<img width="1352" height="682" alt="COD Data srnsht 1" src="https://github.com/user-attachments/assets/76183616-d797-426c-9e5d-f14e26c6b913" />
---

### Friend Recommendation Result
<img width="1356" height="214" alt="COD srnsht result" src="https://github.com/user-attachments/assets/72466968-394c-4c05-91b5-b091f614e3d4" />

---
### Page Recommendation Result
<img width="1356" height="609" alt="COD srnsht pages result" src="https://github.com/user-attachments/assets/51b832e5-3c27-42a7-b051-ed00097945f3" />

---
## Datasets Used

This project uses multiple datasets to demonstrate different stages of the recommendation system.

### data2.json

Used for displaying user information, friendships, and liked pages through the `about_user()` function.

### data3.json

Used for data cleaning operations such as:

* Removing users with missing names
* Removing duplicate friends
* Removing inactive users
* Removing duplicate pages

### cleaned_data3.json

Generated after applying the data cleaning process on `data3.json`. This dataset contains the cleaned and structured data.

### massive_data.json

A larger dataset used for testing the recommendation system on a larger scale and evaluating its performance.

---

## Author

Shivam Ahirwar
IIT Kharagpur
