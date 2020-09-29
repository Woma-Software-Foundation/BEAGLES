# Introduction [![GitHub version](https://badge.fury.io/gh/rjdbcm%2FBEAGLES.svg)](https://badge.fury.io/gh/rjdbcm%2FBEAGLES)[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/rjdbcm/BEAGLES/graphs/commit-activity)[![Maintainability](https://api.codeclimate.com/v1/badges/4a252ae7978e72fe850a/maintainability)](https://codeclimate.com/github/rjdbcm/BEAGLES/maintainability)

BEAGLES stands for **BE**havioral **A**nnotation and **G**esture **LE**arning **S**uite, and is intended for behavioral analysis and quantification. BEAGLES is a graphical image annotation 
tool originally forked from [labelImg](https://github.com/tzutalin/labelImg) and frontend for a fork of 
[darkflow](https://github.com/thtrieu/darkflow). 

##### Created Using:

[![python](https://img.shields.io/badge/python-3.7%20|%203.8-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![tensorflow](https://raw.githubusercontent.com/aleen42/badges/master/src/tensorflow.svg?)](https://www.tensorflow.org/)
[![cython](https://img.shields.io/badge/Cython-0.29.6-%23646464)](https://cython.org)
[![numpy](https://img.shields.io/badge/NumPy-1.18-013243)](https://numpy.org/)
[![opencv](https://img.shields.io/badge/OpenCV-4.0-%233a6aeb)](https://opencv.org/)
[![pyqt5](https://img.shields.io/badge/PyQt-5.12-41cd52.svg)](https://pypi.org/project/PyQt5/)
[![traces](https://img.shields.io/badge/traces-0.5.0-orange.svg)](https://github.com/datascopeanalytics/traces)

##### Build Status:

|  Branch  |                     Status                     |
|:---------:|:------------------------------------------------:|
| master   |[![codecov](https://codecov.io/gh/rjdbcm/BEAGLES/branch/master/graph/badge.svg)](https://codecov.io/gh/rjdbcm/BEAGLES)[![Build Status](https://travis-ci.org/rjdbcm/BEAGLES.svg?branch=master)](https://travis-ci.org/rjdbcm/BEAGLES)
| dev      |[![codecov](https://codecov.io/gh/rjdbcm/BEAGLES/branch/dev/graph/badge.svg)](https://codecov.io/gh/rjdbcm/BEAGLES)[![Build Status](https://travis-ci.org/rjdbcm/BEAGLES.svg?branch=dev)](https://travis-ci.org/rjdbcm/BEAGLES)

##### Features:

- Darknet-style configuration files 
- TensorFlow checkpoint files
- YOLO and VOC annotation formats
- Automatic anchor box generation
- Preconfigured to output training data to TensorBoard
- Fixed or cyclic learning rates 
- Command-line backend interface 
- Human-in-the-loop prediction and dataset expansion

##### Feature Wishlist:

- YOLOv3 detection
- Automatic [hyperparameter tuning](https://github.com/autonomio/talos#Talos) using talos

##### Development Goals:

- Code coverage of \>60% (*in progress*)
- Improve maintainability to A rating (*in progress*)
- [OBS Studio](https://github.com/obsproject/obs-studio) utility for USB camera arrays (*in progress*)
- Statistical report generation using [traces](https://github.com/datascopeanalytics/traces) (*in progress*)
- TensorFlow 2 native code (*separate development branch created*)

<details>
  <summary>Table of Contents:</summary>

## Table of Contents
* [Installation](#installation)
    * [Source Install](#source-install-virtualenv)
    * [Binary Build](#binary-build)
    * [Open BEAGLES](#open-BEAGLES)
* [Controls](#controls)
* [Image Annotation](#image-annotation)
    * [Verify Image](#verify-image)
    * [Difficult](#difficult)
* [Important Directories](#important-directories)
* [How to Contribute](#how-to-contribute)
* [License](#license)
* [Related](#related)

</details>

## Installation

### Source Install (virtualenv)

Navigate to the source directory and run the following commands:

```
cd build/
./build-venv.sh
cd ..
make
```

### Binary Build

Scripts are included in `build/` for those interested but are **NOT** **RECOMMENDED**.

### Open BEAGLES
From the source directory run:
```
./BEAGLES.py
```

## Controls
|  Hotkey  |                     Action                     |
|----------|------------------------------------------------|
| Ctrl ⇧ a | Toggle advanced mode toolbar                   |
| Ctrl +   | Zoom in                                        |
| Ctrl -   | Zoom out                                       |
| Ctrl i   | Choose a video to import frames for annotation |
| Ctrl u   | Choose a directory to load images from         |
| Ctrl r   | Change the default annotation directory        |
| Ctrl s   | Save                                           |
| Crtl d   | Duplicate the selected label and bounding box  |
| Ctrl t   | Open machine learning interface                |
| Space    | Flag the current image as verified             |
| w        | Create a new bounding box                      |
| d        | Next image                                     |
| s        | Previous Image                                 |
| del      | Delete the selected bounding box               |
| ↑→↓←     | Move the selected bounding box                 |

## Image Annotation
### Verify Image

When pressing space, the user can flag the image as verified, a green background will appear.
This is used when expanding a training dataset automatically, the user can then through all the pictures and flag them instead of annotate them.

### Difficult

The difficult field being set to 1 indicates that the object has been annotated as "difficult", for example an object which is clearly visible but difficult to recognize without substantial use of context.
According to your deep neural network implementation, you can include or exclude difficult objects during training.

## Important Directories
* Frames are imported to a folder named for the video filename in ```data/rawframes```.

* When you press Commit Frames images in the open directory with matching annotation files are moved into ```data/committedframes```.

* Tensorboard summaries are found in```data/summaries```

* Training checkpoints are saved in```data/ckpt```

* Frozen graph files (*.pb, *.meta) output in```data/built_graph```

* Model configurations are stored in```data/cfg```

* Pretrained weights should be saved into```data/bin```

* Text-based log files are in ```data/logs```

* Image sets to annotate are stored in ```data/sample_img```


## How to contribute

See the section on contributing in the developer wiki [here](https://github.com/rjdbcm/BEAGLES/wiki/Developer-Guide#contributing).

## License

### Free software:
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rjdbcm/slgrSuite/blob/master/NOTICE)

### Based in part on original code by: 
- Tzutalin. LabelImg. Git code (2015). https://github.com/tzutalin/labelImg
- Mahmoud Aslan. Cyclic Learning Rate. Git code (2018). https://github.com/mhmoodlan/cyclic-learning-rate


## Related

1. [labelImg](https://github.com/tzutalin/labelImg) the original image annotation software BEAGLES is forked from
2. [darkflow](https://github.com/thtrieu/darkflow) the original basis of the machine learning backend
3. [cyclic-learning-rate](https://github.com/mhmoodlan/cyclic-learning-rate) the implementation of cyclic learning rates used
4. [traces](https://github.com/datascopeanalytics/traces) library for non-transformative unevenly-spaced timeseries analysis
5. [OBS Studio](https://github.com/obsproject/obs-studio) video recording software
6. [You Only Look Once:Unified, Real-Time Object Detection](https://pjreddie.com/media/files/papers/yolo_1.pdf)
7. [YOLO9000: Better, Faster, Stronger](https://pjreddie.com/media/files/papers/YOLO9000.pdf)
8. [A Framework for the Analysis of Unevenly Spaced Time Series Data](http://www.eckner.com/papers/unevenly_spaced_time_series_analysis.pdf)
9. [Unevenly-spaced data is actually pretty great](https://datascopeanalytics.com/blog/unevenly-spaced-time-series/) 
10. [Interactive machine learning: experimental evidence for the human in the algorithmic loop](https://link.springer.com/content/pdf/10.1007/s10489-018-1361-5.pdf)
11. [Why Momentum Really Works](https://distill.pub/2017/momentum/)
