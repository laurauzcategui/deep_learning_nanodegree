# RNNs 

## RNNs Characteristics 

- Able to capture temporal dependencies over time.
- Modeling temporal data is critical
- Incorporating memory is crucial for analysing sequence data.

## RNNs Weakness

 The main weakness from RNNs is that the state is shortly stored, and its squeezed through the activation function causing then the problem of vanishing gradient. 

 Over backpropagation step, when updating the weights the values of the derivatives might be so small that when multiplying those cause the gradients to almost vanish. 

 Then LSTMs come to the rescue.

## Long Short Term Memory ( LSTMs )

