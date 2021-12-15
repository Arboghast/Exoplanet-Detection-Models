# load reticulate and use it to load numpy
library(reticulate)
library(ggplot2)
library(patchwork)
np <- import("numpy")
plt <- import ("matplotlib.pyplot") 

# load all the csv files 
gru <- read.csv("TrainData/GRUtraining.csv")
lstm <- read.csv("TrainData/LSTMtraining.csv")
rnn <- read.csv("TrainData/RNNtraining.csv")

lr_data_acc <- read.csv("TrainData/multi-lr_acc.csv")
lr_data_loss <- read.csv("TrainData/multi-lr_loss.csv")
dft_data_acc <- read.csv("TrainData/multi-lr-dft_acc.csv")
dft_data_loss <- read.csv("TrainData/multi-lr-dft_loss.csv")

lr_data_acc
lr_data_loss
dft_data_acc
dft_data_loss

# Unable for now
#ols <- read.csv("multi-lr-ols.csv")

# ------------------------------------------------------------------------------
# filter out unnecessary columns and add necessary columns

gru_data <- gru[c("epoch", "accuracy", "loss")]
gru_data['algorithm'] = 'gru'
gru_data

lstm_data <- lstm[c("epoch", "accuracy", "loss")]
lstm_data['algorithm'] = 'lstm'
lstm_data

rnn_data <- rnn[c("epoch", "accuracy", "loss")]
rnn_data['algorithm'] = 'rnn'
rnn_data

#add epoch and algorithms columns
lr_data_acc$epoch<-0:(nrow(lr_data_acc)-1)
colnames(lr_data_acc) <- c("accuracy", "epoch")
lr_data_acc <- lr_data_acc[c("epoch", "accuracy")]
lr_data_acc

lr_data_loss$epoch<-0:(nrow(lr_data_loss)-1)
colnames(lr_data_loss) <- c("loss", "epoch")
lr_data_loss <- lr_data_loss[c("epoch", "loss")]
lr_data_loss

dft_data_acc$epoch<-0:(nrow(dft_data_acc)-1)
colnames(dft_data_acc) <- c("accuracy", "epoch")
dft_data_acc <- dft_data_acc[c("epoch", "accuracy")]
dft_data_acc

dft_data_loss$epoch<-0:(nrow(dft_data_loss)-1)
colnames(dft_data_loss) <- c("loss", "epoch")
dft_data_loss <- dft_data_loss[c("epoch", "loss")]
dft_data_loss

lr_data <- merge(lr_data_acc, lr_data_loss, by= "epoch")
lr_data['algorithm'] = 'lr'
lr_data

dft_data <- merge(dft_data_acc, dft_data_loss, by= "epoch")
dft_data['algorithm'] = 'dft'

# Remove x-axis data
gru_data1 <- gru_data[c("epoch", "accuracy", "loss", "algorithm")]
lstm_data1 <- lstm_data[c("epoch", "accuracy", "loss", "algorithm")]
rnn_data1 <- rnn_data[c("epoch", "accuracy", "loss", "algorithm")]
lr_data1 <- lr_data[c("epoch", "accuracy", "loss", "algorithm")]
dft_data1 <- dft_data[c("epoch", "accuracy", "loss", "algorithm")]

# write files
write.csv(gru_data1, file = 'AlgoData/GRU_Data.csv', row.names = FALSE)
write.csv(lstm_data1, file = 'AlgoData/LSTM_Data.csv', row.names = FALSE)
write.csv(rnn_data1, file = 'AlgoData/RNN_Data.csv', row.names = FALSE)
write.csv(lr_data1, file = 'AlgoData/LR_Data.csv', row.names = FALSE)
write.csv(dft_data1, file = 'AlgoData/DFT_Data.csv', row.names = FALSE)

