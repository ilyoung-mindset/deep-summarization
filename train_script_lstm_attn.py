from algorithms import lstm, gru

# Get the review summary file
review_summary_file = 'extracted_data/review_summary.csv'

# Do using LSTM cell - with attention mechanism
out_file = 'result/test_results_lstm_with_attention.csv'
lstm_net = lstm.NeuralNet(review_summary_file, attention = True)
lstm_net.set_parameters(batch_size=2, memory_dim=4,learning_rate=0.05)
lstm_net.begin_session()
lstm_net.form_model_graph()
lstm_net.fit()
lstm_net.predict()
lstm_net.store_test_predictions(out_file)
lstm_net.close_session()
