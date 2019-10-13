# Picton

A webservice that tries to use machine learning to recognize the type of bird.

## Installation

To install this program you need to have Python 3(.6 or .7) and ```pip``` installed. (You can [download Python](https://www.python.org/downloads/) from this page or if you're using Ubuntu you can install Python using ```sudo apt install python3 python3-pip```)

Then download this repository, if you're on Linux or macOS use: 

```bash
git clone https://github.com/CSMdevs/Picton.git
```

If you're using Windows download the .zip file from [here](https://github.com/csmdevs/picton/master.zip).

Now open the folder in the command line, and install the Python requirements using:

```bash
pip3 install -r requirements.txt
```

If you're using Linux you need to install the following libraries using : ```sudo apt install libsm6 libxext6 libxrender-dev libglib2.0-0```

## Usage

If you want to run the webservice just run:

```bash
python3 app.py
```

You can just visit the service by going to: ```http://localhost:5000/```

### Add more birds

You can edit the ```main.py```, ```train.py``` and ```look.py``` to add more birds.

Run ```main.py``` to download training images, and convert them. Then train them by running ```train.py```.

# License

[MIT](/LICENSE.md)
