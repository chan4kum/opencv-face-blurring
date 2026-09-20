# Face Blurring / Anonymization

Automatically blurs every face in an image or live webcam feed to protect privacy.

Part of a series of beginner-friendly OpenCV projects.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
python main.py --image group.jpg --output blurred.jpg
python main.py                  # webcam
```

Press `q` to quit any live window.

## License

MIT
