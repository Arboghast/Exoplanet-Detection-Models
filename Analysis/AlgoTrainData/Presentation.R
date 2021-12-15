# load reticulate and use it to load numpy
library(reticulate)
library(ggplot2)
library(patchwork)
np <- import("numpy")
plt <- import ("matplotlib.pyplot") 

# load all the csv files 
gru_data <- read.csv("AlgoData/GRU_Data.csv")
lstm_data <- read.csv("AlgoData/LSTM_Data.csv")
rnn_data <- read.csv("AlgoData/RNN_Data.csv")
lr_data <- read.csv("AlgoData/LR_Data.csv")
dft_data <- read.csv("AlgoData/DFT_Data.csv")

gru_data 
lstm_data 
rnn_data 
lr_data
dft_data

# ------------------------------------------------------------------------------
# gru line graph
gru_acc <- ggplot (gru_data, aes(x = epoch, y = accuracy)) + geom_line() + geom_point() 
gru_acc
gru_loss <- ggplot (gru_data, aes(x = epoch, y = loss)) + geom_line() + geom_point()
gru_loss
gru_acc + gru_loss

gru_total <- ggplot(gru_data, aes(x=epoch)) +
  
  geom_line( aes(y=accuracy), color = 'red') + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss), color = 'blue') + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
gru_total

# ------------------------------------------------------------------------------
# lstm line graph
lstm_acc <- ggplot (lstm_data, aes(epoch, y = accuracy)) + geom_line() + geom_point()
lstm_acc
lstm_loss <- ggplot (lstm_data, aes(epoch, y = loss)) + geom_line() + geom_point()
lstm_loss
lstm_acc + lstm_loss

lstm_total <- ggplot(lstm_data, aes(x=epoch)) +
  
  geom_line( aes(y=accuracy), color = 'red') + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss), color = 'blue') + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
lstm_total

# ------------------------------------------------------------------------------
# rnn line graph
rnn_acc <- ggplot (rnn_data, aes(x = epoch, y = accuracy)) + geom_line() + geom_point()
rnn_acc
rnn_loss <- ggplot (rnn_data, aes(x = epoch, y = loss)) + geom_line() + geom_point()
rnn_loss
rnn_acc + rnn_loss

rnn_total <- ggplot(rnn_data, aes(x=epoch)) +
  
  geom_line( aes(y=accuracy), color='red') + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss), color='blue') + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
rnn_total

# ------------------------------------------------------------------------------
# merge all the data frames
train_data <- rbind(gru_data, lstm_data, rnn_data)
train_data

train_data_acc <- ggplot(train_data, aes(epoch, accuracy, color = algorithm)) + 
  geom_line() + geom_point()
train_data_acc
train_data_loss <- ggplot(train_data, aes(epoch, loss, color = algorithm)) + 
  geom_line() + geom_point()
train_data_loss

train_data_acc + train_data_loss

train_data_total <- ggplot(train_data, aes(x=epoch, color = algorithm)) +
  
  geom_line( aes(y=accuracy)) + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss)) + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
train_data_total

# ------------------------------------------------------------------------------
# lr data

lr_acc <- ggplot (lr_data, aes(x = epoch, y = accuracy)) + geom_line() + geom_point() 
lr_acc

lr_loss <- ggplot (lr_data, aes(x = epoch, y = loss)) + geom_line() + geom_point()
lr_loss

lr_acc + lr_loss

lr_total <- ggplot(lr_data, aes(x=epoch)) +
  
  geom_line( aes(y=accuracy), color = 'red') + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss), color = 'blue') + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
lr_total

# ------------------------------------------------------------------------------
# dft data

dft_acc <- ggplot (dft_data, aes(x = epoch, y = accuracy)) + geom_line() + geom_point()
dft_acc

dft_loss <- ggplot (dft_data, aes(x = epoch, y = loss)) + geom_line() + geom_point()
dft_loss

dft_acc + dft_loss

dft_total <- ggplot(dft_data, aes(x=epoch)) +
  
  geom_line( aes(y=accuracy), color = 'red') + geom_point(aes(y=accuracy)) +
  geom_line( aes(y=loss), color = 'blue') + geom_point(aes(y=loss)) + 
  
  scale_y_continuous(
    
    # Features of the first axis
    name = "Accuracy",
    
    # Add a second axis and specify its features
    sec.axis = sec_axis(~.*0.05,  name="Loss")
  )
dft_total








