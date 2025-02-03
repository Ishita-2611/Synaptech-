from brainflow.board_shim import BoardShim, BrainFlowInputParams

def acquire_eeg():
    params = BrainFlowInputParams()
    params.serial_port = 'COM3'  # Update for your device

    board = BoardShim(2, params)  # 2 = OpenBCI Cyton
    board.prepare_session()
    board.start_stream()

    print("Collecting EEG Data...")
    data = board.get_board_data()
    
    board.stop_stream()
    board.release_session()
    
    return data

if __name__ == "__main__":
    eeg_data = acquire_eeg()
    print("EEG Data Shape:", eeg_data.shape)
