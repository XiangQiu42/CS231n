import numpy as np
from random import shuffle
from past.builtins import xrange

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)

  Inputs have dimension D, there are C classes, and we operate on minibatches
  of N examples.

  Inputs:
  - W: A numpy array of shape (D, C) containing weights.
  - X: A numpy array of shape (N, D) containing a minibatch of data.
  - y: A numpy array of shape (N,) containing training labels; y[i] = c means
    that X[i] has label c, where 0 <= c < C.
  - reg: (float) regularization strength

  Returns a tuple of:
  - loss as single float
  - gradient with respect to weights W; an array of same shape as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]
  num_class = W.shape[1]
 
  for i in range(num_train):
      scores = X[i].dot(W)
      correct_class_score = scores[y[i]]
      exp_sum = np.sum(np.exp(scores))
      loss += -correct_class_score + np.log(exp_sum)
      
      dW[:,y[i]] += -X[i]
      for j in range(num_class):
         dW[:,j] += (np.exp(scores[j])/exp_sum) * X[i]
        
         
      

  loss /= num_train 
  dW = dW/num_train
  
  loss += 0.5*reg*np.sum(W*W)
  dW += reg*W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[0]

  scores = X.dot(W)
  scores_exp_sum = np.sum(np.exp(scores),axis = 1).reshape(num_train, 1)
  correct_scores = scores[np.arange(num_train),y].reshape(num_train, 1) 
  loss += np.sum( np.log(scores_exp_sum) - correct_scores )
                          
  mask = np.exp(scores)/scores_exp_sum
  mask[np.arange(num_train),y] += -1
  dW = X.T.dot(mask)

  loss /= num_train
  dW /= num_train

  loss += 0.5*reg*np.sum(W*W)
  dW +=  reg*W
  ############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW

