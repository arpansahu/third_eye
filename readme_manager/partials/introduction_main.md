# arpansahu.me | Django Portfolio Project 

This is a simple django portfolio project

## Project Features

1. **Account Functionality:** Complete account management.
2. **PostgreSql Integration:** Utilized as a database.
3. **AWS S3/MinIO Integration:** For file storage.
4. **Redis Integration:** Utilized for caching and message pub/sub.
5. **MailJet Integration:** Used for email services.
6. **Dockerized Project:** Fully containerized for easy deployment.
7. **Kubernetes-native** Kubernetes support also available.
8. **CI/CD Pipeline:** Continuous integration and deployment included using Jenkins.
9. **Sentry Integrated:** Logging and Debugging Made Easy.
10. **Scikit Learn & Pandas:** Training and using Machine Learning.

## WhatsApp Clone Functionalities

1. **Symptom Analysis and Disease Prediction::**
   - Users can input symptoms, and the application predicts the most probable disease using a trained Machine Learning model.
   - The model is trained using the Naive Bayes algorithm on data collected from MIT, focusing on 53 symptoms.
   - The trained model is pickled and utilized within Django views to make predictions.
2. **Medical Facility Locator:**
   - Integrated with Google Maps API to identify the user’s location.
   - Displays nearby hospital facilities based on the user’s location.
   - The hospital data is primarily sourced from Indian government databases, but users can add additional facilities as needed.
3. **Data Handling::**
   - Utilizes a dataset collected from the MIT website for training the Machine Learning model.
   - Hospitals and medical facility data are sourced from Indian government websites and stored in the project’s database.
4. **Web Interface:**
   - A simple web interface with three primary views, all function-based, allowing users to interact with the application easily.
   - Provides users with an intuitive interface to input symptoms, view predictions, and locate nearby medical facilities.
 