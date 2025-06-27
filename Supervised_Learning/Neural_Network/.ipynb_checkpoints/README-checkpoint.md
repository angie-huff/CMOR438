# Neural Networks with TensorFlow: Multiclass Classification of Openness to Experience

This notebook implements a neural network using TensorFlow and Keras to classify individuals into three levels of Openness to Experience—low, medium, or high—based on ten psychological survey items. The model structure and training approach are adapted from Lecture 6_3 of the CMOR 438 course.

## Dataset

The dataset is drawn from a larger open-source Big Five personality inventory. For this task, we use 2,000 randomly sampled individuals who completed the full set of trait measures. We specifically use the responses to the ten Openness items:

- `OPN1`, `OPN2`, ..., `OPN10`

Each item is rated on a Likert scale, and together they represent a participant's openness to experience—a trait linked to imagination, curiosity, and preference for novelty.

## Target Variable

Instead of a binary classification, we partition openness scores into **three classes** using tertiles:

- Class 0: Low openness (bottom third)
- Class 1: Medium openness (middle third)
- Class 2: High openness (top third)

This multiclass approach provides a more nuanced view of personality prediction and reflects the continuous nature of the openness trait.

## Model Overview

We define a simple multi-layer feedforward neural network using the Keras Sequential API:

- Input layer: 10 standardized features
- Hidden layers: Two layers with ReLU activation (8 and 4 neurons)
- Dropout layers for regularization
- Output layer: 3 neurons with softmax activation

The model is trained with the Adam optimizer and sparse categorical cross-entropy loss. Early stopping is used to prevent overfitting.

## Results

- Final validation accuracy: ~93%
- Macro F1-score: 0.91
- Confusion matrix shows strong recall for low and high openness classes
- Medium openness was more difficult to classify, consistent with its conceptual ambiguity

These results suggest that even a small neural network can meaningfully differentiate psychological trait profiles from brief survey data. The model generalizes well and avoids overfitting, unlike earlier binary versions.

## Interpretation

This notebook demonstrates how neural networks can be applied to structured, real-world data from psychology. The results show potential for automated trait estimation in applications such as personalized content delivery, career matching, or mental health screening. The transition from binary to multiclass targets reflects a more realistic use case for continuous psychological dimensions.
