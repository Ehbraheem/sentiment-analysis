# AI-Based Web App for Emotion Detection and Sentiment Analysis

## Project Overview

This project involves creating an AI-based web application that performs analytics on customer feedback for an e-commerce company's signature products. The application includes two main components: an Emotion Detection system and a Sentiment Analysis system. Both components are built using the Flask framework and leverage Watson AI libraries for natural language processing.

## Scenario

You have been hired as a software engineer to create an AI-based web app that processes customer feedback in text format and deciphers the associated emotions and sentiments expressed. This project will assess your knowledge of app creation and web deployment.

## Introduction

Emotion detection extends the concept of sentiment analysis by extracting finer emotions, such as joy, sadness, anger, and more, from statements. This makes emotion detection a crucial branch of study, widely used in AI-based recommendation systems, automated chatbots, and more.

## Project Guidelines

For the completion of this project, you'll have to complete the following 8 tasks:

1. **Fork and Clone the Project Repository**
2. **Create an Emotion Detection Application using Watson NLP Library**
3. **Format the Output of the Application**
4. **Package the Application**
5. **Run Unit Tests on Your Application**
6. **Deploy as Web Application using Flask**
7. **Incorporate Error Handling**
8. **Run Static Code Analysis**

## Getting Started

### Prerequisites

- Python 3.6 or higher
- IBM Cloud account
- Access to Watson AI services

### Installation

1. **Fork and Clone the Repository**

    ```bash
    git clone https://github.com/Ehbraheem/ai-emotion-detection.git
    cd ai-emotion-detection
    ```

2. **Install the Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Your IBM Cloud Credentials and API Keys**

    Ensure you have the necessary credentials and API keys for Watson AI services.

## Applications

### Emotion Detector

The `emotion_detector` app processes customer feedback and detects emotions such as joy, sadness, anger, and more.

### Sentiment Analysis

The `sentiment_analysis` app analyzes customer feedback to determine the overall sentiment (positive, negative, or neutral).

## Running the Applications

1. **Emotion Detector**

    ```bash
    cd emotion_detector
    python app.py
    ```

2. **Sentiment Analysis**

    ```bash
    cd sentiment_analysis
    python app.py
    ```

## Deployment

To deploy the applications as web apps using Flask, follow these steps:

1. **Package the Application**

    Ensure all dependencies are listed in `requirements.txt`.

2. **Run Unit Tests**

    ```bash
    python -m unittest discover
    ```

3. **Deploy Using IBM Cloud Code Engine**

    ```bash
    ibmcloud ce application create --name emotion-detector --image us.icr.io/${SN_ICR_NAMESPACE}/emotion-detector --registry-secret icr-secret --m 8G --es 8G --port 8000 --minscale 1
    ibmcloud ce application create --name sentiment-analysis --image us.icr.io/${SN_ICR_NAMESPACE}/sentiment-analysis --registry-secret icr-secret --m 8G --es 8G --port 8000 --minscale 1
    ```

## Error Handling

Incorporate error handling to manage exceptions and ensure the application runs smoothly.

## Static Code Analysis

Run static code analysis to ensure code quality and adherence to best practices.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

- [IBM Watson](https://www.ibm.com/watson) for providing the AI capabilities.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- All contributors and users for their support.

---

**Author:** Ehbraheem
