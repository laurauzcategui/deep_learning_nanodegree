# Lesson 6 - Sentiment Prediction RNNs

This lesson was a bit tricky but fun. It was about how you can process text data and feed it into a RNN to give you sentiment prediction. 

### Steps followed

1. **Read a Text**
2. **Pre-process the text**
    
    2.1 Get rid of punctuation 
    2.2 Split the text by new lines 
3. **Encoding the vocabulary**

    This step is really important, because it will map each of your words in the vocabulary to an integer ( remember that neural nets likes working with numbers )

    In this case, the text was mapped by frequency

    Example: 

    ```python 
    vocab = {
        "the": 1000,
        "best": 100, 
        "worst": 50,
        "loved" : 200,
        "movie": 400
    }
    ```

4. **Tokenize each review**

    Once the encoding was done. The list of reviews was taken and one by one transformed to a list of tokens. 

    For example: 

    Imagine your review is: 
    
    "The best movie"

    | the          | best      | movie |
    | -------------|:---------:| -----:|
    | 1000         | 100       | 400   |

    And another review Models

7. **Split the data**

    It's a good and well known practice to split the data into:

    - Training 
    - Validation
    - Test 

    This way you check ifyour model is actually performing well by looking at data that hasn't seen before ( Validation) and make the respective adjustments until training is complete. 

8. **Definining a model**

    On this section, a RNN was created using: 

    - 1 Embedding layer
    - 1 LSTM Layer
    - 1 Dropout layer 
    - 1 Fully connected layer 
    - Applying sigmoid as last layer


Notebooks: 

- [Create a Sentiment RNN](./Sentiment_RNN_Exercise.ipynb), to perform Sentiment Analysis.

Resources: 
 - [LSTM Layers](https://pytorch.org/docs/stable/nn.html#lstm)
 - [Embedding Layers](https://pytorch.org/docs/stable/nn.html#embedding)
 - [Large Moview Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/), Staford publication on sentiment classification on IMDB movies reviews.