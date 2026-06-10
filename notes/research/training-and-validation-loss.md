# Training and Validation Loss in Deep Learning

[**Training loss**](https://www.geeksforgeeks.org/deep-learning/training-and-validation-loss-in-deep-learning/) measures how well the model learns from the training data during training. **Validation loss** shows how well the trained model performs on unseen data, helping detect overfitting.

## Training Loss

Training Loss is a metric that measures how well a deep learning model is performing on the training dataset. During training, the model makes predictions and compares them with the actual target values. The loss function then calculates the error between these predicted outputs and the true labels.

Training loss is computed after each forward pass and backward pass. The training loss can be expressed as:

$$
\text{Loss} = \frac{1}{N} \sum_{i=1}^{N} L(y_i, \hat{y}_i)
$$

Where:

- **N**: Total number of training examples
- **yᵢ**: True label
- **ŷᵢ**: Predicted output
- **L**: Chosen loss function

A lower training loss means the model is learning well, whereas a high training loss often indicates underfitting or difficulty in learning patterns.

## Validation Loss

Validation loss is a metric that evaluates a deep learning model's performance on a validation dataset (a set of data that the model has never seen during training). Validation loss is computed after each epoch during training.

$$
\text{Validation Loss} = \frac{1}{M} \sum_{i=1}^{M} L(y_i^{\text{val}}, \hat{y}_i^{\text{val}})
$$

Where:

- **M**: Number of validation examples
- **yᵢᵛᵃˡ**: True label of the i-th validation example
- **ŷᵢᵛᵃˡ**: Predicted output for the i-th validation example

## Importance of Monitoring Both Losses

- **Detect Overfitting**: Training loss decreases but validation loss increases, indicating the model is memorizing the training data.

- **Detect Underfitting**: Both losses remain high, showing the model is too simple or not learning patterns well.

- **Hyperparameter Tuning**: Loss trends help adjust learning rate, batch size, architecture, and regularization.

- **Generalization**: Validation loss reflects how well the model performs on unseen real-world data.

- **Optimize Training Process**: Monitoring both losses supports decisions like early stopping and learning rate scheduling.