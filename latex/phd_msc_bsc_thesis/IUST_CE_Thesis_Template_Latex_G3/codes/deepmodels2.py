from keras.models import Sequential, load_model
from keras.layers import Dense, Activation, Dropout
from keras.layers import LSTM, Bidirectional

# Unidirectional LSTM (Many to One)
def model_1(input_dim, output_dim):
    print('Build model...')
    model = Sequential()
    model.add(LSTM(128, input_shape=input_dim))
    model.add(Dense(output_dim))
    model.add(Activation('softmax'))
    return model, 'model_1'

# Unidirectional LSTM (Many to One)
def model_2(input_dim, output_dim):
    model = Sequential()
    model.add(LSTM(128, input_shape=input_dim, return_sequences=True))
    model.add(LSTM(128, input_shape=input_dim, return_sequences=False))
    model.add(Dense(output_dim))
    model.add(Activation('softmax'))
    return model, 'model_2'

# Unidirectional LSTM (Many to One)
def model_3(input_dim, output_dim):
    model = Sequential()
    model.add(LSTM(256, input_shape=input_dim, return_sequences=True, recurrent_dropout=0.1))
    model.add(Dropout(0.3))
    model.add(LSTM(256, input_shape=input_dim, return_sequences=False, recurrent_dropout=0.1))
    model.add(Dropout(0.3))
    model.add(Dense(output_dim))
    model.add(Activation('softmax'))
    return model, 'model_3'

# Bidirectional LSTM (Many to One)
def model_4_1(input_dim, output_dim):
    model = Sequential()
    model.add(Bidirectional(LSTM(256, return_sequences=False), input_shape=input_dim, merge_mode='sum'))
    model.add(Dense(output_dim))
    model.add(Activation('softmax'))
    return model, 'model_4_1'

# Bidirectional Deep LSTM (Many to One)
def model_4_2(input_dim, output_dim):
    model = Sequential()
    model.add(Bidirectional(LSTM(128, return_sequences=True), input_shape=input_dim,merge_mode='sum'))
    model.add(Bidirectional(LSTM(128, return_sequences=False), merge_mode='sum'))
    model.add(Dense(output_dim))
    model.add(Activation('softmax'))
    return model, 'model_4_2'
# End of model definition