## Intro to Deep Learning Notes

### Lesson 3 - Applying Deep Learning 

On this lesson I was able to progress on: 

- [Using Fast Style Transfer](https://github.com/lengstrom/fast-style-transfer), a repository that use Tensorflow CNN for Fast style transfer. 

    *Notes*
    
    - This project was originally created on Tensorflow 1, so in order to make it work with the container in TF 2.0 I had to modify the code using: 

        ```
        from tensorflow.compat.v1 import ConfigProto
        from tensorflow.compat.v1 import Session
        from tensorflow.compat.v1 import placeholder
        from tensorflow.compat.v1.train import Saver
        ```

- [Deep Traffic Project](https://selfdrivingcars.mit.edu/deeptraffic/), is a project / competition that uses deep reinforcement learning, with the goal to create neural networks to simulate high way traffic and drive a vehicle as fast as possible. 

    *Notes*
    - Input: car surroundings, where the car with respect to lane, other cars..
    - Actions: move left/right, accelerate or not.

- [Flappybird](https://github.com/yenchenlin/DeepLearningFlappyBird), this project use Deep Q-Network in order to learn how to play flappy bird. 

    *Notes*
    - It doesn't work properly with a docker container, therefore I had to apply some tweaks as follows: 


        ```
        export LD_LIBRARY_PATH="/home/udacity/miniconda/lib:$LD_LIBRARY_PATH"
        export SDL_VIDEODRIVER="dummy"
        export SDL_AUDIODRIVER="dummy"

        sudo apt-get install -y libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
        ```

    **What is Deep Q-Network?**
    
    > It is a convolutional neural network, trained with a variant of Q-learning, whose input is raw pixels and whose output is a value function estimating future rewards.

    