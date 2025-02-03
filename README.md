# Synaptech-
# 🧠 BCI Laptop Control

This project enables users to control their laptop using a **Brain-Computer Interface (BCI) Kit**. The system processes EEG signals and translates them into keyboard and mouse actions, allowing hands-free control.

## 🚀 Features
- **Real-time EEG Data Acquisition** 📡
- **Signal Preprocessing & Filtering** 🎛️
- **Machine Learning-Based Signal Classification** 🤖
- **Keyboard & Mouse Control via EEG** 🖥️

## 📂 Project Structure
```
BCI_Laptop_Control/
│── data/                  # EEG datasets, raw signals, trained models
│── src/                   # Source code
│   ├── acquisition.py     # Collect EEG data
│   ├── preprocessing.py   # Filter & preprocess signals
│   ├── classification.py  # Machine learning for command classification
│   ├── control.py         # Simulate keyboard & mouse actions
│   ├── main.py            # Main script to run the system
│── notebooks/             # Jupyter notebooks for analysis
│── requirements.txt       # Python dependencies
│── README.md              # Documentation
│── config.yaml            # Configuration settings
```

## 🔧 Installation & Setup
### 1️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate     # (Windows)
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the BCI Control System
```bash
python src/main.py
```

## 🧠 Supported BCI Devices
- OpenBCI Cyton
- Emotiv Epoc
- Muse Headband
- NeuroSky MindWave

## 🎯 How It Works
1. **Acquire EEG Data** → Reads signals from a BCI headset.
2. **Preprocess Signals** → Filters noise and extracts meaningful features.
3. **Classify Brain Signals** → Uses an ML model to map EEG data to commands.
4. **Control Laptop** → Sends corresponding keyboard/mouse actions.

## 🎓 Future Improvements
- Improve ML model accuracy 🎯
- Add deep learning-based classification 🧠
- Expand to more BCI devices 🎧

